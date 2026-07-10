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