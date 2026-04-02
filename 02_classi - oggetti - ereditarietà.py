class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__ (self):
        return f"{self.nome} {self.cognome} | Età: {self.eta}"

class Paziente(Persona):
    def __init__(self, nome, cognome, eta, identificatico, gruppo_sanguigno):
        super().__init__(nome, cognome, eta)
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = []
        self.allergie = []
        self.identificativo = identificatico
        
    def __str__(self):
        pat_str = ", ".join(self.patologie)
        all_str = ", ".join(self.allergie)
        
        return (f"ID: {self.identificativo} | {super().__str__()} | Gruppo: {self.gruppo_sanguigno} | Patologie: {pat_str} | Allergie: {all_str}")
    
class Dottore (Persona):
    def __init__(self, nome, cognome, eta, specializzazione, matricola, reparto):
        super().__init__(nome, cognome, eta)
        self.matricola = matricola
        self.specializzazione = specializzazione
        self.reparto = reparto
        self.pazienti_in_cura = []
    
    def __str__(self):
        return f"Dott. {self.cognome} {self.nome} (Specializzazione: {self.specializzazione}) - Matricola: {self.matricola}"

doc = Dottore("Francesco", "Sapienza", 45, "Cardiologia", "MED123", "Terapia Intensiva")

pz1 = Paziente("Giovanni", "Rossi", 46, "100076406", "0-")
pz1.patologie = ["Aritmia", "Ipertensione"]
pz1.allergie = ["Polline"]

pz2 = Paziente("Luigi", "Bianchi", 38, "1000056734", "AB")
pz2.patologie = ["Bassa Pressione"]
pz2.allergie = ["Polvere"]

doc.pazienti_in_cura.extend([pz1, pz2])

print("="*50)
print("INFORMAZIONI DOTTORE")
print("="*50)
print(doc) 

print("\n" + "="*50)
print(f"PAZIENTI IN CURA NEL REPARTO: {doc.reparto.upper()}")
print("="*50)

for p in doc.pazienti_in_cura:
    print(p) 