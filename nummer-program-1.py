def hämta_heltal():
    while True:
        try:
            a, b, c, d, e = map(int, input("Ange fem heltal med mellanslag: ").split())
            return [a, b, c, d, e]
        
        except ValueError:
            return "Fel inmatning. Du måste ange exakt fem heltal med mellanslag, t.ex. 1 2 3 4 5"
        
def störst(lista):
    return max(lista)

def minsta(lista):
    return min(lista)

def medel(lista):
    return sum(lista) // len(lista)

def huvudprogram():

    print()
    lista = hämta_heltal()

    print(f"Största talet: {störst(lista)}")
    print(f"Minsta talet: {minsta(lista)}")
    print(f"Medelvärdet: {medel(lista)}")
    print()

huvudprogram()
