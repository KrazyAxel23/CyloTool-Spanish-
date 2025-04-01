#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from cylo import Bubcyz

__CHANNEL_USERNAME__ = "CyloToolChannel"
__GROUP_USERNAME__   = "CyloToolChat"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')    
    
    brand_name =  "                ╔═══╗───╔╗──╔════╗────╔╗\n"
    brand_name += "                ║╔═╗║───║║──║╔╗╔╗║────║║\n"
    brand_name += "                ║║─╚╬╗─╔╣║╔═╩╣║║╠╩═╦══╣║\n"
    brand_name += "                ║║─╔╣║─║║║║╔╗║║║║╔╗║╔╗║║\n"
    brand_name += "                ║╚═╝║╚═╝║╚╣╚╝║║║║╚╝║╚╝║╚╗\n"
    brand_name += "                ╚═══╩═╗╔╩═╩══╝╚╝╚══╩══╩═╝\n"
    brand_name += "                ────╔═╝║\n"
    brand_name += "                ────╚══╝\n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         CIERRE LA SESIÓN DE CPM ANTES DE USAR ESTA HERRAMIENTA'))
    print(Colorate.Horizontal(Colors.rainbow, '    NO ESTÁ PERMITIDO COMPARTIR LA CLAVE DE ACCESO Y SERÁ BLOQUEADO'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌           telegrama: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ DETALLES DEL JUGADOR ]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Nombre   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'ID local : {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Dinero   : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'monedas  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '!ERROR: Las cuentas nuevas deben iniciar sesión en el juego al menos una vez.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '!ERROR: ¡Parece que tu inicio de sesión no está configurado correctamente!.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ DETALLES DE LA CLAVE DE ACCESO ]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Clave de acceso : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'ID de telegrama : {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Saldo $         : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} No puede estar vacío ni contener solo espacios. Inténtalo de nuevo.'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ UBICACIÓN ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'Dirección IP : {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Ubicación    : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'País         : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ MENÚ ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Correo electrónico de la cuenta[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Contraseña de cuenta[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Clave de acceso[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = Bubcyz(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'CUENTA NO ENCONTRADA.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'CONTRASEÑA INCORRECTA.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'CLAVE DE ACCESO INVÁLIDA.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'INTENTAR OTRA VEZ.'))
                print(Colorate.Horizontal(Colors.rainbow, '! Nota: asegúrate de completar los campos!.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: aumentar el dinero                   1.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: aumentar monedas                     4.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: Rango Rey                            8K'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: Cambiar ID                           4.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: Cambiar nombre                       100'))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: Cambiar nombre (Arcoíris)            100'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: Matrículas                           2K'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: Eliminar cuenta                      FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: Registro de cuenta                   FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: Eliminar amigos                      500'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: Desbloquear coches de pago           5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: Desbloquear todos los coches         6K'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: Desbloquea todos los coches Siren    3.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: Desbloquear motor w16                4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: Desbloquea todos los cuernos         3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: Desbloquear Desactivar Daño          3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: Desbloquear combustible ilimitado    3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: Desbloquear la casa 3                4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: Desbloquear humo                     4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: Desbloquear ruedas                   4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: Desbloquear animaciones              2K'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: Desbloquear equipos M                3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{23}: Desbloquear equipos F                3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{24}: Cambiar victorias en carreras        1K'))
            print(Colorate.Horizontal(Colors.rainbow, '{25}: La carrera por el cambio pierde      1K'))
            print(Colorate.Horizontal(Colors.rainbow, '{26}: Clonar cuenta                        7K'))
            print(Colorate.Horizontal(Colors.rainbow, '{27}: Auto Interior 414hp                  2.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{28}: Ángulo personalizado                 1.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : Salida'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌 ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Seleccione un servicio [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌 ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Inserta cuanto dinero deseas.'))
                amount = IntPrompt.ask("[?] Cantidad")
                console.print("[%] Guardando tus datos: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Introduce la cantidad de monedas que deseas.'))
                amount = IntPrompt.ask("[?] Cantidad")
                console.print("[%] Guardando tus datos: ", end=None)
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: Si el rango de rey no aparece en el juego, ciérrelo y ábralo varias veces.", end=None)
                console.print("[bold red][!] Note:[/bold red]: Por favor, no hagas King Rank en la misma cuenta dos veces.", end=None)
                sleep(2)
                console.print("[%] Dándote un rango de rey: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Introduzca su nueva ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Guardando tus datos: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Introduzca su nuevo nombre.'))
                new_name = Prompt.ask("[?] Nombre")
                console.print("[%] Guardando tus datos: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Introduce tu nuevo nombre Arcoiris.'))
                new_name = Prompt.ask("[?] Nombre")
                console.print("[%] Guardando tus datos: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Dándole una Matrícula: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] Después de eliminar tu cuenta no hay vuelta atrás!!.'))
                answ = Prompt.ask("[?] Quieres eliminar esta cuenta !?", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] Registrar nueva cuenta.'))
                acc2_email = prompt_valid_value("[?] Correo electrónico de la cuenta", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Contraseña de cuenta", "Password", password=False)
                console.print("[%] Creando nueva cuenta: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFORMACIÓN: Para modificar esta cuenta con CPMElsedev.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Debes iniciar sesión en el juego usando esta cuenta.'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'This email is already exists !.'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Eliminando a tus amigos: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Nota: esta función tarda un tiempo en completarse, no la cancele.", end=None)
                console.print("[%] Desbloqueo de todos los coches pagados: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Desbloqueo de todos los coches: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Desbloqueo de la sirena de todos los coches: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Desbloqueo del motor w16: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Desbloqueo de todos los cuernos: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Desbloqueo de daño deshabilitado: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Desbloqueo de combustible ilimitado: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Desbloqueo de la Casa 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Desbloqueo de humo: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] Desbloqueo de ruedas: ", end=None)
                if cpm.unlock_wheels():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] Desbloqueo de animaciones: ", end=None)
                if cpm.unlock_animations():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] Desbloqueo de Equipos Masculinos: ", end=None)
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Desbloqueo de equipos femeninos: ", end=None)
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Inserta cuantas carreras ganaste.'))
                amount = IntPrompt.ask("[?] Cantidad")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Por favor inténtalo de nuevo.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] Inserta cuantas carreras pierdes'))
                amount = IntPrompt.ask("[?] Cantidad")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] Por favor, utilice valores válidos.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] Ingrese los detalles de la cuenta.'))
                to_email = prompt_valid_value("[?] Correo electrónico de la cuenta", "Email", password=False)
                to_password = prompt_valid_value("[?] Contraseña de cuenta", "Password", password=False)
                console.print("[%] Clonando tu cuenta: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                        
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 27:
                console.print("[bold yellow][!] Nota[/bold yellow]: La velocidad original no se puede restaurar!.")
                console.print("[bold cyan][!] Ingrese los detalles del automóvil.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] identificación del coche[/bold]")
                console.print("[bold cyan][%] Hackear la velocidad del coche[/bold cyan]:",end=None)
                if cpm.hack_car_speed(car_id):
                    console.print("[bold green]EXITOSA (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask("[?] Quieres salir? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Gracias por utilizar nuestra herramienta, únase a nuestro canal de telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Por favor, utilice valores válidos.'))
                    sleep(2)
                    continue
            elif service == 28: # ANGLE
                print(Colorate.Horizontal(Colors.rainbow, '[!] INGRESE LOS DETALLES DEL VEHÍCULO'))
                car_id = IntPrompt.ask("[red][?] IDENTIFICACIÓN DEL COCHE[/red]")
                print(Colorate.Horizontal(Colors.rainbow, '[!] INTRODUCIR EL ÁNGULO DE DIRECCIÓN'))
                custom = IntPrompt.ask("[red][?] INTRODUCE LA CANTIDAD DE ÁNGULO QUE DESEAS[/red]")                
                console.print("[red][%] HACKEANDO EL ÁNGULO DEL COCHE[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    print(Colorate.Horizontal(Colors.rainbow, 'EXITOSA'))
                    answ = Prompt.ask("[red][?] Quieres salir?[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FALLIDA'))
                    print(Colorate.Horizontal(Colors.rainbow, 'POR FAVOR INTÉNTALO DE NUEVO'))
                    sleep(2)
                    continue                                        
            else: continue
            break
        break
            
        
            
              
