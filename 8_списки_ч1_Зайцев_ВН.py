# Задание 1
product = ["торт", 1]

# Задание 2 (бытовая химия)
household_chemicals = [["стиральный порошок", 1], ["средство для мытья посуды", 1]]

# Задание 3 (zip)
names = ["Alice", "Bob"]
dogs = ["Rex", "Fido"]
names_and_dogs_names = zip(names, dogs)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

# Задание 4 (append)
orders = ['маргаритки', 'васильки']
orders.append('тюльпаны')
orders.append('розы')
print(orders)

# Задание 5 (+)
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
broken_prices = [5, 3, 4, 5, 4] + [4]

# Задание 6 (range I)
list1 = range(9)
list2 = range(8)

# Задание 7 (range II)
list1 = range(5, 16, 3)
list2 = range(0, 40, 5)

# Задание 8
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
ages = []
ages.append(42)
all_ages = [32, 41, 29] + ages
name_and_age = zip(first_names, all_ages)
ids = range(4)