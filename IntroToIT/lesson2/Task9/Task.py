#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def is_palindrome(string):
    return string == string[::-1]
string = "радар"
print(f"Является ли '{string}' палиндромом? {is_palindrome(string)}")