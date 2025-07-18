
from funcEsteticas import limpiar,carteldebarras
from datetime import datetime
import random
from colorama import init,Fore,Style
init()
cantVuelos=[["Aerolíneas Argentinas ",0],
            ["LATAM Airlines",0],
            ["Flybondi",0],
            ["GOL",0],
            ["IBERIA",0]]
vuelos = [[""]*7 for i in range(20)]
precioVuelos = [0.0]*20   
aerolineas=["AA","LATAM","FLY","GOL","IBERIA"]
matrizAsientos = [[""]*7 for i in range(40)]

def generar_asientos():
    lugarVacio= 0
    while lugarVacio < 40 and matrizAsientos[lugarVacio][0] == '':       
        for i in range(40):
            fila=[""]*7
            for j in range(7):
                if j == 3:
                    fila[j]=("")
                else:
                    fila[j]=(random.choice(["L", "O", "R"]))
            matrizAsientos[lugarVacio] = fila
            lugarVacio += 1    
def buscarAerolinea(codigo):
    i=0
    while aerolineas[i]!= codigo and i<= 4:
        i+=1
    if aerolineas[i]== codigo:
        return True
    else:
        return False
def mostrar_asientos_vuelo(nro_vuelo):
    inicio = nro_vuelo * 40
    fin = inicio + 40
    for i in range(inicio, fin):
        print(f"Fila {i - inicio + 1}: {matrizAsientos[i]}")
def listarVuelosAerolineas():
    print("Reporte de vuelos vigentes por aerolinea")
    for i in range(5):
        for j in range(5):
            if cantVuelos[i][1]>cantVuelos[j][1]:
                aux = cantVuelos[i]
                cantVuelos[i] = cantVuelos[j]
                cantVuelos[j] = aux
    print("="*65)
    print("REPORTE DE VUELOS VIGENTES POR AEROLÍNEA")
    print("="*65)
    print(f"{'POSICIÓN':<10} {'AEROLÍNEA':<30} {'CANTIDAD DE VUELOS':>20}")
    print("-"*65)

    total_vuelos = 0

    for i in range(5):
        nombre = cantVuelos[i][0]
        cantidad = cantVuelos[i][1]
        print(f"{i:<10} {nombre:<30} {cantidad:>20}")
        total_vuelos += cantidad

    print("-"*65)
    print(f"{'TOTAL DE VUELOS VIGENTES:'}{total_vuelos}")            
    print(f"{'Aerolinea con MAYOR cantidad de vuelos:'}{cantVuelos[0][0]} ({cantVuelos[0][1]})")            
    print(f"{'Aerolinea con MENOR cantidad de vuelos:'}{cantVuelos[4][0]} ({cantVuelos[4][1]})")            
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False
def gestionDeVuelo():
    
    menuVuelo = True
    while menuVuelo:
        
        print("\nMenú de vuelos")
        print("1. Crear Vuelo")
        print("2. Modificar Vuelo")
        print("3. Eliminar Vuelo")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            crearVuelo()
        elif opcion == "2":
            limpiar()
            modificarVuelo()
        elif opcion == "3":
            limpiar()
            eliminarVuelo()
        elif opcion == "4":
            limpiar()
            print("Saliendo del sistema.")
            menuVuelo= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
def verVuelos():
    print("\nVuelos actuales:")
    i=0
    while i < 20:
        if vuelos[i][0]!="":
            print("Vuelo", i+1, ":",
                  "Aerolinea:",vuelos[i][2], 
                  Fore.GREEN + "Origen:",vuelos[i][3], 
                  Fore.CYAN + "Destino:", vuelos[i][4], 
                  Fore.LIGHTGREEN_EX + "Fecha:", vuelos[i][5], 
                  "Hora:", vuelos[i][6],
                  Style.RESET_ALL)
        i+=1
def crearVuelo():
    
    print("Bienvenido a la creación de vuelos.")
    verVuelosCargados=input("¿Desea ver los vuelos actuales? (s/n): ").lower()
    while verVuelosCargados != "s" and verVuelosCargados != "n":
        verVuelosCargados = input("Opción inválida. Ingrese 's' para ver los vuelos actuales o 'n' para no verlos: ").lower()
    if verVuelosCargados == "s":
        verVuelos()
    seguirCreando=True
    while seguirCreando:
        limite=0
        try:
            while limite <= 20 and vuelos[limite][0] == '':
                print("\nIngrese los datos del vuelo:")
                print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
                vuelos[limite][2]= input("Ingrese el código de la aerolínea: ").upper()
                while buscarAerolinea(vuelos[limite][0]) == False:
                    print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
                    vuelos[limite][0] = input("Código de aerolínea inválido. Ingrese un código válido: ").upper()
                vuelos[limite][3] = input("Ingrese el origen del vuelo: ")
                vuelos[limite][4] = input("Ingrese el destino del vuelo: ")
                vuelos[limite][5] = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
                while validar_fecha(vuelos[limite][5]) == False:
                    vuelos[limite][5] = input("Fecha inválida. Ingrese una fecha válida (DD/MM/AAAA): ")
                vuelos[limite][6] = input("Ingrese la hora de salida (HH:MM): ")
                while validar_hora(vuelos[limite][6]) == False:
                    vuelos[limite][6] = input("Hora inválida. Ingrese una hora válida (HH:MM): ")
                if vuelos[limite][5] <= datetime.now().strftime("%d/%m/%Y"):
                    if vuelos[limite][1] == "AA":
                        cantVuelos[0][1] += 1
                    elif vuelos[limite][0] == "LATAM":
                        cantVuelos[1][1] += 1
                    elif vuelos[limite][0] == "FLY":
                        cantVuelos[2][1] += 1
                    elif vuelos[limite][0] == "GOL":
                        cantVuelos[3][1] += 1
                    elif vuelos[limite][0] == "IBERIA":
                        cantVuelos[4][1] += 1
                vuelos[limite][7]= limite
                vuelos[limite][0]= "A"
                try:
                    precioVuelos[limite] = float(input("Ingrese el precio del vuelo: "))
                    while precioVuelos[limite] <= 0:
                        print("El precio es erroneo, intente nuevamente")
                        precioVuelos[limite] = float(input("Ingrese el precio del vuelo: "))
                except ValueError:
                    print("Precio inválido. Debe ser un número.")
                generar_asientos()
                limite += 1
                continuar = input("¿Desea cargar otro vuelo? (s/n): ").lower()
                if continuar != "s":
                    listarVuelosAerolineas()
                    mostrar_asientos_vuelo(limite)
                    seguirCreando = False
        except IndexError:
            limpiar()
            listarVuelosAerolineas()
            print("No hay mas espacio para cargar vuelos, intente mas tarde.")
            input("Presione enter para continuar.")
            seguirCreando = False
