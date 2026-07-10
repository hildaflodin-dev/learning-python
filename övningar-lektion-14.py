# #VAD ÄR EN FUNKTION

# def hälsa(namn):
#     return f"Funktion 'Hälsa': Hej {namn}!"

# print(hälsa("Erik"))
# print(hälsa("Anna"))
# print("\n")

# def presentera(namn, ålder):
#     return f"Funktion 'Presentera': {namn.capitalize()} är {ålder} år."

# #PARAMETRAR OCH ARGUMENT

# print(presentera("Erik", 17))
# print(presentera("Anna", 18))
# print("\n")

# def hälsning(namn, hälsning = "Hej"):
#     return f"Funktion 'Hälsning': {hälsning}, {namn}!"

# print(hälsning("Erik"))
# print(hälsning("Anna", "Hallå"))
# print("\n")

# #RETURN

# def dubbla(tal):
#     return tal * 2

# x = dubbla(5)
# print(x)

# print("\n")

# def cirkel_area(radie):
#     return 3.14 * radie * radie

# a = cirkel_area(5)
# print("Area:", a)
# print("\n")

# def betyg(poäng):
#     if poäng >= 90: return "A"
#     elif poäng >= 70: return "C"
#     elif poäng >= 50: return "E"
#     else: return "F"

# print(betyg(98), end="\n\n")

# #PRINT vs RETURN
# # Print visar text på skärmen | Return skickar tillbaka ett värde
# # Print kan inte sparas (ger None) | Return kan sparas i en variabel
# # Print används för att visa information | Return används för att avsluta en funktion och eventuellt returnera ett värde

# def plus_print(a, b):
#     print("plus_print printar", a + b) #Visar summa, men returnerar inget

# def plus_return(a, b):
#     return a + b #Ger tillbaka summa, måste printas själv till konsollen

# x = plus_print(3, 4)
# print(x, end="\n\n")

# y = plus_return(3, 4)
# print(y)
# print(y * 2, end="\n\n")


# #FUNKTIONER + FOR-LOOP

# def summa_lista(lista):
#     total = 0
#     for tal in lista:
#         total += tal
#     return total

# print(summa_lista([10, 20, 30]))

# def räkna_jämna(lista):
#     antal = 0
#     for tal in lista:
#         if tal % 2 == 0:
#             antal += 1
#     return antal

# print(räkna_jämna([1, 2, 3, 4, 5, 6]))

# def hitta_max(lista):
#     störst = lista[0]
#     for tal in lista:
#         if tal > störst:
#             störst = tal
#     return störst

# print(hitta_max([4, 9, 2, 7]), end="\n\n")

# def skriv_tabell(tal):
#     for i in range(1, 11):
#         print(f"{tal} * {i} = {tal * i}")

# skriv_tabell(5)

#FUNKTIONER + WHILE-LOOP

# def fråga_tills_rätt(rätt):
#     while True:
#         svar = input("Gissa: ")
#         if svar == rätt:
#             print("Rätt!")
#             return True #Betyder "avsluta funktionen nu och skicka tillbaka värdet True", return stoppar alltid funktionen oavsett vad du returnerar!
#         print("Fel!")

# resultat = fråga_tills_rätt("ok")
# if resultat:
#     print("\nSpelet är klart!\n")

# def hämta_positivt():
#     while True:
#         tal = int(input("Positivt tal: "))
#         if tal > 0:
#             return tal
#         print("Måste vara positivt!")

# x = hämta_positivt()
# print("Du angav:", x, end="\n\n")


#FLER EXEMPEL

# def vänd_sträng(text):
#     ny = ""
#     for b in text:
#         ny = b + ny
#     return ny

# print(vänd_sträng("Hej"))

# #Miniräknare:

# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mul(a, b): return a * b
# def div(a, b):
#     if b == 0: return "Fel!"
#     return a / b

# print(add(10, 3))
# print(add(10, 0))

# #Quiz-program:

# def ställ_fråga(fråga, svar):
#     g = input(fråga + " ")
#     if g.lower() == svar.lower():
#         print("Rätt!")
#         return 1
#     print(f"Fel! Rätt: {svar}")
#     return 0

