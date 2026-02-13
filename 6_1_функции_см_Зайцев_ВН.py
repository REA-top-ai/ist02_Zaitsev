# Задача 1
def f_to_c(f_temp):
    return (f_temp - 32) * 5 / 9
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
    return c_temp * 9/5 + 32
c0_in_fahrenheit = c_to_f(0)

# Задача 2
train_mass = 22680
train_acceleration = 10
train_distance = 100
def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print("Поезд GE поставляет", train_force, "ньютонов силы")

def get_energy(mass, c=3*10**8):
    return mass * c**2
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print("1 кг бомбы составляет", bomb_energy, "Джоулей")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("Поезд выполняет", train_work, "Джоулей за", train_distance, "метров.")

# Задача 3
clothes = "домашняя одежда"
print("У меня большой гардероб")
print("Утром лучше всего подходит", clothes)
print("Днем лучше всего подходит", clothes)
print("Вечером лучше всего подходит", clothes)
print("Ночью лучше всего подходит", clothes)
meal = "завтрак"
print("мои предпочтения в еде")
print("Утром лучше всего подходит", meal)
meal = "обед"
print("Днем лучше всего подходит", meal)
meal = "ужин"
print("Вечером лучше всего подходит", meal)

# Задача 4
def check_access(user_name, arm):
    users = {"Дмитрий": 1, "Ангелина": 2, "Василий": 3, "Екатерина": 4}
    if user_name in users and users[user_name] == arm:
        print("Добро пожаловать!")
    elif user_name == "Дмитрий":
        print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
    else:
        print("Логин или пароль не верный, попробуйте еще раз")

# Задача 5
def get_grade(score):
    if score >= 4.0:
        return "A"
    elif score >= 3.0:
        return "B"
    elif score >= 2.0:
        return "C"
    elif score >= 1.0:
        return "D"
    else:
        return "F"
