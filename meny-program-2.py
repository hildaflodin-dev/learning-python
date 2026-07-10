
alternativ_1 = "1. Addera två tal"
alternativ_2 = "2. Multiplicera två tal"
alternativ_3 = "3. Avsluta"

#När alternativ-variablerna finns UTANFÖR funktionen, kan övriga funktioner ha tillgång till dessa variabler!

def visa_meny():

    print("\nVänligen välj ett alternativ:\n"
          f"\n{alternativ_1}\n"
          f"{alternativ_2}\n"
          f"{alternativ_3}\n"
    )


def addera_två_tal():

    print(f"Du valde: '{alternativ_1}'")

    tal_1, tal_2 = map(
        int,
        input("\nAnge två siffor med mellanslag: ").split()
    )
        
    resultat = f"\nAddition:\n{tal_1} + {tal_2} = {tal_1 + tal_2}"
    print(resultat)


def multiplicera_två_tal():

    print(f"Du valde: '{alternativ_2}'")

    tal_1, tal_2 = map(
        int,
        input("\nAnge två siffor med mellanslag: ").split()
        )
    
    resultat = f"\nMultiplikation:\n{tal_1} * {tal_2} = {tal_1 * tal_2}"
    print(resultat)


def huvudprogram():
    
    while True:
        
        visa_meny()
        användarens_val = int(input("Val: "))

        if användarens_val == 1:
            addera_två_tal()
        
        elif användarens_val == 2:
            multiplicera_två_tal()

        elif användarens_val == 3:
            print(f"\nDu valde: '{alternativ_3}'")
            print("Programmet avslutas.\n")
            break
    
        else:
            print(f"\nDu valde: '{användarens_val}'")
            print("Ogiltigt val.")


huvudprogram()