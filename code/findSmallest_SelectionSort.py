def findSmallest(arr):

    """
    Алгоритм поиска наименьшего путём сравнения с каждым элементом.
    """
    smallest = arr[0]
    smallest_ind = 0

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind


def selectionSort(arr):

    """
    Сортировка выбором. Ищется наименьший элемент и забирается в новый массив. 
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        
    return newArr


print(selectionSort([4,5,1,2,3,5,6,7,8,1,2,3]))