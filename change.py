def change():
    Gasto = 23.75
    Ingreso = 100
    print("Ingresar gasto:")
    print(Gasto)
    print("Dinero recibido")
    print(Ingreso)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    a = Ingreso - Gasto
    a = int(a)
    b = (Ingreso - Gasto)

    print(a)
    print("Centavos:")
    
    vuelto = int(a)
    c = b-vuelto
    print(int(c*100))
    

change()
