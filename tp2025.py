
from menuCeo import menu_ceo
from funcEsteticas import limpiar, input_con_asteriscos, carteldeasteriscos
from menuAdm import menu_administrador
from menuUsuario import menu_usuario

usuarios = [
    ["admin@ventaspasajes777.com","admin","administrador"],
    ["ceo1@ventaspasajes777.com","ceo123","ceo"],
    ["ceo2@ventaspasajes777.com","ceo456","ceo"],
    ["ceo3@ventaspasajes777.com","ceo789","ceo"],
    ["ceo4@ventaspasajes777.com","ceo012","ceo"],
    ["ceo5@ventaspasajes777.com","ceo345","ceo"],
    ["usuario1@ventaspasajes777.com","usuario123","usuario"],   
    ["usuario2@ventaspasajes777.com","usuario456","usuario"],
    ["","",""],
    ["","",""]]

def iniciar():
    inicio= input("¿Desea registrarse o desea iniciar sesión? (r/i): ").lower()
    while inicio != "r" and inicio != "i":
        inicio = input("Opción inválida. Ingrese 'r' para registrarse o 'i' para iniciar sesión: ").lower()
    if inicio == "r":
        limpiar()
        registrarse()
    elif inicio == "i":
        limpiar()
        login()
# Función para logear
def registrarse():
    limpiar()
    print("Registro de usuario")
    email = input("Ingrese su correo electrónico: ")
    while "@" not in email and email !="":
        email = input("Correo inválido. Ingrese un correo electrónico válido: ")
    
    contraseña = input_con_asteriscos("Ingrese su contraseña: ")

    tipo_usuario = "usuario"
    
    registrado = False
    j = 0

    while j < 10:
        if usuarios[j][0] == email:
            print("Este correo ya está registrado.")
            registrado = True  
            j = 10             
        j += 1
    if registrado == False:
        i=0
        try:
            while i < 10:
                if usuarios[i][0] =="" and registrado == False:
                    usuarios[i][0] = email
                    usuarios[i][1] = contraseña
                    usuarios[i][2] = tipo_usuario
                    registrado = True
                    print("\nRegistro exitoso.")
                    
                i+=1
        except IndexError:
            limpiar()
            print("Ocurrió un error al registrar el usuario, intente mas tarde")
            input("Presione enter para continuar.")
            limpiar()
            return
    if registrado == True:
        limpiar()
        print("Usuario registrado exitosamente.")
        print("Ahora puede iniciar sesión.")
    else:
        limpiar()
        print("No se pudo registrar el usuario, posiblemente no haya mas cupos, intente mas tarde.")
    input("Presione enter para continuar.")
    limpiar()
    iniciar()
def login():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese usuario: ")
        contraseña = input_con_asteriscos("Ingrese contraseña: ")
        print("Presione enter sin ingresar nigún dato para salir del sistema.")
        try:
            if usuario == "" or contraseña == "":
                print("Saliendo del sistema.")
                intentos = 3
            i=0
            while usuario != usuarios[i][0] and i < 10:
                i += 1
            if usuarios[i][0] == usuario and usuarios[i][1] == contraseña:
                if usuarios[i][2] == "administrador":
                    limpiar()
                    menu_administrador()
                elif usuarios[i][2] == "ceo":
                    limpiar()
                    menu_ceo()
                elif usuarios[i][2] == "usuario":
                    limpiar()
                    menu_usuario()
        except:
            limpiar()
            print("Usuario o contraseña incorrectos.")
            intentos += 1
    print("El sistema se cerrará, hasta luego!.")

# Ejecución del programa
iniciar()

print(carteldeasteriscos('Este trabajo fue hecho por Nicolás Vannelli, Mateo Paolizzi, Agustín Andrenacci,Mateo Glich Vargas .'))