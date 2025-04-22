from time import time


def find_el(arr, el):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == el:
            print(f"Операций: {count}")
            return i
    print(f"Операций: {count}")
    return -1


def binary_find_el(arr, el):
    left = 0
    right = len(arr)
    mid_before = 0
    count = 0
    while left < right:
        count += 1
        mid = (right + left) // 2
        if mid == mid_before:
            print(f"Операций: {count}")
            return -1
        if arr[mid] == el:
            print(f"Операций: {count}")
            return mid
        elif arr[mid] > el:
            right = mid
        elif arr[mid] < el:
            left = mid
        mid_before = mid
    print(f"Операций: {count}")
    return -1

arr = [i for i in range(1, 300000001)]
el = 295000000

print("Массив создан!")
binary_start = time()
print(binary_find_el(arr, el))
binary_end = time()

linear_start = time()
print(find_el(arr, el))
linear_end = time()

print(f"Бинарный поиск: {binary_end-binary_start}")
print(f"Линейный поиск: {linear_end - linear_start}")
