#INTRO TO IT 2nd COURSE
# Задача: создать словарь, где ключи - числа от 1 до N, а значения - квадраты этих чисел
def squares_dict(n):
    return {i: i ** 2 for i in range(1, n + 1)}

print(squares_dict(5))  # Должно вывести {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
