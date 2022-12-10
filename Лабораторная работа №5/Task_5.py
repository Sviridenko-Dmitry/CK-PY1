from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n) -> str:
    symbols = ascii_uppercase + ascii_lowercase + digits
    password = "".join(sample(symbols, n))
    return password


print(get_random_password(8))
# Задание выполнено
