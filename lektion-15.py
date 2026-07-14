# poäng = int(input("Hur många poäng har du? "))

# if poäng >= 90:
#     print("Utmärkt!")
# elif poäng >= 50:
#     print("Godkänt.")
# else:
    # print("Icke godkänt.")


def hämta_poäng(poäng):
    while True:
        try:
            return int(input(poäng)) #Glöm inte att skriva return!
        except ValueError:
            print("Felaktig inmatning!")

def hämta_meddelande():
    poäng = hämta_poäng("\nHur många poäng har du? ")
    
    if poäng >= 90:
        return "Utmärkt!\n"
    elif poäng >= 70:
        return "Bra jobbat!\n"
    elif poäng >= 50:
        return "Godkänt.\n"
    else:
        return "Icke godkänt.\n"
    
# hämta_meddelande()
print(hämta_meddelande()) #Glöm inte att lägga till print! Eftersom det är print som skriver ut returvärdet från funktionen.