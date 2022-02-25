"""
Data structure
Main function for data structure algorithms graph plotting

"""

from list import _list
from stack import _stack
from linkedlist import _LinkedList
from hashtable import _HashTable
from queue import _queue


def ListFun():
    
    ls = _list()
    print('list')
    ls.append(20)
    ls.append(30)
    ls.append(50)
    print(len(ls))
    print(ls[1])

def LLFun():
    pass
    
def StackFun():
    
    st = _stack()
    print('stack')
    st.add(20)
    st.add(30)
    st.add(80)
    print(len(st))
    print(st.peek())

    
def HashFun():
    
    hs = _HashTable()
    print('hash')
    hs['hash'] = 20
    hs['table'] = 30
    hs['fun'] = 80
    print(hs['fun'])
    
    
def QueueFun():
    
    qu = _queue()
    print('queue')
    qu.enqueue(20)
    qu.enqueue(30)
    qu.enqueue(10)
    print(qu.size())
    print(qu.dequeue())
    
def main():
    
    ListFun()
#    LLFun()
    StackFun()
    HashFun()
    QueueFun()

if __name__ == '__main__':
    main()