
import os
import subprocess
import sys
import socket
import urllib.request
import json

cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"

def adicionar_ao_cache(chave, valor):
    cache = carregar_cache()  
    cache[chave] = valor
    salvar_cache(cache)  

def remover_do_cache(chave):
    cache = carregar_cache()  
    if chave in cache:
        del cache[chave]
        salvar_cache(cache) 

def obter_do_cache(chave):
    cache = carregar_cache()  
    return cache.get(chave)

def carregar_cache():
    try:
        with open('/root/checkuser/cache.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} 
    
def salvar_cache(cache):
    with open('/root/checkuser/cache.json', 'w') as arquivo:
        json.dump(cache, arquivo)


def get_public_ip():
    try:
        url = "https://ipinfo.io"
        response = urllib.request.urlopen(url)
        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))
            if 'ip' in data:
                return data['ip']
            else:
                print("Dirección IP pública no encontrada en la respuesta.")
                return None
        else:
            print("La solicitud al servidor falló.")
            return None
    except Exception as e:
        print("No se puede obtener la dirección IP pública:", str(e))
        return None




def verificar_processo(nome_processo):
    try:
        resultado = subprocess.check_output(["ps", "aux"]).decode()
        linhas = resultado.split('\n')
        for linha in linhas:
            if nome_processo in linha and "python" in linha:
                return True
    except subprocess.CalledProcessError as e:
        print(f"Proceso de verificación de errores: {e}")
    return False


nome_do_script = "/root/checkuser/checkuser.py"




