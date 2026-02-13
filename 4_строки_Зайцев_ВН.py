# Задание 1
favour_word = "программирование"
print(favour_word)

# Задание 2
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]

# Задание 3
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]
new_account = account_generator(first_name, last_name)

# Задание 4
def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]
temp_password = password_generator(first_name, last_name)

# Задание 5
company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# Задание 6
first_name = "Rob"
try:
    first_name[0] = "P"
except TypeError:
    pass
fixed_first_name = "P" + first_name[1:]

# Задание 7
password = "theycallme\"crazy\"91"

# Задание 8
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)