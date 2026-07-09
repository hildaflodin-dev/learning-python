#for loop:
#for i in range(5):
    #print(i)
#print("") #Inte nödvändigt, gör bara att det blir en tom rad mellan utskrifterna


#if statement:
#x = 15

#if x > 10:
    #print("Stort", end="\n\n")
#else:
    #print("Litet", end="\n\n") 


#Beräkna arean av en rektangel:

#width = 5
#height = 7.5
#area = width * height

#print("The area of a rectangle with the width", width, "units and height", height, "units, is", area, "square units")


#Input i Python3 alternativ 1

#print("What's your name?")
#name = input()
#print("Hello", name, "!")

#Input i Python3 alternativ 2

#name = input("Vad heter du? ")
#print("Hej", name,"!")

#Vi omvandlar svaret från input() från en sträng till andra datatyper (integer, float) -> CASTING
#ålder=int(input("Hur gammal är du? "))
#längd=float(input("Hur lång är du i centimeter? "))
#print("Din ålder är:",ålder,"år.\nDin längd är:", längd, "cm.")

#tal = int(input("Skriv ett tal: "))
#print(tal * 5)

#Skriv ett program där användaren anger sin ålder och programmet anger åldern om fem år:
#age = int(input("Skriv din ålder: "))
#print("Om fem år är du", age + 5, "år gammal.", end="\n\n")

#Skriv ett program där användaren anger sin längd i meter och programmet anger längen i centimeter:
#length = float(input("Skriv din längd i meter: "))
#print("Du är alltså", length * 100, "cm.", end="\n\n")

#Program för maxpuls:
#maxpuls = int(input("Skriv din ålder: "))
#print("\nDin maxpuls är", 220 - maxpuls, "slag per minut.", end="\n\n")

#For-loop:
#for n in range(5):
    #print(n, "Hej!" , end="\n\n")

#for i in range (1, 6):
    #print(i, end="\n\n")

#Använd For-Loopar för beräkningar
#summa = 0
#for i in range (1, 101):
    #summa += i
    #print(summa)

#print("\nSumman av talen 1 till 100 är", summa, end="\n\n")

#For-Loopar med Start, Stopp och Steg:

#for i in range (start, stopp, steg):
    #print(i)

#or i in range (0, 21, 5):
    #print(i)

#for i in range (1, 5): #När n=5 avsultas loopen, varför vi inte får en femte utskrift
    #print(i, "Jensen!")

#Skriv ett program som skriver ut alla heltal fr.o.m.

#a) 1 till och med 11
#print("1 till och med 11:")
#for i in range (1, 12):
    #print(i)

#print("\n")

#b) 1 till och med 100
#print("1 till och med 100:")
#for i in range (1, 101):
    #print(i)

#print("\n")

#c) -100 till och mde 5
#print("-100 till och med 5:")
#for i in range (-100, 6):
    #print(i)

#print("\n")

#d) 50 till och med -50
#print("50 till och med -50:")
#for i in range (50, -51, -1):
    #print(i)

#print("\n")

#for n in range (10, -1, -1):
    #print(n)

#Expexted output:
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#0

#Skriv ett program som skriver var 4:e tal mellan 16 och 2048 (inklusive)
#for i in range (16, 2049, 4):
    #print(i)

#print("\n")

#Skriv ett program som skriver ut de tio första talen i sjuans multiplikationstabell
#for i in range (1, 11):
    #print (i * 7, "är på plats", i, "i 7:ans tabell")

#svar = input("Är patienten ett barn? Y/N ").strip().upper()

#if svar == "Y":
    #print("\nPatienten ska ha 500 mg per dag.\n")
#else:
    #print("\nPatienten ska ha 750 mg per dag.\n")

#dos = 500 if svar == "Y" else 750

#print(f"\nPatienten ska {dos} mg per dag.\n")

#vikt = int(input("Hur mycket väger patienten? Svara i kilogram. "))

#if vikt < 20:
    #print("\nPatienten ska ges 500 mg per dag.\n")
#elif 20 <= vikt <= 40:
    #print("\nPatienten ska ges 750 mg per dag.\n")
#elif 41 <= vikt <= 60:
    #print("\nPatienten ska ges 1000 mg per dag.\n")
#else:
    #print("\nPatienten ska ges 1500 mg per dag.\n")

