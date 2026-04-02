class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def ToString (self):
        return f"{self.nome} {self.cognome}, Età: {self.eta}"

class Dottore (Persona):
    def __init__(self, nome, cognome, eta, specializzazione, stipedio):
        Persona.__init__(self, nome, cognome, eta)
        self.stipendio = stipedio
        self.specializzazione = specializzazione
        
    def ToString(self):
        return f"{Persona.ToString(self)}, Specializzazione: {self.specializzazione}, Stipendio: {self.stipendio}"
    
class Paziente(Persona):
    def __init__(self, nome, cognome, eta, gruppo_sanguigno, patologie):
        Persona.__init__(self, nome, cognome, eta)
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = patologie
        
    def ToString(self):
        return f"{Persona.ToString(self)}, Gruppo: {self.gruppo_sanguigno}, Patologie: {self.patologie}"
    

p = Persona("Mario", "Di Paola", 20)
print (p.ToString())

d = Dottore("Luca", "Argentero", 40, "Chirurgo Estetico", 5000)
print(d.ToString())

patologie = ["Diarrea", "Vomito", "Pressione alta"]
pa = Paziente ("Giovanni", "Santonocito", 65, "0+" , patologie)
print(pa.ToString())