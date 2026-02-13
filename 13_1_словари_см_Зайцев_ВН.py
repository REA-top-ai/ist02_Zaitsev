# Задание 1
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {k: v for k, v in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
    total = 0
    for char in word.upper():
        total += letter_to_points.get(char, 0)
    return total

# Проверка
print(score_word("BLUE"))

player_to_words = {
    "player1": ["BLUE", "EARTH", "ERASER", "ZAP", "TENNIS", "EYES", "BELLY", "COMA", "EXIT", "MACHINE", "HUSKY", "PERIOD"],
    "wordNerd": ["BLUE", "EARTH", "ERASER", "ZAP", "TENNIS", "EYES", "BELLY", "COMA", "EXIT", "MACHINE", "HUSKY", "PERIOD"],
    "Lexi Con": ["BLUE", "EARTH", "ERASER", "ZAP", "TENNIS", "EYES", "BELLY", "COMA", "EXIT", "MACHINE", "HUSKY", "PERIOD"],
    "Prof Reader": ["BLUE", "EARTH", "ERASER", "ZAP", "TENNIS", "EYES", "BELLY", "COMA", "EXIT", "MACHINE", "HUSKY", "PERIOD"]
}

player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points
print(player_to_points)

# Дополнительные задания
def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]

def update_point_totals():
    for player, words in player_to_words.items():
        player_to_points[player] = sum(score_word(word) for word in words)

letter_to_points_lower = {k.lower(): v for k, v in letter_to_points.items()}
letter_to_points_lower.update({k: v for k, v in letter_to_points.items()})