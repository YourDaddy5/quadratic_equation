from math import sqrt


def quadratic_equation(a,b,c):

    global D

    D = b*b - 4*a*c

    print(D)

    if D > 0:

        print('Уравнение имеет 2 корня.')

        x1 = (-b + sqrt(D)) / (2 * a)

        print('Первый корень равен',x1)

        x2 = (-b - sqrt(D)) / (2*a)

        print('Второй корень равен',x2)

    if D == 0:
        print("Уравнение имеет 1 корень.")
        x = (-b + sqrt(D)) / (2*a)
        print("Корень- " , x)

    if D <0:
        print("Уравнение не имеет корней.")

    return ""


print(quadratic_equation(2,5,3))