def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")

    print()

    print("Pesos:")
    resultado = money - expense
    Decimal = str(resultado)[3 : 5]

    print(int(resultado))
    print("Centavos")
    print(Decimal) 

change()