def modificarVuelo():
    modificarVuelos = True
    while modificarVuelos:
        if vuelos[0][0] == "":
            print("No hay vuelos cargados para modificar.")
            input("Presione enter para continuar.")
            modificarVuelos = False
        else:
            print("Modificación de vuelo")
            verVuelos()
            vueloAModificar=input("Ingrese el código del vuelo a modificar: ")
            i=0
            while i < 20 and vuelos[i][1] != vueloAModificar:
                i += 1
            if vuelos[i][1] == vueloAModificar:
                if vuelos[i][0] == "B":
                    baja=input("El vuelo está dado de baja, desea modificarlo? (s/n): ")
                    while baja != "s" and baja != "n":
                        baja = input("Opción inválida. Ingrese 's' para modificar el vuelo o 'n' para no modificarlo: ").lower()
                    if baja == "s":
                        vuelos[i][0] = "A"
                        print("Datos del vuelo a modificar:", vuelos[i])
                        vuelos[i][0]= input("Ingrese el código de la aerolínea: ").upper()
                        while buscarAerolinea(vuelos[i][0]) == False:
                            print("Codigos de aerolíneas disponibles:\nAA(Aerolineas Argentinas)\nLATAM(LATAM Airlines)\nFLY\nGOL\nIBERIA")
                            vuelos[i][0] = input("Código de aerolínea inválido. Ingrese un código válido: ").upper()
                        vuelos[i][1] = input("Ingrese el nuevo origen del vuelo: ")
                        vuelos[i][2] = input("Ingrese el nuevo destino del vuelo: ")
                        vuelos[i][3] = input("Ingrese la nueva fecha de salida (DD/MM/AAAA): ")
                        while validar_fecha(vuelos[i][3]) == False:
                            vuelos[i][3] = input("Fecha inválida. Ingrese una fecha válida (DD/MM/AAAA): ")
                        vuelos[i][4] = input("Ingrese la nueva hora de salida (HH:MM): ")
                        while validar_hora(vuelos[i][4]) == False:
                            vuelos[i][4] = input("Hora inválida. Ingrese una hora válida (HH:MM): ")
                        try:
                            precioVuelos[i] = float(input("Ingrese el nuevo precio del vuelo: "))
                            while precioVuelos[i] <= 0:
                                print("El precio es erroneo, intente nuevamente")
                                precioVuelos[i] = float(input("Ingrese el nuevo precio del vuelo: "))
                        except ValueError:
                            print("Precio inválido. Debe ser un número.")
                    else:
                        modificarVuelos = False
                        print("Modificación cancelada.")                     
def eliminarVuelo():
    eliminarVuelo = True
    while eliminarVuelo:
        if vuelos[0][0] == "":
            print("No hay vuelos cargados para modificar.")
            input("Presione enter para continuar.")
            eliminarVuelo = False
        else:
            print("Eliminación de vuelos")
            verVuelos()
            vueloAEliminar=input("Ingrese el código del vuelo a modificar: ")
            i=0
            while i < 20 and vuelos[i][1] != vueloAEliminar:
                i += 1
            if vuelos[i][1] == vueloAEliminar:
                if vuelos[i][0] == "B":
                    print("El vuelo ya está dado de baja.")
                    input("Presione enter para continuar.")
                else:
                    print("Datos del vuelo a eliminar:", vuelos[i])
                    confirmacion = input("¿Está seguro que desea eliminar el vuelo? (s/n): ").lower()
                    while confirmacion != "s" and confirmacion != "n":
                        confirmacion = input("Opción inválida. Ingrese 's' para eliminar el vuelo o 'n' para no eliminarlo: ").lower()
                    if confirmacion == "s":
                        vuelos[i][0]= "B"
                    else:
                        eliminarVuelo = False
                        print("Eliminación cancelada.")
def gestionDePromociones():
    print(Fore.RED + carteldebarras("En construcción..."))
    input("Presione enter para volver al menú anterior.")
    print(Style.RESET_ALL)
def reportes():

    print(Fore.RED + carteldebarras("En construcción..."))
    input("Presione enter para volver al menú anterior.")
    print(Style.RESET_ALL)
def menu_ceo():
    menuCeo = True
    while menuCeo:
        print("\nMenú del CEO")
        print("1. Gestión de Vuelo")
        print("2. Gestión de Promociones")
        print("3. Reportes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            gestionDeVuelo()
        elif opcion == "2":
            limpiar()
            gestionDePromociones()
        elif opcion == "3":
            limpiar()
            reportes()
        elif opcion == "4":
            limpiar()
            print("Saliendo del sistema.")
            menuCeo= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
