#Sala del cine
filas = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Lista de asientos
sala = []

for fila in filas:
    for numero in range(1,11):
        sala.append((fila,numero))

# Asientos guardados 
asientos = {}

for asiento in sala:
    asientos[asiento] = "Libre"

while True:
    print("\n     1 2 3 4 5 6 7 8 9 10")

    for fila in filas:
        print(fila, "|-", end= " ")

        for numero in range(1,11):
            if asientos[(fila, numero)] == "Libre":
                print("L", end= " ")
            else:
                print("X", end= " ")    

        print()

    asiento_usuario = input("Elige asiento")

    fila = asiento_usuario[0]
    numero = int(asiento_usuario[1:])

    asiento = (fila,numero)

    if asientos[asiento] == "Libre":
        asientos[asiento] = "Ocupado"
        print("Asiento reservado")
    else:
        print("Ese asiento ya esta ocupado")

    salir = input("¿Salir? si/no:")

    if salir == "si":
        break