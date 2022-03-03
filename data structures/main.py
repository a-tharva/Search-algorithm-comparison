"""
Data structure
Main function for data structure algorithms graph plotting

"""
import time
import matplotlib.pyplot as plt

from random import randint

from list import _list
from stack import _stack
from queue import _queue
from linkedlist import _LinkedList
from hashtable import _HashTable


RANGE = 50000
search_element = randint(2000, RANGE)

def HashFun():
    
    hs = _HashTable()
    print('\n- hash initialized')
    # Insertion
    print('insertion started - ', end='', flush=True)
    insert_time = time.time()
    for _ in range(RANGE):
        hs[f'{_}'] = _
    insert_time = time.time() - insert_time
    print(f'time for insertion : {insert_time}')
    # Search element
    print('search started - ', end='', flush=True)
    search_time = time.time()
    hs[f'{search_element}']
    search_time = time.time() - search_time
    print(f'time for search : {search_time}')
    del(hs)
    return insert_time, search_time
    
    
def ListFun():
    
    ls = _list()
    print('\n- list initialized')
    # Insertion
    print('insertion started - ', end='', flush=True)
    insert_time = time.time()
    for _ in range(RANGE):
        ls.append(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion : {insert_time}')
    # Search element
    print('search started - ', end='', flush=True)
    search_time = time.time()
    for _ in ls:
        if _ == search_element:
            break
    search_time = time.time() - search_time
    print(f'time for search : {search_time}')
    del(ls)
    return insert_time, search_time

    
def LLFun():
    
    ll = _LinkedList()
    print('\n- linkedlist initialized')
    # Insertion
    print('insertion started - ', end='', flush=True)
    insert_time = time.time()
    for _ in range(RANGE):
        ll.insert_at_end(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion : {insert_time}')
    # Search element
#    print('search started - ', end='', flush=True)
#    search_time = time.time()
#    hs[f'{search_element}']
#    search_time = time.time() - search_time
#    print(f'time for search : {search_time}')
    search_time = 0
    del(ll)
    return insert_time, search_time
    
    
def QueueFun():
    
    qu = _queue()
    print('\n- queue initialized')
    # Insertion
    print('insertion started - ', end='', flush=True)
    insert_time = time.time()
    for _ in range(RANGE):
        qu.enqueue(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion : {insert_time}')
    # Search element
    print('search started - ', end='', flush=True)
    search_time = time.time()
    for _ in range(RANGE):
        if qu.dequeue() == search_element:
            break
    search_time = time.time() - search_time
    print(f'time for search : {search_time}')
    del(qu)
    return insert_time, search_time
    
    
def StackFun():
    
    st = _stack()
    print('\n- stack initialized')
    # Insertion
    print('insertion started - ', end='', flush=True)
    insert_time = time.time()
    for _ in range(RANGE):
        st.add(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion : {insert_time}')
    # Search element
    print('search started - ', end='', flush=True)
    search_time = time.time()
    for _ in range(RANGE):
        if st.remove() == search_element:
            break
    search_time = time.time() - search_time
    print(f'time for search : {search_time}')
    del(st)
    return insert_time, search_time
    
    
def TreeFun():
    pass
    
    
def plot_graph(ls, lb):
    
    data = {'hash':ls[0], 'list':ls[1], 'linked list':ls[2], 'queue':ls[3], 'stack':ls[4]}
    names = list(data.keys())
    values = list(data.values())
    
    plt.scatter(names, values, label=lb)
    plt.suptitle(f'Comparison with {RANGE} elements')
    plt.ylabel('Time')
    
    
def run():
    hash_insert_time, hash_search_time = HashFun()
    list_insert_time, list_search_time = ListFun()
    ll_insert_time, ll_search_time = LLFun()
    queue_insert_time, queue_search_time = QueueFun()
    stack_insert_time, stack_search_time = StackFun()
#    tree_insert_time = TreeFun()

    insert_time_ls = [hash_insert_time, list_insert_time, 
                 ll_insert_time, queue_insert_time, stack_insert_time]
    search_time_ls = [hash_search_time, list_search_time,
                 ll_search_time, queue_search_time, stack_search_time]
    return insert_time_ls, search_time_ls


def main():
    print('Comparison started')
    insert_ls, search_ls = run()
    plot_graph(insert_ls, 'Insertion')
    plot_graph(search_ls, f'search {search_element}')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    main()