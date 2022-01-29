"""Searching algorithms

class:

    search

functions:

    linear_search(array, search_element)
    jump_search(array, array_length, search_element)
    binary_search(array, left, right, search_element)
    interpolation_search(array, lower_limit, higher_limit, search_element)
"""

import math
import time


def timer(func):
    # Decorator for time
    def wrapper(*args, **kwargs):
        before = time.time()
        search = func(*args,**kwargs)
        time.sleep(2)
        return (time.time()-before-2)*1000, search
    
    return wrapper


def linear_search(arr, search_element):
    """linear search
    
        keywords:
            arr -- array for searching
            search element -- search element
        
        return:
            selarch element result(index)
        """
    
    search_at = 0
    search_result = False
    
    while search_at < len(arr) and search_result is False:
        if arr[search_at] == search_element:
            search_result = True
            return search_at
        else:
            search_at = search_at + 1
    return False
    

def jump_search(arr, n, x):
    """jump search
    
        keywords:
            arr -- array for searching
            n -- length of array
            x -- search element
            
        return:
            selarch element result(index)
        """
    
    step = math.sqrt(n)
    
    prev = 0
    while arr[int(min(step, n)-1)]<x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return False
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return False
    if arr[int(prev)] == x:
        return int(prev)
    
    return False


def binary_search(arr, l, r, x):
    """Binary search
    
        keywords:
            arr -- array for searching
            l -- left
            r -- right
            x -- search element
            
        return:
            selarch element result(index)
        """
    
    if r >= l:
        
        mid = l + (r-l) // 2
        
        if arr[mid] == x:
            return mid
        elif arr [mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid+1, r, x)
    else:
        #element not present in array
        return False


def interpolation_search(arr, low, hi, x):
    """interpolation search
    
        keywords:
            arr -- array for searching
            low -- lower limit
            hi -- higher limit
            x -- search element
        
        return:
            selarch element result(index)
        """
    
    if(low <= hi and x >= arr[low] and x<= arr[hi]):
        pos = low+((hi-low)//(arr[hi] - arr[low])*(x-arr[low]))
        
        if arr[pos] == x:
            return pos;
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)
        if arr[pos] > x:
            return interpolation_search(arr, low, pos-1, x)
    
    return False



class search:
    """search 
    para:
        array 
        search element
    
    methods:
        linear(array, element)
        jump(array, element)
        binary(array, element)
        interpolation(array, element)
    """
    
    def __init__(self,arr,ele):
        self.arr = arr
        self.ele = ele
        
        
    @timer
    def linear(self):
        return linear_search(self.arr, self.ele)
        
        
    @timer
    def jump(self):
        length = len(self.arr)
        return jump_search(self.arr, length, self.ele)
        
        
    @timer
    def binary(self):
        length = len(self.arr)
        return binary_search(self.arr, 0, length-1, self.ele)
        
        
    @timer
    def interpolation(self):
        length = len(self.arr)
        return interpolation_search(self.arr, 0, length-1, self.ele)