#i = 0

#while i < 6:
  #i += 1
  #if i == 3:
    #continue
  #print(i)

#for i in range (1, 7):
    #if i ==4:
        #continue
    #print(i)

#print("Te amo como se aman ciertas cosas oscuras,\nsecretamente,\nentre la sombra y el alma.\n\t– Pablo Neruda", end="\n\n")

#print("–Hej, trevligt att träffas.\n–Detsamma. Vad heter du?\n–Jag heter Jeckyll, vad heter du?\n–Jag heter Hyde.", end="\n\n\n")

#print("\tEXTRAPRIS:\n")
#print("\tJordgubbar")
#print("Endast 20 kr/kg!!!", end="\n\n\n")

#favoritfilm = "'Smile'"
#favoritdjur = "katt"
#favoritårstid = "sommar"
#print(f"Min favoritfilm är {favoritfilm}, mitt favoridjur är {favoritdjur} och min favoritårstid är {favoritårstid}.", end="\n\n")

#text = "Jag heter Hilda och jag lär mig programmering."
#födelsemånad = 7
#betyg = 4.5
#gillar_glass = False

#print(type(text))
#print(type(födelsemånad))
#print(type(betyg))
#print(type(gillar_glass))

#namn = input("Vänligen mata in ett personnamn: ")
#namn = namn.capitalize()

#plats = input("\nVänligen mata in ett platsnamn: ")
#plats = plats.capitalize()

#objekt = input("\nVänligen mata in namnet på ett valfritt objekt (t.ex. en boll): ")
#objekt = objekt.lower()

#print(f"\nEn dag gick {namn} till {plats} och hittade en/ett {objekt} som förändrade allt.\n")

#längd = float(input("\nVänligen ange din längd i centimeter: "))
#längd_i_meter = längd / 100
#print(f"Du är {längd_i_meter} m lång.", end="\n\n")


# vädertyp = input("Vänligen ange vädertypen på din plats [soligt, molnigt, regnigt, etc.]: ").strip().lower()
#temp = int(input("Vänligen ange temperaturen i Celcius på din plats: "))
#plats = input("Vänligen ange namnet på den plats du befinner dig: ").strip().capitalize()
#print(f"\nIdag är det {vädertyp} och {temp}°C i {plats}.", end="\n\n")

#ord_1 = input("Vänligen mata in en valfri färg: ").strip().capitalize()
#ord_2 = input("Vänligen mata in namnet på ett valfritt djur: ").strip().capitalize()
#ord_3 = int(input("Vänligen mata in en valfri siffra mellan 0–10: "))
#print(f"\n{ord_1}{ord_2}{ord_3}\n")

# ålder = int(input("Vänligen ange din ålder: "))

# if ålder < 18:
#     print("\nDu är minderårig.\n")
# elif 18 <= ålder < 25:
#     print("\nDu är ung vuxen.\n")
# elif 25 <= ålder <= 35:
#     print("\nDu är vuxen.\n")
# elif 35 <= ålder <= 40:
#     print("\nDu är i yngre medelåldern.\n")
# elif 40 < ålder <= 45:
#     print("\nDu är i medelåldern.\n")
# elif 45 < ålder <= 65:
#     print("\nDu är i övre medelåldern.\n")
# else:
#     print("\nDu är pensionär.\n")

# tal = int(input("Vänligen ange ett tal: "))

# if tal % 2 == 0:
#     print(f"{tal} är jämnt")
# else:
#     print(f"{tal} är udda")


# tal_1 = int(input("Vänligen ange ett tal: "))
# tal_2 = int(input("Vänligen ange ett annat tal: "))

# if tal_1 > tal_2:
#     print(f"{tal_1} är större än {tal_2}")
# elif tal_1 == tal_2:
#     print(f"{tal_1} är lika med {tal_2}")
# else:
#     print(f"{tal_2} är större än {tal_1}")

# print(5 + 2 * 3)
# print((5 + 2) * 3)

# tal_1 = int(input("Vänligen ange en siffra: "))
# tal_2 = int(input("Vänligen ange en till siffra: "))
# tal_3 = int(input("Vänligen ange en sista siffra: "))

# tal_1, tal_2, tal_3 = map(int, input("Ange tre siffor med mellanslag: ").split())

