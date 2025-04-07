"""
Напишіть рекурсивну функцію для обчислення суми списку цілих чисел
Вхідні дані:
1 4 7 90 45 23 16
Вихідні дані: 186
"""
def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + recursive_sum(numbers[1:])

input_list = [1, 4, 7, 90, 45, 23, 16]
result = recursive_sum(input_list)
print(result)
