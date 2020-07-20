# Sorting Algorithms


# 1. Bubble Sort
def bubble_sort(array):
    swapped = False
    sort = array
    i = 0
    while i < len(array) - 1:
        if int(array[i]) > int(array[i + 1]):
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
            swapped = True
        if swapped is True and i == len(array) - 2:
            i = 0
            swapped = False
        else:
            i += 1
    return sort


# 2. Insertion Sort
def insertion_sort(array):
    sort = array
    j = 0
    while j < len(sort) - 1:
        i = j
        while sort[i + 1] < sort[i]:
            temp = sort[i]
            sort[i] = sort[i + 1]
            sort[i + 1] = temp
            if i == 0:
                break
            else:
                i -= 1
        j += 1
    return sort


# 3. Selection Sort
def selection_sort(array):
    sort = array
    for i in range(len(sort) - 1):
        low = i
        for j in range(len(sort)):
            if j > low:
                if sort[j] < sort[low]:
                    low = j
        if low != i:
            temp = sort[low]
            sort[low] = sort[i]
            sort[i] = temp
    return sort


# 4. Merge Sort
def merge_sort(array):
    if len(array) == 1:
        return array

    a = array[:int(len(array)/2)]
    b = array[int(len(array)/2):]

    a = merge_sort(a)
    b = merge_sort(b)

    return merge(a, b)


def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b = b[1:]
        else:
            c.append(a[0])
            a = a[1:]
    c += a[:]
    c += b[:]
    return c


# 5. Shell Sort
def shell_sort(array):
    n = int(len(array))
    interval = int(n / 2)

    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                array[j] = temp
        interval = int(interval / 2)

    return array


# 6. Quick Sort
def quick_sort(array, start, end):
    if end - start > 1:
        p = partition(array, start, end)
        quick_sort(array, start, p)
        quick_sort(array, p + 1, end)
    return array


def partition(array, start, end):
    pivot = array[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and array[i] <= pivot:
            i = i + 1
        while i <= j and array[j] >= pivot:
            j = j - 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            continue
        else:
            array[start], array[j] = array[j], array[start]
            break

    return j
