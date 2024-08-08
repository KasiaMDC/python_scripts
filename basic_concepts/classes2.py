# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:57:05 2024

@author: Felipe
"""

class QueueError(IndexError):  # Choose base class for the new exception.
        pass


class Queue:
    def __init__(self):
        self.__queque = []
        
        
        
    def put(self, elem):
        self.__queque.insert(0,elem)
        

    def get(self):
       try: 
           val = self.__queque[-1]
           del self.__queque[-1]
           return val
       except IndexError:
           print("Queque Error")
           raise QueueError
           

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

print(que._Queue__queque)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
