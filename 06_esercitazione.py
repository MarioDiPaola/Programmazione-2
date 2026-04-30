class Notifiche:
    def __init__(self):
        self.messaggi = []

    def arriva(self, messaggio):
        self.messaggi.append(messaggio)
    
    def leggi (self):
        if not len(self.messaggi)==0:
            return self.messaggi.pop()
        return IndexError("Nessuna notifica")
    
    def prossima(self):
        if not len(self.messaggi)==0:
            return self.messaggi[-1]
        return IndexError("Lista vuota")
    
    def __repr__(self):
        return f"Notifiche({self.messaggi})"
    
history = Notifiche()

history.arriva("WhatsApp: Ciao!")
history.arriva("Gmail: Hai un nuovo messaggio")
history.arriva("Instagram: Ti hanno taggato")

current = history.prossima()

print(f"Ultima notifica: {current}")

current = history.leggi()
print(f"Notifica corrente: {current}")     

current = history.leggi()
print(f"Notifica corrente: {current}")    

current = history.leggi()
print(f"Notifica corrente: {current}")   

current = history.leggi()
print(f"Notifica corrente: {current}")   