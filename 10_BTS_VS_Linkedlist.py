import time 
import random

class ListaNodo:
    def __init__(self, valore):
        self.valore = valore
        self.next = None

class LinkedList:
    def __init__(self):
        self.testa = None
        self.size = 0

    def Insert(self, valore):
        nuovo = ListaNodo(valore)
        nuovo.next = self.testa
        self.testa = nuovo 
        self.size += 1

    def Cerca(self, target):
        corrente = self.testa
        while corrente:
            if corrente.valore == target:
                return True
            corrente = corrente.next
        return False
    
class NodoBST:
    def __init__(self, valore):
        self.valore = valore 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.radice = None

    def Insert(self, valore):
        if not self.radice:
            self.radice = NodoBST(valore)
        else:
            self._insert_recursive(self.radice, valore)

    def _insert_recursive(self, nodo, valore):
        if valore < nodo.valore:
            if nodo.left: self._insert_recursive(nodo.left, valore)
            else: nodo.left = NodoBST(valore)
        else:
            if nodo.right: self._insert_recursive(nodo.right, valore)
            else: nodo.right = NodoBST(valore)

    def Cerca(self, target):
        return self.cerca_ricorsivo(self.radice, target)
    
    def cerca_ricorsivo(self, nodo, target):
        if not nodo: return False 
        if nodo.valore == target: return True
        if target < nodo.valore: return self.cerca_ricorsivo(nodo.left, target)
        return self.cerca_ricorsivo(nodo.right, target)
    

numeri_randomici = [random.randint(1,10000) for _ in range(1000)]

ll = LinkedList()
bst = BST()
for n in numeri_randomici:
    ll.Insert(n)
    bst.Insert(n)

target = numeri_randomici[499]

inizia_ll = time.perf_counter()
ll.Cerca(target)
fine_ll = time.perf_counter()
durata_ll =fine_ll - inizia_ll

inizia_bst = time.perf_counter()
bst.Cerca(target)
fine_bst = time.perf_counter()
durata_bst = fine_bst - inizia_bst

print(f"Tempo LinkedList: {durata_ll:.8f} secondi")
print(f"Tempo BST       : {durata_bst:.8f} secondi")

if durata_bst > 0:
    ratio = durata_ll/durata_bst
print(f"\nIl BST è stato circa {ratio:.2f} volte più veloce della LinkedList.")