def hälsa(namn):
    return f"Funktion 'Hälsa': Hej {namn}!"

print(hälsa("Erik"))
print(hälsa("Anna"))
print("\n")

def presentera(namn, ålder):
    return f"Funktion 'Presentera': {namn.capitalize()} är {ålder} år."

print(presentera("Erik", 17))
print(presentera("Anna", 18))
print("\n")

def hälsning(namn, hälsning = "Hej"):
    return f"Funktion 'Hälsning': {hälsning}, {namn}!"

print(hälsning("Erik"))
print(hälsning("Anna", "Hallå"))
print("\n")

def dubbla(tal):
    return tal * 2

x = dubbla(5)
print(x)

print("\n")

def cirkel_area(radie):
    return 3.14 * radie * radie

a = cirkel_area(5)
print("Area:", a)
print("\n")