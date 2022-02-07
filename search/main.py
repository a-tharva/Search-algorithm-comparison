"""
Search
Main function for search algorithms graph plotting

"""

import search
from random import randint
import matplotlib.pyplot as plt


ARRAY_LENGTH = 10000000 # Array size from 0 to length
                        # Array of this size will take a lot of memory 


def plot_graph(retime, fetime, bitime, jutime, search_element):
    
    data = {'linear search':retime, 'interpolation search':fetime, 'binary search':bitime, 'jump search':jutime}

    names = list(data.keys())
    values = list(data.values())

    plt.scatter(names, values, label = search_element)
    plt.suptitle('searching algorithms')
    plt.ylabel('Time in milliseconds')


def main():
    
    array = [i for i in range(0, ARRAY_LENGTH)]
    print('-array created')
    itr = 4 # Number of times loop will go
    search_element = 0
    search_obj = search.search(array, search_element)
    print('Starting loop')
    
    while itr>0:
        
        search_obj.ele = randint(0, ARRAY_LENGTH)
        print(f'\n-Search element for this iteration is {search_obj.ele}')
        
        linearTime, linear = search_obj.linear()
        print('Search element {} time for execution in linear search {}'.format(linear,linearTime))
        interpolationTime, interpolation = search_obj.interpolation()
        print('Search element {} time for execution in interpolation search {}'.format(interpolation,interpolationTime))
        binaryTime, binary = search_obj.binary()
        print('Search element {} time for execution in binary search {}'.format(binary,binaryTime))
        jumpTime, jump = search_obj.jump()
        print('Search element {} time for execution in jump search {}'.format(jump,jumpTime))

        
        plot_graph(linearTime, interpolationTime, binaryTime, jumpTime, search_obj.ele)
        
        itr -= 1
    
    plt.legend(loc='upper right')
    plt.show()

    
main()
#help(search)