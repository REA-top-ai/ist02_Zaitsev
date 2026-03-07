#Задание 1
#1
def fct(n):
    x = 1
    for n in range(1,n+1):
        x= x*n
    return x
print(fct(5))
#2
def recfct(n):
    if n == 1:
        return 1
    return n * recfct(n-1)
print(recfct(6))
#Задание 2
def sq(n):
    return [x ** 2 for x in n]

n = [1, 2, 3, 4, 5]
print(n)
print(sq(n))