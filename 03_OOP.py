from abc import ABC, abstractmethod

# ASTRAZIONE: La classe Persona è un modello, non un oggetto reale
class Persona(ABC):
    def __init__(self, nome, cognome, eta):
        # INCAPSULAMENTO: _ indica attributi protetti
        self._nome = nome 
        self._cognome = cognome 
        self._eta = eta
        
    @property
    def eta(self):
        return self._eta
    
    @eta.setter
    def eta(self, valore):
        if valore < 0:
            print(f"--- Errore per {self._nome}: L'età ({valore}) non può essere negativa! ---")
        else:
            self._eta = valore
        
    @abstractmethod
    def presentati(self):
        pass

class Studente(Persona):
    def __init__(self, nome, cognome, eta, matricola, classe):
        super().__init__(nome, cognome, eta)
        # INCAPSULAMENTO: __ indica un attributo privato (nascosto all'esterno)
        self.__matricola = matricola 
        self.classe = classe 
        
    def presentati(self):
        return (f"Ciao, mi chiamo {self._nome} {self._cognome}, ho {self._eta} anni. "
                f"Classe: {self.classe}, Matricola: {self.__matricola}")
    
class Bidello(Persona):
    def __init__(self, nome, cognome, eta, vaccino, piano):
        super().__init__(nome, cognome, eta)
        self.vaccino = vaccino
        self.piano = piano
        
    def presentati(self):
        return (f"Sono {self._nome} {self._cognome}, il bidello. Ho {self._eta} anni, "
                f"vaccino {self.vaccino} e lavoro al piano {self.piano}")

# POLIMORFISMO: Questa funzione accetta qualsiasi oggetto derivato da Persona
def fai_presentare(istanza):
    print(istanza.presentati())

persone = [
    Studente("Mario", "Rossi", 20, 1000076456, "39"),
    Bidello("Luca", "Barbagianni", 45, "Astrazeneca", "secondo")
]   

print("--- PRESENTAZIONI ---")
for p in persone:
    fai_presentare(p)

print("\n--- TEST INCAPSULAMENTO ---")
persone[0].eta = -5 
print(f"Età attuale di {persone[0]._nome}: {persone[0].eta} anni")