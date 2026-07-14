#Skriv en funktion som tar emot en lista och returnerar medelvärdet

# def medel_värde(lista):
#     return sum(lista) / len(lista)

# print(medel_värde([3, 5, 7]))


# def chat_medel_värde(lista):

#     if not isinstance(lista, list): #syntax: isinstance(element, type), exempelvis isinstance(tal, int) eller isinstance(text, str)
#         return "Fel: Argumentet måste vara en lista."
    
#     if not lista:
#         return "Fel: Listan är tom."

#     for tal in lista:
#         if not isinstance(tal, (int, float)):
#             return "Fel, listan får endast innehålla tal."
        
#     resultat = sum(lista) / len(lista)
#     return resultat

# print(chat_medel_värde([1, 5]))


#Låt användaren skriva in fem tal, programmet ska sedan skriva ut:
#Största talet
#Minsta talet
#Medelvärdet

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



#while-loop
#anrop till hämta_heltal
#kör funktioner
        

