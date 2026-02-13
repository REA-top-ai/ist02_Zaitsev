#Задание 1
print('Задание 1:')
a=(6*6)-1==8+1
b=13-7!=(3*2)+1
c=3*(2-1)==4-1

print('Утверждение 1:',a)
print('Утверждение 2:',b)
print('Утверждение 3:',c)

#Задание 2
print('Задание 2:')
a=(6*6)-1>=8+1
b=13-7<=(3*2)+1
c=3*(2-1)>4-1

print('Утверждение 1:',a)
print('Утверждение 2:',b)
print('Утверждение 3:',c)

#Задание 3
print('Задание 3:')
"""bool_variable = true
print(bool_variable)"""
# 1. Выводится ошибка: NameError: name 'true' is not defined. Она выводится так как True или False без кавычек пишутся только с заглавных букв.
bool_variable = 'true'
print(type(bool_variable))

# 2. тип - str
# 3. т.к это строка, а не булево значение

bool_variable_2 = True
print(bool_variable_2)
print(type(bool_variable_2))

#Задание 4
print('Задание 4:')
user_name= input()
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
abc = "Добро пожаловать,"
if user_name == 'Дмитрий':
    print(Dmitriy_check)
else:
    print(abc,user_name)
# user_name='Дмитрий': Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!
# user_name='Ангелина': Добро пожаловать, Ангелина

enter_number = 0
for enter_number in (1,2,3):
    if enter_number < 3:
        print('Попробуйте еще раз. У вас осталось',3-enter_number,'попыток')
    else:
        print('Вы превысили максимальное число попыток.Ваша учетная запись заблокирована.Для разблокировки обратитесь в службу поддержки')
#Задание 5
print('Задание 5:')
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

print(statement_one)
print(statement_two)


def check_access(user_name: str, arm: int) -> str:
    users_to_arm = {"Дмитрий": 1,"Ангелина": 2,"Василий": 3,"Екатерина": 4,}

    expected_arm = users_to_arm.get(user_name)

    if expected_arm is None:
        return "Логин или пароль не верный, попробуйте еще раз"

    if arm == expected_arm:
        return "Добро пожаловать!"

    if user_name == "Дмитрий":
        return Dmitriy_check

    return "Логин или пароль не верный, попробуйте еще раз"
e = [("Дмитрий", 1),("Ангелина", 1),("Дмитрий", 2),("Екатерина", 4),]
for user_name, arm in e:
    print(f"user_name={user_name!r}, ARM={arm} -> {check_access(user_name, arm)}")

#Задание 6
print('Задание 6:')
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

print(statement_one)
print(statement_two)


#Задание 7
print('Задание 7:')

Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
abc = "Добро пожаловать,"
user_name= input()
if user_name == 'Дмитрий':
    print(Dmitriy_check)
else:
    print(abc,user_name)


#Задание 8
print('Задание 8:')
grade = float(input())
if grade >= 4.0:
        print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0:
    print("C")
elif grade >= 1.0:
    print("D")
else:
    print("F")
