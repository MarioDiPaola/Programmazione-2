# inizializziamo la coda
queue = ["luca", "sara", "mario"]

# enqueue — aggiungiamo in fondo
queue.append("anna")
print(queue)   # ['luca', 'sara', 'mario', 'anna']

# dequeue — rimuoviamo dalla testa
primo = queue.pop(0)
print(primo)   # 'luca' — il primo entrato è il primo ad uscire
print(queue)   # ['sara', 'mario', 'anna']

print ("----------------------------")

from collections import deque

queue = deque(["luca", "sara", "mario"])

queue.append("anna")       # enqueue — O(1)
primo = queue.popleft()    # dequeue — O(1)
print(primo)               # 'luca'


from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()         # deque privato — O(1) per enqueue e dequeue

    def enqueue(self, item):
        self.__data.append(item)      # aggiunge in fondo

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()  # rimuove dalla testa — O(1)

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty queue")
        return self.__data[0]         # guarda la testa senza rimuoverla

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Queue({list(self.__data)})"