# print("Uträknning på formen (a + b) * c ger svaret:", (tal_1 + tal_2) * tal_3)
# print("Uträknning på formen a + b * c ger svaret:", tal_1 + tal_2 * tal_3)


# for tal in range (1, 21):
#   if tal % 2 != 0:
#     continue
#   tal += tal
#   print(tal)

  #FEL, FÖRSÖK IGEN

# for i in range(1, 11):
#   print(i)
#   i += 1

# lista = ["Hilda", "Smilla", "Malva", "Elin", "Martin"]

# for i in range (len(lista)):
#   print(lista[i])


# summa = 0

# for i in range (2, 21, 2):
#   summa += i

# print("Summan av alla jämna tal mellan 1 och 20 är", summa)


# n = 10

# while n > 0:
#   print(n)
#   n -= 1

# print("Klar!")

# tal = int(input("Vänligen ange ett heltal: "))

# if tal < 10:
#     for i in range(tal, 11):
#         print(i)
# elif tal >= 10:
#     while tal > 0:
#         print(tal)
#         tal -= 1

# dryck = input("Vill du ha kaffe, te eller vatten? ").strip().lower()

# if dryck not in ["kaffe", "te", "vatten"]:
#     print("Det valet finns inte på menyn.")
# elif dryck == "kaffe":
#     print("Du valde koffeinboost!")
# elif dryck == "te":
#     print("En lugn kopp, bra val.")
# else:
#     print("Hälsosamt val!")

# temp = int(input("Vänligen ange temperaturen på din nuvarande plats i grader Celcius: "))

# if temp < -20 or temp > 30:
#     print("Extrema väderförhållanden!")
# elif temp >= 10 and temp <= 25:
#     print("Perfekt väder!")
# else:
#     print("Ganska normalt väder.")

# lösen = input("Vänligen ange ett lösenord: ")

# if not lösen == "hemligt123": #Kan även skrivas 'if lösen != "hemligt123":'
#     print("Åtkomst nekad!")
# else:
#     print("Välkommen!")

# for i in range (1, 31):
#     if i % 4 == 0 and not i % 8 == 0:
#         print(i)
#     # i += 1 OBS! Denna rad behövs inte eftersom range() automatiskt sköter ökningen av i!

# ord = input("Vänligen ange ett ord: ")

# while not ord == "sluta":
#     print("Du skrev:", ord)
#     ord = input("Vänligen ange ett ord: ")

# tal = int(input("Vänligen ange ett heltal: "))

# while tal < 0:
#     tal = int(input("Vänligen ange ett positivt heltal: "))

# if 0 < tal < 50:
#     for i in range(1, (tal + 1), 2):
#         print(i)
#     # if tal != tal + 1:
#     #     print(tal)
# elif tal >= 50:
#     while tal >= 0:
#         print(tal)
#         tal -= 5
#     if tal != 0:
#         print(0)

# temp = int(input("Vänligen ange temperaturen ute: "))

# if temp < 0:
#     print("Ta på dig vinterkläder!\n")
# elif 0 <= temp <= 10:
#     print("Ta en jacka.\n")
# elif 11 <= temp <= 20:
#     print("En tröja räcker nog.\n")
# else:
#     print("Shorts och t-shirt funkar fint!\n")

# längd = int(input("Vänligen ange längden på sida S: "))
# area = längd ** 2
# omkrets = längd * 4
# print(f"Arean är: {area} a.e.\nOmkretsen är: {omkrets} a.e.\n")

import random

# överdelar = ["Kofta", "Blus", "Linne", "Skjorta", "Crop top", "Kavaj", "Piké"]
# underdelar = ["Jeans", "Maxikjol", "Tygbyxor", "Kostymbyxor", "A-line kjol"]
# accessoarer = ["Raybans", "Garmin-klocka", "Kristallörhängen", "Silverarmband", "Guldklocka", "Pärlörhängen"]
# skor = ["Sneakers", "Ballerinaskor", "Slip-ins", "Trainers", "Sandaler", "Boots"]

# vald_överdel = random.choice(överdelar)
# vald_underdel = random.choice(underdelar)
# vald_accessoar = random.choice(accessoarer)
# valda_skor = random.choice(skor)

