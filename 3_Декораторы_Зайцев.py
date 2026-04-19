from functools import wraps
import time
import random

# 1. декораторы
def is_alive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hero = args[0]
        if hero.health <= 0:
            print(f"{hero.name} мёртв и не может действовать!")
            return None
        return func(*args, **kwargs)
    return wrapper

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        result = func(*args, **kwargs)
        print("[LOG] Действие завершено")
        return result
    return wrapper

# 2. Класс hero
class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class
        if hero_class == "волшебник":
            self.health = 60
            self.mana = 50
        elif hero_class == "воин":
            self.health = 100
            self.mana = 10
        else:
            raise ValueError("Неизвестный класс")
        self.spells_names = {}
        self.items = {}

    @is_alive
    def attack(self, damage):
        print(f"{self.name} нанёс урон: {damage}")

    @log_action
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} восстановил {amount} здоровья. Теперь {self.health}")

    @is_alive
    def cast_spell(self, spell_name):
        if spell_name not in self.spells_names:
            print("Заклинание не изучено")
            return
        spell = self.spells_names[spell_name]
        if self.mana < spell["mana_cost"]:
            print("Не хватает маны")
            return
        self.mana -= spell["mana_cost"]
        print(f"{self.name} применил {spell_name}")
        if spell["attack_damage"] > 0:
            print(f"Урон: {spell['attack_damage']}")
        if spell["health_increase"] > 0:
            self.health += spell["health_increase"]
            print(f"Лечение: {spell['health_increase']}")

    def add_spell(self, name, mana_cost, attack_damage, health_increase):
        self.spells_names[name] = {
            "mana_cost": mana_cost,
            "attack_damage": attack_damage,
            "health_increase": health_increase
        }

    def add_item(self, item_name, stat, value):
        if len(self.items) >= 6:
            print("Нельзя надеть больше 6 предметов")
            return
        self.items[item_name] = {stat: value}
        if stat == "health":
            self.health += value
        elif stat == "mana":
            self.mana += value

# 3. самостоятельная работа (пасхальные декораторы)
def easter_health_boost(duration):
    """Удваивает здоровье героя на время (пасхальный ивент)"""
    def decorator(func):
        @wraps(func)
        def wrapper(hero, *args, **kwargs):
            old_hp = hero.health
            hero.health *= 2
            print(f"[EVENT] Здоровье удвоено → {hero.health}")
            result = func(hero, *args, **kwargs)
            time.sleep(duration)
            hero.health = old_hp
            print(f"[EVENT] Здоровье восстановлено → {hero.health}")
            return result
        return wrapper
    return decorator

def easter_mana_boost(duration):
    """дает волшебникам +5 маны на время (священный посох)"""
    def decorator(func):
        @wraps(func)
        def wrapper(hero, *args, **kwargs):
            if hero.hero_class != "волшебник":
                return func(hero, *args, **kwargs)
            old_mp = hero.mana
            hero.mana += 5
            print(f"[EVENT] Волшебник получает +5 маны → {hero.mana}")
            result = func(hero, *args, **kwargs)
            time.sleep(duration)
            hero.mana = old_mp
            print(f"[EVENT] Мана возвращена → {hero.mana}")
            return result
        return wrapper
    return decorator


# даёт 25% шанс удвоить урон атаки
def crit_chance(func):
    @wraps(func)
    def wrapper(hero, damage, *args, **kwargs):
        if random.random() < 0.25:
            damage *= 2
            print("[CRIT] КРИТИЧЕСКИЙ УДАР!")
        return func(hero, damage, *args, **kwargs)
    return wrapper

# Применяем крит к атаке
Hero.attack = crit_chance(Hero.attack)

#демонстрация
if __name__ == "__main__":
    gandalf = Hero("Гэндальф", "волшебник")
    gandalf.add_spell("Огненный шар", 20, 35, 0)
    gandalf.add_spell("Лечение", 15, 0, 30)

    print("=== Обычные действия ===")
    gandalf.attack(20)
    gandalf.heal(10)
    gandalf.cast_spell("Огненный шар")

    print("\n=== Пасхальный ивент (удвоение здоровья) ===")
    @easter_health_boost(2)
    def fight(hero):
        hero.attack(30)
    fight(gandalf)

    print("\n=== Пасхальный ивент (+5 маны волшебнику) ===")
    @easter_mana_boost(2)
    def magic_boost(hero):
        hero.cast_spell("Огненный шар")
    magic_boost(gandalf)

    print("\n=== Проверка смерти ===")
    gandalf.health = 0
    gandalf.attack(10)
    gandalf.cast_spell("Огненный шар")