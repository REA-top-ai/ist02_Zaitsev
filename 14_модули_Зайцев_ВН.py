# Задание 1 (datetime)
from datetime import datetime
current_time = datetime.now()
print(current_time)

# Задание 2 (random)
import random
random_list = [random.randint(1, 100) for _ in range(101)]
random_number = random.choice(random_list)

# Задание 3 (matplotlib)
import matplotlib.pyplot as plt
import random
number_a = range(1, 13)
number_b = random.sample(range(1000), 12)
plt.plot(number_a, number_b)
plt.show()

# Задание 1 (сотрудники)
employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

def is_programmer(position):
    return "программист" in position.lower()

def bonus_programmer(employee):
    if is_programmer(employee[1]):
        return employee[3] * 0.03
    return 0

def gender_from_name(name):
    parts = name.split()
    if len(parts) >= 3 and parts[2].endswith('на'):
        return 'female'
    return 'male'

def holiday_bonus(employee):
    if gender_from_name(employee[0]) == 'female':
        return 2000
    else:
        return 2000

def indexation(employee):
    hire = datetime.strptime(employee[2], "%d.%m.%Y")
    years = (datetime.now() - hire).days / 365.25
    if years > 10:
        return employee[3] * 0.07
    else:
        return employee[3] * 0.05

def worked_more_than_6months(employee):
    hire = datetime.strptime(employee[2], "%d.%m.%Y")
    days = (datetime.now() - hire).days
    return days > 180

vacation_candidates = [e[0] for e in employees if worked_more_than_6months(e)]

# Задание 2 (розыгрыш)
def lottery_winner(admin_number, user_numbers):
    winners = []
    for num in user_numbers:
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum % admin_number == 0:
            winners.append(num)
        if len(winners) == 5:
            break
    return winners

# Самостоятельная работа 1
def coin_flip(attempts):
    for _ in range(attempts):
        print("Орел" if random.randint(0, 1) == 0 else "Решка")

# Самостоятельная работа 2
def dice_roll(attempts):
    for _ in range(attempts):
        print(random.randint(1, 6))

# Самостоятельная работа 3
import string
def generate_password(length):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))