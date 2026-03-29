#Задание 1
class Facade:
    pass

#Задание 2
facade_1 = Facade()

#Задание 3
facade_1_type = type(facade_1)
print(facade_1_type)

#Задание 4
class Grade:
    minimum_passing = 65

#Задание 5
class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."

#Задание 6
class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2


circle_for_area = Circle()
print(circle_for_area.area(5))

#Задание 7
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print(f"New circle with diameter: {diameter}")

    def area(self, radius):
        return self.pi * radius ** 2


teaching_table = Circle(36)


#Задание 8
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Задание 8:")
print("medium_pizza circumference =", medium_pizza.circumference())
print("teaching_table circumference =", teaching_table.circumference())
print("round_room circumference =", round_room.circumference())


#Задание 9
print("Задание 9: dir(5)")
print(dir(5))


def this_function_is_an_object(*args, **kwargs):
    return {
        "args": args,
        "kwargs": kwargs,
    }


print("Задание 9: dir(this_function_is_an_object)")
print(dir(this_function_is_an_object))

#Задание 10
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Задание 10:")
print(medium_pizza)
print(teaching_table)
print(round_room)