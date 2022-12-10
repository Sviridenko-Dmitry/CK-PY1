from random import randint


def get_unique_list_numbers(start: int, stop: int, count: int) -> list[int]:
    random_list = []
    while len(random_list) != count:
        num = randint(start, stop)
        if num not in random_list:
            random_list.append(num)
    return random_list


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# Задание выполнено
