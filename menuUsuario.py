from funcEsteticas import limpiar,carteldebarras
from colorama import Fore,init,Style
from datetime import datetime
from menuCeo import vuelos,precioVuelos,matrizAsientos

matriz_asientos_prueba = [
    ["O", "L", "L", " ", "O", "R", "R"],
    ["R", "R", "L", " ", "L", "L", "O"],
    ["O", "L", "O", " ", "R", "O", "L"],
    ["L", "O", "R", " ", "O", "O", "R"],
    ["O", "O", "R", " ", "R", "L", "L"],
    ["L", "L", "O", " ", "O", "R", "O"],
    ["R", "O", "L", " ", "L", "O", "R"],
    ["L", "R", "L", " ", "R", "L", "L"],
    ["R", "R", "R", " ", "O", "L", "R"],
    ["O", "L", "O", " ", "L", "R", "L"],
    ["L", "R", "R", " ", "O", "O", "R"],
    ["R", "L", "O", " ", "L", "R", "L"],
    ["O", "R", "O", " ", "O", "O", "L"],
    ["L", "L", "R", " ", "R", "R", "O"],
    ["O", "O", "O", " ", "L", "L", "L"],
    ["R", "R", "L", " ", "O", "R", "R"],
    ["L", "O", "L", " ", "O", "O", "O"],
    ["R", "L", "O", " ", "R", "L", "R"],
    ["O", "R", "R", " ", "O", "R", "L"],
    ["L", "O", "L", " ", "L", "L", "R"],
    ["R", "R", "O", " ", "R", "O", "O"],
    ["L", "L", "R", " ", "O", "R", "L"],
    ["O", "R", "L", " ", "L", "L", "R"],
    ["R", "L", "L", " ", "R", "R", "L"],
    ["L", "O", "R", " ", "O", "L", "O"],
    ["O", "R", "O", " ", "R", "O", "R"],
    ["R", "L", "R", " ", "L", "R", "L"],
    ["O", "O", "L", " ", "O", "L", "O"],
    ["L", "L", "O", " ", "R", "R", "R"],
    ["R", "O", "L", " ", "O", "L", "R"],
    ["O", "R", "R", " ", "L", "L", "L"],
    ["L", "L", "L", " ", "R", "O", "O"],
    ["O", "O", "O", " ", "R", "R", "L"],
    ["R", "L", "O", " ", "O", "O", "L"],
    ["L", "O", "R", " ", "L", "R", "R"],
    ["O", "R", "O", " ", "O", "L", "R"],
    ["R", "R", "L", " ", "L", "L", "O"],
    ["O", "L", "R", " ", "R", "R", "R"],
    ["L", "L", "O", " ", "O", "O", "L"],
    ["R", "O", "R", " ", "L", "L", "R"]
]
init()
vuelosUsuario = [[""]*7 for i in range(20)]
def mostrar_matriz(codigo):
    i = 0
    while i < 40:
        j = 0
        while j < 7:
            if j == 3:
                print("|", end="  ")  # Pasillo
            else:
                print(matrizAsientos[codigo][j], end="  ")
            j += 1
        print()  # Salto de línea al final de cada fila
        i += 1
def buscarCodigo(codigo):
    i=0
    while vuelosUsuario[i][1]!= codigo and i<= 20:
        i+=1
    if vuelosUsuario[i][1]== codigo:
        return True
    else:
        return "n"
def verVuelosUsuario():
    print("\nVuelos actuales:")
    i=0
    while i < 20:
        if vuelosUsuario[i][0]!="" and vuelosUsuario[i][0]!="B":
            print("Vuelo", i+1, ":",
                  "Código:", vuelosUsuario[i][1],
                  "Aerolinea:",vuelosUsuario[i][2], 
                  Fore.GREEN + "Origen:",vuelosUsuario[i][3], 
                  Fore.CYAN + "Destino:", vuelosUsuario[i][4], 
                  Fore.LIGHTGREEN_EX + "Fecha:", vuelosUsuario[i][5], 
                  "Hora:", vuelosUsuario[i][6],
                    Fore.YELLOW + "Precio:", precioVuelos[i],
                  Style.RESET_ALL)
        i+=1
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
def buscarVuelo():
    fecha= input("Ingrese la fecha de salida (DD/MM/AAAA): ")
    while validar_fecha(fecha) == False:
        print("Fecha inválida. Por favor, ingrese una fecha en formato DD/MM/AAAA.")
        fecha = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
    i=0
    while i < 20 and vuelos[i][0] != '':
        if vuelos[i][0]== "B":
            i=i
        elif vuelos[i][5] >= fecha:
            vuelosUsuario[i][0] = vuelos[i][0]
            vuelosUsuario[i][1] = vuelos[i][1]
            vuelosUsuario[i][2] = vuelos[i][2]
            vuelosUsuario[i][3] = vuelos[i][3]
            vuelosUsuario[i][4] = vuelos[i][4]
            vuelosUsuario[i][5] = vuelos[i][5]
            vuelosUsuario[i][6] = vuelos[i][6]
        i +=1
    verVuelosUsuario()
def buscarAsientos():
    try:
        codigo_vuelo = input("Ingrese el código del vuelo: ")
        while buscarCodigo(codigo_vuelo) == "n":
            codigo_vuelo = input("Código inválido. Ingrese un código de vuelo válido: ")
        codigo_vuelo = int(codigo_vuelo)
        mostrar_matriz(codigo_vuelo)
        input("Presione enter para continuar.")
    except IndexError:
        print("El código de vuelo no existe o no se ha ingresado correctamente.")
        print("En caso de que el problema persista, vuelva a buscar vuelos")
        input("Presione enter para volver al menú anterior.")
        limpiar()     
def menu_usuario():
    menuUsuario = True
    while menuUsuario:
        print("\nMenú de usuario")
        print("1. Buscar Vuelo")
        print("2. Buscar asientos")
        print("3. Reservar Vuelos")
        print("4. Gestionar Reservas")
        print('5. Ver historial de compras(reservas con estado "Confirmada")')
        print("6. Ver Novedades")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            buscarVuelo()
        elif opcion == "2":
            limpiar()
            buscarAsientos()
        elif opcion == "3":
            limpiar()
            reservarVuelo()
        elif opcion == "4":
            limpiar()
            reportes()
        elif opcion == "5":
            limpiar()
            reportes()
        elif opcion == "6":
            limpiar()
            reportes()
        elif opcion == "7":
            limpiar()
            print("Saliendo del sistema.")
            menuUsuario= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
def gestionDePromociones():
    print(Fore.RED + carteldebarras("En construcción..."))
    input(Style.RESET_ALL+"Presione enter para volver al menú anterior.")
    limpiar()
def reportes():
    print(Fore.RED + carteldebarras("En construcción..."))
    input(Style.RESET_ALL+"Presione enter para volver al menú anterior.")
    limpiar()
def reservarVuelo():
    print(Fore.RED + carteldebarras("En construcción..."))
    input(Style.RESET_ALL+"Presione enter para volver al menú anterior.")
    limpiar()
buscarAsientos()