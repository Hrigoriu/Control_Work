"""
Напиши функцію, для сортування рядка слів,
розділених пропусками за довжиною слів в порядку зменшення.
Вхідні дані: Ruby Python Go JavaScript Java
Очікуваний результат: JavaScript Python Java Ruby Go
"""
def sort_word(string):
    words = string.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)

input_words = "Ruby Python Go JavaScript Java"
result = sort_word(input_words)
print(result)

