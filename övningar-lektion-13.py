# #Break och Continue i loopar

# i = 0

# while i < 5:
#     print("This number is:", i)
#     i += 1
#     if i == 3:
#         break

# print("The end!", end = "\n\n")
# #Här upphör loopen helt när i = 3


# j = 0

# while j < 6:
#     j += 1
#     if j == 3:
#         print("Continue!")
#         continue
#     print("This number is:", j)

# print("The end!", end="\n\n")
#Här hoppar loopen över j = 3 och fortsätter kompilera så länge j < 6


#Exempel med Break:
# while True:
#     number = int(input("Enter a number (1, 2, 3 or 0 to quit): "))

#     if number == 1:
#         print("Status: One")

#     elif number == 2:
#         print("Status: Two")

#     elif number == 3:
#         print("Status: Three")

#     elif number == 0:
#         print("Program stopped")
#         break

#     else:
#         print("Invalid number")

import random

my_bag = ["Dator", "Block", "Mapp", "Pennskrin", "Vattenflaska", "Solglasögon", "Läppsyl", "Airpods", "Cykelnycklar", "Laddare", "Näsdukar", "Solskyddsmedel", "Kamm", "Hårsnodd"]
# print(random.choice(my_bag))
# print(my_bag[3])
# print(len(my_bag))

for x in my_bag: #Loop som skriver ut alla element i en lista
    print(x)

for i in range(0, len(my_bag)): #Loop som skriver ut alla element i en lista
    print(my_bag[i])

#List methods:
#len()
#append() - lägger till element i slutet av listan
#insert() - lägger till element på valfri plats i listan, syntax: lista.insert(index, element)
#pop() – tar bort element på valfritt index, syntax: lista.pop(index)
#remove() – tar bort valfritt element, syntax: lista.remove(element)
#clear() – rensar hela listan, syntax: lista.clear()
#index() – hittar index för ett känt element, syntax: lista.index(element)
#min() & max() – hittar minsta och största värdet i en lista med nummer, syntax: print(min(lista)) och print(max(lista))
#sum() – summerar en lista med nummer, syntax: print(sum(lsita))
#count() – räknar antalet gånger ett element förekommer i en lista, syntax: lista.count(element)
#sort() – sorterar en lista med nummer i stigande ordning, syntax: lista.sort()
#reverse() – reverserar en lista, syntax: lista.reverse()

my_bag.append("Handkräm")
print(my_bag)

my_bag.insert(1, "Powerbank")
print(my_bag)

print(my_bag.index("Kamm"))
my_bag.pop(13)
print(my_bag)

my_bag.remove("Handkräm")
print(my_bag)

my_bag[13] = "Scrunchie"
print(my_bag)

print(len(my_bag))

my_bag_copy = my_bag[:]
print(my_bag_copy) #Detta är ett effektivt sätt att byta namn på listan

my_bag = my_bag[1:3] #[i:] = från index t.o.m. slut, [:i] = från början t.o.m. element innan index, [i:j] = från index t.o.m. elementet innan j!
print(my_bag)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Såhär mergar man två listor med varandra:

frukter_2 = ["äpple", "banan", "päron"]
bär = ["jordgubbe", "blåbär", "hallon"]

frukter_och_bär = frukter_2 + bär
print(frukter_och_bär)

filmer = ["Matrix", "Inception", "Titanic", "Avengers", "Joker"]
print(filmer[0], filmer[-1]) #En string
print(filmer[0] + filmer[-1]) #En string utan mellanrum mellan strängarna
print(filmer[:1] + filmer[-1:]) #En array
print(filmer[:1], filmer[-1:]) #Två separata arrays

for i in range(1, 7):

    if i == 4:
        continue

    print(i)

