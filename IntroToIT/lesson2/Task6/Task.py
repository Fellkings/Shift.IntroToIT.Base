#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def counting_vowels(string):
    return sum(1 for symbol in string if symbol.lower() in "аеёиоуыэюя")
string = "Привет, мир!"
print(f"В '{string}' {counting_vowels(string)} гласных")
