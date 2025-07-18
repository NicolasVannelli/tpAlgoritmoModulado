from funcEsteticas import limpiar

novedad1="Promoción de verano"
novedad2="Nuevo destino agregado"
novedad3="Descuento por fidelidad"

def menu_administrador():
    menuAdministrador = True
    while menuAdministrador:
        print("\nMenú del Administrador")
        print("1. Gestión de Aerolíneas")
        print("2. Aprobar/Denegar Promociones")
        print("3. Gestión de Novedades")
        print("4. Reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            gestion_aerolineas()
        elif opcion == "2":
            limpiar()
            print("En construcción…")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "3":
            limpiar()
            gestion_novedades()
        elif opcion == "4":
            limpiar()
            print("Toca hacerla")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "5":
            limpiar()
            print("Saliendo del sistema.")
            menuAdministrador= False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
            limpiar()
def gestion_aerolineas():
    gestionAerolineas=True
    while gestionAerolineas:
        print("\nGestión de Aerolíneas")
        print("1. Crear Aerolínea")
        print("2. Modificar Aerolínea")
        print("3. Eliminar Aerolínea")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            crear_aerolineas()
        elif opcion == "2":
            limpiar()
            print("La opción 2 está en construcción")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "3":
            limpiar()
            print("La opción 3 está en construcción")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "4":
            limpiar()
            gestionAerolineas = False
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
            limpiar()
def crear_aerolineas():
    arg=0
    bra=0
    chi=0

    seguir=True
    while seguir:
        nombre = input("Nombre de la aerolínea: ")
        codigo = input("Código IATA (máximo 3 caracteres): ").upper()
        while len(codigo) > 3:
            codigo = input("Código inválido. Ingrese nuevamente (máx 3 caracteres): ").upper()
        descripcion = input("Descripción: ")
        pais = input("Código de país (ARG, CHI, BRA): ").upper()
        while pais != "ARG" and pais != "CHI" and pais != "BRA":
            pais = input("Código inválido. Ingrese ARG, CHI o BRA: ").upper()
        if pais == "ARG":
            arg+=1
        elif pais == "BRA":
            bra+=1
        elif pais == "CHI":
            chi+=1    
        

        continuar = input("¿Desea cargar otra aerolínea? (s/n): ").lower()
        limpiar()
        if continuar != "s":
            seguir=False

    # Mostrar estadísticas
    pais_mayor = ""
    if arg >= bra and arg >= chi:
        pais_mayor = "Argentina"
        mayor_cantidad=arg
    elif bra >= arg and bra >= chi:
        pais_mayor = "Brasil"
        mayor_cantidad=bra
    elif chi >= arg and chi >= bra:
        pais_mayor = "Chile"
        mayor_cantidad=chi
    pais_menor = ""
    if arg <= bra and arg <= chi:
        pais_menor = "Argentina"
        menor_cantidad=arg
    elif bra <= arg and bra <= chi:
        pais_menor = "Brasil"
        menor_cantidad=bra
    elif chi <= arg and chi <= bra:
        pais_menor = "Chile"
        menor_cantidad=chi
    print(f"\nPaís con mayor cantidad de aerolíneas: {pais_mayor} con {mayor_cantidad} aerolinea/s ")
    print(f"País con menor cantidad de aerolíneas: {pais_menor} con {menor_cantidad} aerolinea/s")
    input("Presione enter para volver al menú anterior.")
    limpiar()
def gestion_novedades():
    gestionNovedades=True
    while gestionNovedades:
        print("\nGestión de Novedades")
        print("a. Crear Novedad")
        print("b. Modificar Novedad")
        print("c. Eliminar Novedad")
        print("d. Ver Novedades")
        print("e. Volver")

        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a" or opcion == "c":
            limpiar()
            print("En construcción…")
            input("Presione enter para volver al menú anterior.")
            limpiar()
        elif opcion == "b":
            modificar_novedad()
        elif opcion == "d":
            ver_novedades()
            input("Presione enter para continuar.")
            limpiar()
        elif opcion == "e":
            gestionNovedades = False
            limpiar()
        else:
            limpiar()
            print("Opción inválida.")
            input("Presione enter para volver al menú anterior.")
def modificar_novedad():
    global novedad1, novedad2, novedad3 
    ver_novedades()
    codigo = input("Ingrese el código de la novedad que desea modificar: ").upper
    while codigo != "N1" and codigo != "N2" and codigo != "N3":
        codigo = input("Código inválido. Ingrese N1, N2 o N3: ").upper()
    if codigo == "N1":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 1: "))
        novedad1 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione enter para volver al menú anterior.")
    elif codigo == "N2":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 2: "))
        novedad2 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione enter para volver al menú anterior.")
    elif codigo == "N3":
        nuevo_texto=(input("Ingrese el nuevo texto para la novedad 3: "))
        novedad3 = nuevo_texto
        limpiar()
        print("Novedad modificada correctamente.")
        input("Presione enter para volver al menú anterior.")
def ver_novedades():
    limpiar()
    print("\nNovedades actuales:")
    print("N1:", novedad1[0])
    print("N2:", novedad2[0])  
    print("N3:", novedad3[0])  
