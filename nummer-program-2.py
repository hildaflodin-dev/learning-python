def hämta_heltal():
    while True:
        try:
            lista = list(map(int, input("Ange fem helal med mellanslag: ").split()))

            if len(lista) != 5:
                print("Du måste ha exakt fem heltal.\n")
                continue

            return lista
        
        except ValueError:
            print("Fel inmatning. Ange endast heltal.\n")

def största(lista):
    return max(lista)

def minsta(lista):
    return min(lista)

def medelvärde(lista):
    return sum(lista) // len(lista)

def huvudprogram():

    print()
    lista = hämta_heltal()

    print(f"\nStörsta talet: {största(lista)}")
    print(f"Minsta talet: {minsta(lista)}")
    print(f"Medelvärdet: {medelvärde(lista)}")
    print()

huvudprogram()