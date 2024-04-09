#INTRO TO IT 2nd COURSE
s = input("Введите строку: ")
reversed_s = s[::-1]
if s == reversed_s:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")