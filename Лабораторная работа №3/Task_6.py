list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_last_index = 0
max_last_value = list_numbers[max_last_index]
for i, current_value in enumerate(list_numbers):
    max_last_value = list_numbers[max_last_index]
    if current_value >= max_last_value:
        max_last_index = i
        max_last_value = list_numbers[max_last_index]

list_numbers[len(list_numbers) - 1], list_numbers[max_last_index] = \
    max_last_value, list_numbers[-1]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
