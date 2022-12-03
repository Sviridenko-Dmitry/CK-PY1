def delete(list_, index=None):
    if index is not None:
        new_list = list_[:index] + list_[index + 1:]
    else:
        new_list = list_[:-1]

    return new_list


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# Задание выполнено
