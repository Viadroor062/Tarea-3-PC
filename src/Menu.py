import Escaneo_activo, escaneo_pasivo

def main():
    while True:
        print("----------- Menú -----------")
        print("1) Ejecutar las tareas pasivas (DNS, WHOIS, SHODAN, SUBDOMINIOS)")
        print("2) Ejecutar el menú de las tareas activas")
        print("3) Salir")
        opcion = int(input("Ingrese una opción: "))
        opcion = Escaneo_activo.validacion(opcion)
        if opcion == 1:
            escaneo_pasivo.main()
        elif opcion == 2:
            Escaneo_activo.main()
        else:
            print("Cerrando el programa...")
            exit() 

if __name__ == "__main__":
    main()