if __name__ == "__main__":
    while True:
        os.system('clear')


        if verificar_processo(nome_do_script):
            status = f'{cor_verde}activo{cor_reset} - {cor_amarela}puerto en uso : {cor_reset}{cor_vermelha}{obter_do_cache("porta")}{cor_reset}'
        else:
            status = f'{cor_vermelha}parado{cor_reset} - {cor_amarela}puerto en uso : {cor_reset}{cor_vermelha}{obter_do_cache("porta")}{cor_reset}'
       
        print(f"{cor_amarela}Status: {status}{cor_reset}")

        print(f"")

        print(f" {cor_vermelha}Selecione una opcion :{cor_reset}")
        print(f" {cor_verde} 1 - Cerrar puerto 5454{cor_reset}")
        print(f" {cor_verde} 2 - Iniciar checkuser{cor_reset}")
        print(f" {cor_verde} 3 - Detener checkuser{cor_reset}")
        print(f" {cor_verde} 4 - Obtener enlaces{cor_reset}")
        print(f" {cor_verde} 5 - Sobre{cor_reset}")
        print(f" {cor_vermelha} 0 - Salir del menu{cor_reset}")
        print("")

        
        print(f" {cor_amarela} Digite una opcion : {cor_reset}")
        option = input()






        if option == "1":

            print(f"\n {cor_vermelha} Puerto 5454 liberado, regrese al menú e inicie checkUser en el puerto 5454 {cor_reset}")
            
            command = "sudo kill -9 $(lsof -t -i:5454)"
            subprocess.run(command, shell=True)
            
            print(f"{cor_vermelha}\nPresione la tecla Enter para regresar al menú.\n{cor_reset}")
            input()  # A linha de input sem mensagem irá para a linha abaixo do print
        elif option == "2":

            print(f" {cor_vermelha} Nota: Para trabajar de forma segura, utilice el puerto 5454 ! {cor_reset}")
            
            adicionar_ao_cache('porta', input("\n Escriba el puerto que desea utilizar y presione enter : "))

            os.system('clear')
            print(f'Porta escolhida: {obter_do_cache("porta")}')

            os.system(f'nohup python3 {nome_do_script} --port {obter_do_cache("porta")} & ')

            print(f"\n {cor_vermelha} Presione la tecla Enter para regresar al menú.\n\n {cor_reset}")
            input()
        elif option == "3":
            if verificar_processo(nome_do_script):

                try:
                    subprocess.run(f'pkill -9 -f "/root/checkuser/checkuser.py"', shell=True)

                        
                except subprocess.CalledProcessError:
                    print("Error al ejecutar el comando.")
                remover_do_cache("porta")
            else: 
                print(" {cor_vermelha} El Checkuser no está activo.{cor_reset}")
            


            input(f" {cor_vermelha} Presione la tecla Enter para regresar al menú. {cor_reset}")
        elif option == "4":
            os.system('clear')
            if verificar_processo(nome_do_script):
                print(f" {cor_vermelha} Abajo las apps, y los link para cada una : {cor_reset}")
                print("")
                ip = get_public_ip()
                porta = obter_do_cache("porta")
                print(f" {cor_amarela} SPEED-X - http://{ip}:{porta}/checkUser{cor_reset} ")
                print(f" {cor_amarela} Dt - http://{ip}:{porta}/dtmod{cor_reset}  ")
                print(f" {cor_amarela} Gl - http://{ip}:{porta}/gl{cor_reset} ")
                print(f" {cor_amarela} Any - http://{ip}:{porta}/anymod{cor_reset} ")
                print(f" {cor_amarela} AtxT - http://{ip}:{porta}/atx{cor_reset} ")
                print("")

                print(f" {cor_vermelha} Para usar de forma segura (utilice únicamente estos enlaces en las apps correspondientes){cor_reset}")
                print("")
                print(f" {cor_amarela}Link SPEED-X abajo👇 :{cor_reset} ")
                print("")
                print(f"  {cor_verde}https://terraatualizada.com/checkuser.php?url=http://{ip}:{porta}/checkUser{cor_reset} ")
                print("")
                print(f" {cor_amarela}Link Dt abajo👇 :{cor_reset} ")
                print("")
                print(f"  {cor_verde}https://terraatualizada.com/checkuser.php?url=http://{ip}:{porta}/dtmod{cor_reset}  ")
                print("")
                print(f" {cor_amarela}Link GL abajo👇 :{cor_reset} ")
                print("")
                print(f"  {cor_verde}https://terraatualizada.com/checkuser.php?url=http://{ip}:{porta}/gl{cor_reset} ")
                print("")
                print(f" {cor_amarela}Link Any abajo👇 :{cor_reset} ")
                print("")
                print(f"  {cor_verde}https://terraatualizada.com/checkuser.php?url=http://{ip}:{porta}/anymod{cor_reset} ")
                print("")
                print(f" {cor_amarela}Link AtxT abajo👇 :{cor_reset} ")
                print("")
                print(f"  {cor_verde}https://terraatualizada.com/checkuser.php?url=http://{ip}:{porta}/atx{cor_reset} ")
                print("")
                input(f" {cor_vermelha} Presione la tecla Enter para regresar al menú. {cor_reset}")

            else:
                print("\nInicie el servicio primero\n")
                print(f"\n {cor_vermelha} Presione la tecla Enter para regresar al menú.\n\n {cor_reset}")
            input()
                  

        elif option == "5":
            os.system('clear')
            print(f"{cor_amarela}Hola!, este es un multi-checkuser creado por : {cor_reset}{cor_vermelha}@Net_Satoshi{cor_reset}{cor_amarela} y mejorado para  {cor_reset} {cor_vermelha}\nWEBCONT{cor_reset}")
            print(f"{cor_amarela} Con este checkuser tiene la posibilidad de usarlo en diferentes apps {cor_reset}")
            print(f"{cor_vermelha} Apps como : {cor_reset}")
            print(f" - SPEED-X")
            print(f" - DT")
            print(f" - GL")
            print(f" - ANY")
            print(f"")
            print(f"{cor_vermelha} Presione la tecla Enter para regresar al menú. {cor_reset}")
            input()
        elif option == "0":
            sys.exit(0)
        else:
            os.system('clear')
            print(f"Si se selecciona una opción no válida, inténtelo de nuevo !")
            input(f"Presione la tecla Enter para regresar al menú.")
