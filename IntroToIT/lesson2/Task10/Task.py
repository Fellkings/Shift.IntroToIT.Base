#INTRO TO IT 2nd COURSE
# Задача 10: Квадраты на улице!
# Создай список, содержащий квадраты чисел от 0 до введенного числа.
def generate_squares(number):
    return [x**2 for x in range(number)]
number = 5
print(f"{number} первых квадратов: {generate_squares(number)}")