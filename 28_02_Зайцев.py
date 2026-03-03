import json
from typing import List, Dict, Any, Optional, Callable
from functools import reduce
import re


def parse_log_line(line: str) -> Dict[str, Any]:

    date_part, level, message_part = line.split("|", 2)

    result = {"date": date_part, "level": level}


    pairs = re.findall(r'(\w+)=([^\s]+)', message_part)

    for key, value in pairs:
        try:
            if '.' in value:
                result[key] = float(value)
            else:
                result[key] = int(value)
        except ValueError:
            result[key] = value

    return result


def parse_logs(log_lines: List[str]) -> List[Dict[str, Any]]:

    return [parse_log_line(line) for line in log_lines]


def save_to_json(logs: List[Dict[str, Any]], filename: Optional[str] = None) -> str:

    json_str = json.dumps(logs, ensure_ascii=False, indent=2)

    if filename:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)

    return json_str


def filter_logs(logs: List[Dict[str, Any]], **filters) -> List[Dict[str, Any]]:

    def matches(log: Dict[str, Any]) -> bool:
        for key, value in filters.items():
            if log.get(key) != value:
                return False
        return True

    return list(filter(matches, logs))


# Агрегационные функции
def count_by_level(logs: List[Dict[str, Any]]) -> Dict[str, int]:
    return _count_by_key(logs, "level")


def count_by_user(logs: List[Dict[str, Any]]) -> Dict[str, int]:

    return _count_by_key(logs, "user")


def _count_by_key(logs: List[Dict[str, Any]], key: str) -> Dict[str, int]:

    result = {}
    for log in logs:
        value = log.get(key)
        if value:
            result[value] = result.get(value, 0) + 1
    return result


def sum_amount_for_failed_payments(logs: List[Dict[str, Any]]) -> int:

    failed_payments = filter_logs(logs, action="payment", status="fail")
    return sum(log.get("amount", 0) for log in failed_payments)


def get_unique_users(logs: List[Dict[str, Any]]) -> List[str]:

    users = {log.get("user") for log in logs if log.get("user")}
    return sorted(users)


def get_stats_by_action(logs: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    stats = {}

    for log in logs:
        action = log.get("action")
        status = log.get("status", "unknown")

        if action not in stats:
            stats[action] = {"success": 0, "fail": 0, "unknown": 0}

        stats[action][status] = stats[action].get(status, 0) + 1

    return stats


def print_logs(logs: List[Dict[str, Any]], title: str = "Logs"):

    print(f"\n{title}:")
    if not logs:
        print("  No logs found")
        return

    for log in logs:
        print(f"  {log}")


if __name__ == "__main__":
    logs = [
        "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
        "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
        "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
        "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
        "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
    ]

    parsed_logs = parse_logs(logs)

    json_output = save_to_json(parsed_logs, "logs.json")
    print("JSON saved to logs.json")

    print_logs(filter_logs(parsed_logs, status="fail"), "FAIL ONLY")
    print_logs(filter_logs(parsed_logs, level="ERROR"), "ONLY ERRORS")
    print_logs(filter_logs(parsed_logs, user="anna"), "ONLY anna")

    print("\n--- COUNT BY LEVEL ---")
    print(count_by_level(parsed_logs))

    print("\n--- COUNT BY USER ---")
    print(count_by_user(parsed_logs))

    print("\n--- SUM AMOUNT FOR FAILED PAYMENTS ---")
    print(f"Total: {sum_amount_for_failed_payments(parsed_logs)}")

    print("\n--- UNIQUE USERS ---")
    print(get_unique_users(parsed_logs))

    print("\n--- STATS BY ACTION ---")
    print(json.dumps(get_stats_by_action(parsed_logs), indent=2, ensure_ascii=False))