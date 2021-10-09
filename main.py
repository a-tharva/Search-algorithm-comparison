"""
Search
Main function for search algorithms graph plotting

"""

import search
import matplotlib.pyplot as plt
import time


def plot_graph(retime, fetime, bitime, jtime):
    
    data = {'linear search':retime, 'interpolation search':fetime, 'binary search':bitime, 'jump search':jtime}

    names = list(data.keys())
    values = list(data.values())

    plt.scatter(names, values)
    plt.suptitle('searching')
    plt.ylabel('Time in milliseconds')
    plt.show()



def main():
    
    
    array = [i for i in range(0,10000000)]

    sear = search.search(array,9999920)

    retime, re = sear.linear()
    fetime, fe = sear.interpolation()
    bitime, bi = sear.binary()
    jtime, ju = sear.jump()
    
  
    print('Search element {} time for execution in linear search {}'.format(re,retime))
    print('Search element {} time for execution in interpolation search {}'.format(fe,fetime))
    print('Search element {} time for execution in binary search {}'.format(bi,bitime))
    print('Search element {} time for execution in jump search {}'.format(ju,jtime))

    plot_graph(retime, fetime, bitime, jtime)
    
main()
#help(search)