#Задание 1
contains_a = lambda my_string: 'a' in my_string
print(contains_a("adfa"))
print(contains_a("d4fc"))
#Задание 2
long_string = lambda word: True if len(word) >= 12 else False
print(long_string('qwertyuiopaa'))
#Задание 3
end_in_a = lambda word1: True if word1[-1] == 'a' else False
print(end_in_a("ff"))
#Задание 4
even_or_odd = lambda num: 'четное' if num % 2 ==0 else 'нечетное'
print(even_or_odd(8))
#Задание 5
multiple_of_three = lambda num: 'кратное трем' if num % 3 ==0 else 'не кратное'
print(multiple_of_three(7))
#Задание 6
rate_movie = lambda rating: 'Мне понравился этот фильм' if rating > 8.5 else 'Этот фильм был не очень хорошим'
print(rate_movie(8.6))