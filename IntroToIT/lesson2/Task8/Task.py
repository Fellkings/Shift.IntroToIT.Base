#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def word_count(string):
    return len(string.split())
string = "Python прекрасен!"
print(f"В '{string}' {word_count(string)} слов")