# poäng = 0
# poäng += ställ_fråga("2+2?", "4")
# poäng += ställ_fråga("Huvudstad?", "Stockholm")
# print(f"Resultat: {poäng}/2")


#VAD ÄR EN LOOP

# for i in range(5):
#     print("Hej!")

# #FOR-LOOPEN

# frukter = ["Äpple", "Banan", "Apelsin"]
# for frukt in frukter:
#     print(frukt)

# #WHILE-LOOPEN

# räknare = 1
# while räknare <= 5:
#     print("Varv", räknare)
#     räknare +=1

# s = 5
# while s > 0:
#     print(s)
#     s -= 1
# print("BOOM!")

#BREAK OCH CONTINUE

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)

# while True:
#     svar = input("Skriv sluta: ")
#     if svar == "sluta":
#         break
#     print("Du skrev", svar)

#INPUT

# namn = input("Namn? ")
# print("Hej", namn)

# ålder = int(input("Ålder? "))
# print("Om 10 år:", ålder + 10)

# #LOOPAR + INPUT

# summa = 0
# for i in range(3):
#     tal = int(input(f"Tal {i+1}: "))
#     summa += tal
# print("Summa:", summa)


# lösen = "abc"

# while True:
#     f = input("Lösenord: ")
#     if f == lösen:
#         print("Rätt!")
#         break
#     print("Fel!")

#Jämna tal, 2–20:

# for i in range(2, 21, 2):
#     print(i)

#Multiplikationstabell:

# tal = int(input("Tabell? "))
# for i in range(1, 11):
#     print(f"{tal} * {i} = {tal * i}")

#Hitta största talet

# största = None
# for i in range(5):
#     t = int(input(f"Tal {i+1}: "))
#     if största is None or t > största:
#         största = t
# print("Största", största)

#Gissa talet:

# import random

# hemligt = random.randint(1, 10) #När man använder randint är både startvärdet 1 och slutvärdet 10 inkluderade!
# while True:
#     g = int(input("Gissa 1–10: "))
#     if g < hemligt: print("För lågt!")
#     elif g > hemligt: print("För högt!")
#     else:
#         print("Rätt!")
#         break

#Övningar: A-frågor:

#Skriv ett program som visar en many. Programmet ska fortsätta visa menyn tills användaren väljer alternativ 3.
   
alternativ_1 = "1. Addera två tal"
alternativ_2 = "2. Multiplicera två tal"
alternativ_3 = "3. Avsluta"


while True:
    print("\nVänligen välj ett alternativ:\n")
    print(alternativ_1)
    print(alternativ_2)
    print(alternativ_3, "\n")

    användarens_val = int(input("Val: "))

    if användarens_val == 1:
        print(f"Du valde: '{alternativ_1}'")
        tal_1, tal_2 = map(
            int,
            input("\nAnge två siffor med mellanslag: ").split()
            )
        print("\nAddition:\n"
              f"{tal_1} + {tal_2} = {tal_1 + tal_2}"
              )

    elif användarens_val == 2:
        print(f"Du valde: '{alternativ_2}'")
        tal_1, tal_2 = map(
            int,
            input("\nAnge två siffor med mellanslag: ").split()
            )
        print("\nMultiplikation:\n"
              f"{tal_1} * {tal_2} = {tal_1 * tal_2}"
              )
        
    elif användarens_val == 3:
        print(f"\nDu valde: '{alternativ_3}'")
        print("Programmet avslutas.\n")
        break
    
    else:
        print(f"\nDu valde: '{användarens_val}'")
        print("Ogiltigt val.")


#def visa_meny()
#skriver ut menyn, inget annat

#def addera_två_tal(a, b)
#"Du valde..."
#läsa in två tal
#räkna ut summan
#skriva ut resultatet

#def_multiplicera_två_tal(a, b)
#ska innehålla allt som idag ligger under elif användarens_val == 2

#def huvudprogram()
#while-loopen
#anrop till visa_meny()
#läsa användarens val
#avgöra vilken funktion som ska köras