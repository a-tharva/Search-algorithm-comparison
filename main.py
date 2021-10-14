"""
Search
Main function for search algorithms graph plotting

"""

import search
import matplotlib.pyplot as plt
import time


def plot_graph(retime, fetime, bitime, jtime, search_element):
    
    data = {'linear search':retime, 'interpolation search':fetime, 'binary search':bitime, 'jump search':jtime}

    names = list(data.keys())
    values = list(data.values())

    plt.scatter(names, values, label = search_element)
    plt.suptitle('searching algorithms')
    plt.ylabel('Time in milliseconds')



def main():
    
    
    array = [i for i in range(0,10000000)]
    
    search_element = 9999920
    search1 = search.search(array, search_element)

    retime, re = search1.linear()
    fetime, fe = search1.interpolation()
    bitime, bi = search1.binary()
    jtime, ju = search1.jump()

    del search1
    
    print('Search element {} time for execution in linear search {}'.format(re,retime))
    print('Search element {} time for execution in interpolation search {}'.format(fe,fetime))
    print('Search element {} time for execution in binary search {}'.format(bi,bitime))
    print('Search element {} time for execution in jump search {}'.format(ju,jtime))

    plot_graph(retime, fetime, bitime, jtime, search_element)
    
    
    # Second array 
    
    array = [i for i in range(0,10000)]
    
    search_element = 825
    search2 = search.search(array, search_element)

    retime, re = search2.linear()
    fetime, fe = search2.interpolation()
    bitime, bi = search2.binary()
    jtime, ju = search2.jump()
    
    del search2
    
    print('\nSearch element {} time for execution in linear search {}'.format(re,retime))
    print('Search element {} time for execution in interpolation search {}'.format(fe,fetime))
    print('Search element {} time for execution in binary search {}'.format(bi,bitime))
    print('Search element {} time for execution in jump search {}'.format(ju,jtime))

    plot_graph(retime, fetime, bitime, jtime, search_element)
    
    
    plt.legend(loc='upper right')
    plt.show()

    
main()
#help(search)