ALTERNATIV_1 = "1. Addera två tal"
ALTERNATIV_2 = "2. Multiplicera två tal"
ALTERNATIV_3 = "3. Avsluta"

#MENY: Visar alternativen
def visa_meny():
    print("\nVänligen välj ett alternativ: ---------------------------------------\n")
    print(ALTERNATIV_1)
    print(ALTERNATIV_2)
    print(ALTERNATIV_3)
    print()


#HÄMTA_MENYVAL: Ger tillbaka ett giltigt heltal
def hämta_menyval():
    while True:
        try:
            användarens_val = int(input("Val: "))
            return användarens_val
        
        except ValueError:
            print("\nDu måste ange en siffra, t.ex. 1, 2 eller 3.\n")

#HÄMTA_TVÅ_TAL: Ger tillbaka två giltiga heltal
def hämta_två_tal():
    while True:
        try:
            tal_1, tal_2 = map(int, input("Ange två tal med mellanslag: ").split())
            return tal_1, tal_2
    
        except ValueError:
            print("\nFelaktig inmatning. Ange exakt två heltal, t.ex. 5 12\n")


#ADDERA: Använder talen och visar additionen
def addera(tal_1, tal_2):
    return tal_1 + tal_2

#MULTIPLICERA: Använder talen och visar multiplikationen
def multiplicera(tal_1, tal_2):
    return tal_1 * tal_2


#HUVUDPROGRAM: Bestämmer vad som ska köras
def huvudprogram():
    while True:
        visa_meny()
        användarens_val = hämta_menyval()

        if användarens_val == 1:
            print(f"\nDu valde: '{ALTERNATIV_1}'")
            tal_1, tal_2 = hämta_två_tal()
            resultat = addera(tal_1, tal_2)
            print(f"Resultat: {resultat}")

        elif användarens_val == 2:
            print(f"\nDu valde: '{ALTERNATIV_2}'")
            tal_1, tal_2 = hämta_två_tal()
            resultat = multiplicera(tal_1, tal_2)
            print(f"Resultat: {resultat}")

        elif användarens_val == 3:
            print(f"\nDu valde: '{ALTERNATIV_3}'")
            print("Programmet avslutas.\n")
            break

        else:
            print(f"\nDu valde: '{användarens_val}'")
            print("Ogiltigt val.")


huvudprogram()


#A-NIVÅ: Checklista:

#Fungerar programmet? 1) Programmet gör det uppgiften ber om, 2) det kraschar inte vid normal användning, 3) resultatet blir korrekt

#Är programmet uppdelat i funktioner? 1) Finns flera funktioner? 2) Har varje funktion ett tydligt ansvar?
#EX: visa_meny(), hämta_menyval(), hämta_två_tal(), addera(), huvudprogram()

#Undvik att upprepa kod!

#Har jag felhantering?

