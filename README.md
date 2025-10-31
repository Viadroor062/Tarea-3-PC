# Tarea 3 (Reconocimiento Pasivo y Activo)

Esta actividad es una herramienta diseñada para realizar tareas de reconocimiento de un objetivo web. Está dividido en dos módulos principales: escaneo pasivo y escaneo activo.

## ⚠️ ADVERTENCIA DE SEGURIDAD IMPORTANTE

Este script contiene un módulo de **escaneo activo** (`Escaneo_activo.py`).

* **El menú de opciones del escaneo activo (opción 2 del menú) solicita una segunda confirmación explicita antes de realizar el escaneo. Para proseguir se debe de introducir la "y" minúscula y para abortar se debe de introducir cualquier otro caracter**
* Ejecutar escaneos activos (como escaneo de puertos, ICMP, o fingerprinting) contra sistemas para los cuales **no tienes autorización explícita** es ilegal en muchas jurisdicciones y viola los términos de servicio de la mayoría de los proveedores de hosting.
* **Usa esta herramienta bajo tu propio riesgo** y exclusivamente en entornos controlados (como laboratorios personales) o contra objetivos que te hayan dado permiso explícito y por escrito.

---

## ⚙️ Dependencias e Instalación

Para que el proyecto funcione, necesitas instalar varias librerías de Python.

1.  Librerías utilizadas en el escaneo pasivo

    ```
    dnspython
    python-whois
    shodan
    socket
    json
    logging
    argpase
    urllib
    requests
    beautifulsoup4
    ```

2.  Librerías utilizadas en el escaneo pasivo

    ```
    socket
    json
    scapy
    python-nmap
    ```

3.  **API de Shodan:** El script de escaneo pasivo requiere una clave de API de Shodan. Debes editar el archivo `escaneo_pasivo.py` y reemplazar el valor de `SHODAN_API_KEY` con tu propia clave.

---

## 🚀 Cómo Usar

El script principal es `main.py`. Para ejecutar el programa, simplemente corre el siguiente script:

```
python main.py
