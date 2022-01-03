"""
Main
This module plot graph for time required for different sorting algorithms
"""

import sort
import random
import matplotlib.pyplot as plt


# array is created with for from 0 to ARRAY_LENGTH
# array then is shuffeled with random.shuffel to make unsorted
ARRAY_LENGTH = 1000
array = [i for i in range(ARRAY_LENGTH)]
print('-array created')
random.shuffle(array)
print('-array shuffled')

# function for plotting scatter graph
def plot_graph(lst):    
    data = {'bubble sort':lst[0], 'insertion sort':lst[1], 'merge sort':lst[2], 'quick sort':lst[3]}

    names = list(data.keys())
    values = list(data.values())

    plt.scatter(names, values)
    plt.suptitle('sorting algorithms')
    plt.ylabel('Time in milliseconds')
    plt.show()
    
# function for sorting
def sort_time():
    s = sort.sort(array)
    
    # Sorting
    bubble_time, bubble_array = s.bubble_sort()
    print(f'bubble sort time: {bubble_time}')
    
    insertion_time, insertion_array = s.insertion_sort()
    print(f'insertion sort time: {insertion_time}')
    
    merge_time, merge_array = s.merge_sort()
    print(f'merge sort time: {merge_time}')
    
    quick_time, quick_array = s.quicksort()
    print(f'quick sort time: {quick_time}')
    
    return bubble_time, insertion_time, merge_time, quick_time

# Main function
def main():
    lst = sort_time()
    plot_graph(lst)
    

if __name__ == '__main__':
    main()