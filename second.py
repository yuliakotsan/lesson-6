
def recursion(number):
    if number > 0:
        x = number - 1
        print(x)
        recursion(x)
    else:
        return


def use_recursion():
    number = int(input('Введіть ціле натуральне число: '))
    recursion(number)


use_recursion()
