#Skriv en funktion som tar emot en lista och returnerar medelvärdet

def medel_värde(lista):
    return sum(lista) / len(lista)

print(medel_värde([3, 5, 7]))


def chat_medel_värde(lista):

    if not isinstance(lista, list): #syntax: isinstance(element, type), exempelvis isinstance(tal, int) eller isinstance(text, str)
        return "Fel: Argumentet måste vara en lista."
    
    if not lista:
        return "Fel: Listan är tom."

    for tal in lista:
        if not isinstance(tal, (int, float)):
            return "Fel, listan får endast innehålla tal."
        
    resultat = sum(lista) / len(lista)
    return resultat

print(chat_medel_värde([1, 5]))

