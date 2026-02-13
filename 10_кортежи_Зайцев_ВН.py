correct_answers = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
# предположим, что ответы пользователя хранятся в списке user_answers
user_answers = [1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1]  # пример
if list(user_answers) == list(correct_answers):
    print("Экзамен сдан")
else:
    print("Экзамен провален")
