
#import the modules
import math
import random

def binary_search(arr, target):

    arr.sort()

    left = 0
    right = len(arr)

    while left <= right:
        mid = math.floor((left + right) / 2)

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return arr.index(target)


print(binary_search([1, 2, 3, 4, 5], 3)) # 2
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)) # 6
print(binary_search([3, 2, 5, 9, 1, 6, 10], 10)) # 6
    