# print("Dagens outfit:", end="\n\n")
# print("*", vald_överdel)
# print("*", vald_underdel)
# print("*", vald_accessoar)
# print("*", valda_skor)


#PROGRAM: GISSA NUMRET
# dator_tal = random.randint(1, 100) #Såhär skapar du ett slumpmässigt tal mellan 1–100

# gissning = int(input("Datorn tänker på ett tal mellan 1–100. Gissa talet: "))

# while gissning != dator_tal:
    
#     if gissning < dator_tal:
#         print("För lågt!")
    
#     else:
#         print("För högt!")

#     gissning = int(input("Vänligen gissa igen: "))

# print("\nRätt!\n")

# a = int(input("Ange koefficienten a: "))
# b = int(input("Ange koefficienten b: "))

# if not type(a) == int:
#     a = int(input("Något blev fel. Vänligen ange koefficienten a: "))
# elif not type(b) == int:
#     b = int(input("Något blev fel. Vänligen ange koefficienten b: "))
#FEL!

# while True:
#     try:
#         a = int(input("Ange koefficienten a: "))
#         break
#     except ValueError:
#         print("Du måste ange ett heltal.")

# while True:
#     try:
#         b = int(input("Ange koefficienten b: "))
#         break
#     except ValueError:
#         print("Du måste ange ett heltal.")

# if a != 0:
#     x = -b / a
#     print(f"x är lika med {x:.3f}")
#     #round(number, digits) avrundar valt tal till valt antal decimaler
#     #{number:.digitsf} ger det antalet decimaler du vill ha

# elif a == 0 and b == 0:
#     print("Ekvationen har oändligt många lösningar.")

# else:
#     print("Ekvationen saknar x-värde.")

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)



#Två reella lösningar (d > 0)
#En reell lösning (d = 0)
#Inga reella lösningar (d < 0)


#Små siffror: ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉

# import cmath

# def läs_heltal(text):
#     while True:
#         try: 
#             return int(input(text))
#         except ValueError:
#             print("Du måste ange ett heltal.")
    
# def lös_andragradsekvation(p, q):
#     diskriminant = (p/2)**2 - q

#     if diskriminant > 0:
#         x1 = -(p/2) + cmath.sqrt(diskriminant)
#         x2 = -(p/2) - cmath.sqrt(diskriminant)
#         print(f"x₁ = {x1:.2f}")
#         print(f"x₂ = {x2:.2f}")
    
#     elif diskriminant == 0:
#         x = -(p/2)
#         print(f"x = {x:.2f}")

#     else:
#         x1 = -(p/2) + cmath.sqrt(diskriminant)
#         x2 = -(p/2) - cmath.sqrt(diskriminant)
#         print(f"x₁ = {x1:.2f}")
#         print(f"x₂ = {x2:.2f}")

# p = läs_heltal("Vänligen ange koefficienten p: ")
# q = läs_heltal("Vänligen ange koefficienten q: ")

# lös_andragradsekvation(p, q)

# djur = ["katt", "hund", "groda", "rådjur", "fågel"]

# djur.append("älg")
# print(djur)

# djur.pop(2)
# print(djur)

# nummer = [34, 78, 19, 56, 93, 41]
# print(min(nummer))
# print(max(nummer))

# frukter = ["äpple", "banan", "äpple", "druva", "banan", "äpple"]
# print(frukter.count("äpple"))

# nummer_2 = [5, 3, 8, 6, 1, 9, 2]
# nummer_2.sort()
# print(nummer_2)
# nummer_2.reverse()
# print(nummer_2)



def läs_färg(text):
    while True:
        färg = input(text).strip().lower()

        if färg.isalpha(): #isalpha() är en strängmetod som kontrollerar om en text innehåller enbart bokstäver.
            return färg
   
        print("Du måste ange en färg med enbart bokstäver.")

def kontrollera_färg_i_register(färg):
    färger = ["röd", "blå", "grön", "gul", "svart"]

    if färg in färger: #if...in kontrollerar om ett element finns i en lsita.
        print(f"{färg.capitalize()} finns i listan!\n")
        return True
    
    else:
        print(f"{färg.capitalize()} finns inte i listan.\n")
        return False

while True:
    färg = läs_färg("Vänligen ange en färg: ")
   
    if kontrollera_färg_i_register(färg):
        break