#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    second_max = max(lst)
    return first_max + second_max

# Правильное решение:
def wrong_sum_of_two_largest(lst):
    sorted_list = sorted(lst)
    first_max = sorted_list[-1]
    second_max = sorted_list[-2]
    return first_max + second_max

lst = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10]
result = wrong_sum_of_two_largest(lst)
print(result)  # Выведет: 15

sorted_list = sorted(lst)
print(sorted_list[-1])
    