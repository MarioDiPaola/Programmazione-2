# -- INIZIALIZZIAMO LA CRONOLOGIA --

history = ["google.com", "wikipedia.org", "python.org"]
forward = []
current = history.pop()

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")

# -- TORNIAMO INDIETRO --
forward.append(current)
current = history.pop()

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward}")

# -- TORNIAMO INDIETRO ANCORA --
forward.append(current)
current = history.pop()

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward}")

# -- ANDIAMO AVANTI --
history.append(current)
current = forward.pop()

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward}")




history.insert(1, "yahoo.com")
print(f"Cronologia: {history}")

print(f"{history[0]}")
print(f"{history[1]}")

history.remove("google.com")
print(f"{history}")

history.pop(0)
print(f"{history}")

