"""Searching algorithms

This module includes sorting algorithms.
return:
    time required by algorithm and sorted list

class:

    sort

    functions:

        bubble_sort(array)
        insertion_sort(array)
        merge_sort(array)
        quicksort(array)
"""

import time
from random import randint


def timer(func):
    # Decorator for time
    def wrapper(*args, **kwargs):
        before = time.time()
        sort = func(*args,**kwargs)
        time.sleep(2)
        return (time.time()-before-2)*1000, sort
    
    return wrapper


def quicksort(array):
        if len(array) < 2:
            return array

        low, same, high = [], [], []

        pivot = array[randint(0, len(array) - 1)]

        for item in array:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        return quicksort(low) + same + quicksort(high)

    
def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


class sort:
    """sort 
    para:
        array 
    
    methods:
        bubble_sort(array)
        insertion_sort(array)
        merge_sort(array)
        quicksort(array)
    """
    
    
    def __init__(self,array):
        self.array = array
    
    
    @timer
    def bubble_sort(self):
        #Bubble sort
        n = len(self.array)
        
        for i in range(n):
            already_sorted = True
            for j in range(n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]                
                    already_sorted = False
            if already_sorted:
                break
        return self.array
    
    
    @timer
    def insertion_sort(self):
        #Insertion sort
        for i in range(1, len(self.array)):
            key_item = self.array[i]
            j = i - 1
        while j >= 0 and self.array[j] > key_item:
            self.array[j + 1] = self.array[j]
            j = j - 1
        self.array[j + 1] = key_item
        return self.array
    
    
    @timer
    def merge_sort(self):
        #Merge sort
        return merge_sort(self.array)
    
    
    @timer
    def quicksort(self):
        #Qick sort
        return quicksort(self.array)