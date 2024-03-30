def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}\n")
    print(f"{"Vuelto"}\n")
    print(f"Pesos:")
    print(f"{int(money - expense)}")
    print(f"Centavos:")
    print(f"{int(money % expense)**2}")
