import os
import msvcrt
from colorama import init,Fore
init()
def input_con_asteriscos(prompt=''):
    print(prompt, end='', flush=True)
    password = ''
    iniciarPrograma = True
    while iniciarPrograma:
        ch = msvcrt.getch()
        if ch == b'\r' or ch == b'\n':
            iniciarPrograma = False
        elif ch == b'\x08':#backspace
            if len(password) > 0:
                password = password[:-1]  
                print('\b \b', end='', flush=True)  
        else:
                password += ch.decode('utf-8')
                print('*', end='', flush=True)
    return password
#Función para limpiar la consola
def limpiar():
    command = 'limpiar'
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'#Por si utiliza mac o linux
    os.system(command)
    
def carteldeasteriscos(cadena):
    linea = '*' * (4 + len(cadena))
    return( Fore.GREEN + f'{linea}\n* {cadena} *\n{linea}')
def carteldebarras(cadena):
    linea = '-' * (4+ len(cadena))
    return(f'{linea}\n| {cadena} |\n{linea}')  
