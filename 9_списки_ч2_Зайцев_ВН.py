# Задание 1 (len)
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)
list1 = range(2, 20, 3)  # шаг 3

# Задание 2 (индексы)
employees = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4 = employees[4]
print(len(employees))
print(employees[6])

# Задание 3 (отрицательные индексы)
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'помидоры', 'хлеб', 'сыр']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5, last_element)

# Задание 4 (срезы)
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:4]
middle = suitcase[2:4]
start = suitcase[:3]

# Задание 5 (count)
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

# Задание 6 (sort)
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

# Задание 7 (sorted)
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games)
print(games_sorted)

# Задание 8 (inventory)
inventory = ["двухспальная кровать", "двухспальная кровать", "изголовье", "двуспальная кровать", "двуспальная кровать", "комод", "комод", "стол", "стол", "тумбочка", "тумбочка", "королевская кровать", "двуспальная кровать", "две односпальные кровати", "две односпальные кровати", "простыни", "простыни", "подушка", "подушка"]
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("две односпальные кровати")
inventory.sort()
print(inventory_len, first, last, inventory_2_6, first_3, twin_beds)
