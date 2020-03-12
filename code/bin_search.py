def binary_search(list, item):
    """
    На входе список и что надо найти
    Возвращает индекс элемента.
    Список должен быть отсортирован
    """
    low = 0
    high = len(list) - 1

    while low <= high:

        mid  = int((low + high) / 2)

        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1,3,5,7,9,19,25]

print (binary_search(my_list, 3))