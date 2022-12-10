from pprint import pprint

dict_list = [
    {function: number for function, number in [('bin', bin(num)), ('dec', num), ('hex', hex(num)), ('oct', oct(num))]}
    for num in range(16)]
pprint(dict_list)
# Задание выполнено
