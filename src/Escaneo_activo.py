import socket, nmap, json
from datetime import datetime
from scapy.all import IP, ICMP, sr1

def enviar_pkt (host):
    print(f"Comprobando conexión con: {host}\n")
    
    paquete = IP(dst=host) / ICMP()
    respuesta = sr1(paquete, timeout=2, verbose=0)
    if respuesta:
        print(f"El host {host} está activo.")
    else:
        print(f"El host {host} no está activo")
    print("---------------------------------\n")
        
def comprobar_puertos(puertos, host):
    ip = socket.gethostbyname(host)
    print(f"Iniciando escaneo de puertos en: {ip} - {host}\n")
    socket.setdefaulttimeout(1)
    puertos_abiertos=""
    for puerto, valor in puertos.items():
        enchufe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexion = enchufe.connect_ex((ip, puerto))
        if conexion == 0:
            puertos_abiertos+=f"{puerto},"

            a = f"El puerto: {puerto} ({valor}) está ABIERTO"
            print(a)
        else:
            a = f"El puerto: {puerto} ({valor}) está CERRADO"
            print(a)
        with open (f"puertos_abiertos_{MT}.txt", "a", encoding = "UTF-8") as file:
            file.write(a + "\n")
        enchufe.close()
    print("--------------------------------------")
    return puertos_abiertos

def fingerP(host, pa):
    pa_completo = pa.rstrip(",")
    escaner = nmap.PortScanner()
    print("Iniciando escaneo...")
    a = escaner.scan(hosts=host, ports=pa_completo, arguments="-sV")
    print(f"Escaneo completo para los puertos: {pa_completo}\n")
    with open (f"Reporte_fingerprinting_activo_{MT}.json", "w") as file:
        json.dump(a, file, indent=4)

def validacion(n):
    while ((n < 1) or (n > 3)):
        n = int(input("Ingrese un valor válido (1 - 3): "))
    return n

def comprobacion():
    print("\n¿Está completamente seguro de ejecutar esta tarea?")
    print('* Presione "y" si está seguro')
    print("* Presione cualquier otra tecla si no lo está\n")
    a = input(">> ")
    if a != "y":
        print("Regresando al menú...")
        return True
    return False

def main():
    while True:
        print("----------- Menú de la tarea activa -----------")
        print("1) Verificación de que el host esté activo")
        print("2) Escaneo de puertos activos y sus respectivos servicios/versiones")
        print("3) Salir")
        opcion = int(input("Ingrese una opción: "))
        opcion = validacion(opcion)
        if opcion == 1:
            c = comprobacion()
            if c:
                continue
            else:
                enviar_pkt(host)
                print("Verificación realizada.\n")
        elif opcion == 2:
            c = comprobacion()
            if c:
                continue
            else:
                pa = comprobar_puertos(puertos, host)
                fingerP(host, pa)
                print("Reporte generado.\n")
        else:
            print("Cerrando el programa...")
            exit() 

#Información
puertos = {
    21:"FTP",
    22:"SSH",
    25:"SMTP", #Email
    80:"HTTP", #Web
    110:"POP3", #Email
    143:"IMAP", #Email
    443:"HTTPS", #Web Segura
    3389:"RDP" #Escritorio Remoto
    }
host = "scanme.nmap.org"
fecha = str(datetime.now())
MT = fecha.replace(":", "-")





