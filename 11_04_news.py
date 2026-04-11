import requests
from datetime import datetime, timedelta

NEWS_API_KEY = "a4cbede0493b48788d419d7ba0abe349"
MISTRAL_API_KEY = "fKASp2OcwqCcTRCFMOd6nFPMSKp5cTlJ"


def get_news(query):
    url = "https://newsapi.org/v2/everything"

    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    params = {
        "q": query,
        "from": yesterday,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "ok":
        raise Exception(f"Ошибка NewsAPI: {data}")

    return data["articles"][:10]  # ограничим 10 статьями



def generate_summary(articles):
    url = "https://api.mistral.ai/v1/chat/completions"

    articles_text = ""
    for i, article in enumerate(articles, 1):
        articles_text += f"{i}. {article.get('title', '')}\n{article.get('description', '')}\n\n"

    prompt = f"""
Ты аналитик новостей.
На основе новостей за последний день сделай аналитическую сводку.

Требования: 250-300 слов;На русском языке;Анализ (не просто пересказ);Вывод в конце

Новости:
{articles_text}
"""

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "choices" not in result:
        raise Exception(f"Ошибка Mistral API: {result}")

    return result["choices"][0]["message"]["content"]


def save_to_file(text, filename="summary.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    topic = "artificial intelligence"  # тема

    articles = get_news(topic)
    summary = generate_summary(articles)

    print(summary)
    save_to_file(summary)

    print("\nГотово! Сохранено в summary.txt")