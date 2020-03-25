# Сумма массива через рекурсию. 4.1


def sumRec(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sumRec(arr[1:])


print(sumRec([]))
print(sumRec([1, 2, 3, 4, 5, 6]))


# 4.2 Кол-во элементов в рекурсии


def counter(arr):
    # Базовый случай. Если массив пустой, то кол-во = 0
    count = 0
    if arr == []:
        return count
    else:
        count += 1
        return count + counter(arr[1:])


print(counter([]))
print(counter([1, 2, 3, 4, 5]))


# 4.3 Наибольшее число в списке


def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max_num([1, 2]))
print(max_num([3, 4, 5, 6, 1, 2, 3, 4, 11, 2, 3, 4]))


# Quick sort


def quiksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quiksort(less) + [pivot] + quiksort(greater)


print(quiksort([10, 5, 2, 3]))
