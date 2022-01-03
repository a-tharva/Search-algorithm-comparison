"""
Search
Main function for search algorithms graph plotting

"""

import search
import matplotlib.pyplot as plt


def plot_graph(retime, fetime, bitime, jutime, search_element):
    
    data = {'linear search':retime, 'interpolation search':fetime, 'binary search':bitime, 'jump search':jutime}

    names = list(data.keys())
    values = list(data.values())

    plt.scatter(names, values, label = search_element)
    plt.suptitle('searching algorithms')
    plt.ylabel('Time in milliseconds')



def main():
    
    
    array = [i for i in range(0,10000000)]
    
    search_element = 9999920
    search1 = search.search(array, search_element)

    linearTime, linear = search1.linear()
    interpolationTime, interpolation = search1.interpolation()
    binaryTime, binary = search1.binary()
    jumpTime, jump = search1.jump()

    del search1
    
    print('Search element {} time for execution in linear search {}'.format(linear,linearTime))
    print('Search element {} time for execution in interpolation search {}'.format(interpolation,interpolationTime))
    print('Search element {} time for execution in binary search {}'.format(binary,binaryTime))
    print('Search element {} time for execution in jump search {}'.format(jump,jumpTime))

    plot_graph(linearTime, interpolationTime, binaryTime, jumpTime, search_element)
    
    
    # Second array 
    
    array = [i for i in range(0,10000)]
    
    search_element = 825
    search2 = search.search(array, search_element)

    linearTime, linear = search2.linear()
    interpolationTime, interpolation = search2.interpolation()
    binaryTime, binary = search2.binary()
    jumpTime, jump = search2.jump()
    
    del search2
    
    print('\nSearch element {} time for execution in linear search {}'.format(linear,linearTime))
    print('Search element {} time for execution in interpolation search {}'.format(interpolation,interpolationTime))
    print('Search element {} time for execution in binary search {}'.format(binary,binaryTime))
    print('Search element {} time for execution in jump search {}'.format(jump,jumpTime))

    plot_graph(linearTime, interpolationTime, binaryTime, jumpTime, search_element)
    
    
    plt.legend(loc='upper right')
    plt.show()

    
main()
#help(search)