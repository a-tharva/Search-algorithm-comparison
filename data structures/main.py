"""
Data structure
Main function for data structure algorithms graph plotting

"""
import time
import matplotlib.pyplot as plt

from list import _list
from stack import _stack
from queue import _queue
from linkedlist import _LinkedList
from hashtable import _HashTable


RANGE = 1000

def HashFun():
    
    hs = _HashTable()
    print('\n- hash initialized')
    print('insertion started-')
    insert_time = time.time()
    for _ in range(RANGE):
        hs[f'{_}'] = _
    insert_time = time.time() - insert_time
    print(f'time for insertion - {insert_time}')
    print(hs['52'])
    print(hs['5'])
    print(hs['10'])
    print(hs['22'])
#    print(hs.arr)
    return insert_time
    
    
def ListFun():
    
    ls = _list()
    print('\n- list initialized')
    print('insertion started-')
    insert_time = time.time()
    for _ in range(RANGE):
        ls.append(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion - {insert_time}')
    print(len(ls))
    print(ls[1])
    return insert_time

    
def LLFun():
    
    ll = _LinkedList()
    print('\n- linkedlist initialized')
    print('insertion started-')
    insert_time = time.time()
    for _ in range(RANGE):
        ll.insert_at_end(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion - {insert_time}')
    return insert_time
    
    
def QueueFun():
    
    qu = _queue()
    print('\n- queue initialized')
    print('insertion started-')
    insert_time = time.time()
    for _ in range(RANGE):
        qu.enqueue(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion - {insert_time}')
    print(qu.size())
    print(qu.dequeue())
    return insert_time
    
    
def StackFun():
    
    st = _stack()
    print('\n- stack initialized')
    print('insertion started-')
    insert_time = time.time()
    for _ in range(RANGE):
        st.add(_)
    insert_time = time.time() - insert_time
    print(f'time for insertion - {insert_time}')
    print(len(st))
    print(st.peek())
    return insert_time
    
    
def TreeFun():
    pass
    
    
def plot_graph(ls, name):
    
    data = {'hash':ls[0], 'list':ls[1], 'linked list':ls[2], 'queue':ls[3], 'stack':ls[4]}
    names = list(data.keys())
    values = list(data.values())
    
    plt.scatter(names, values)
    plt.suptitle(f'{name}')
    plt.ylabel('Time')
    plt.show()
    
    
def run():
    hash_insert_time = HashFun()
    list_insert_time = ListFun()
    ll_insert_time = LLFun()
    queue_insert_time = QueueFun()
    stack_insert_time = StackFun()
#    TreeFun()
    return hash_insert_time, list_insert_time, ll_insert_time, queue_insert_time, stack_insert_time


def main():
    print('Comparison started')
    ls = run()
    plot_graph(ls, 'inserting value')
    

if __name__ == '__main__':
    main()