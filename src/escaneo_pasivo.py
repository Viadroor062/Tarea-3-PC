import dns.resolver
import whois
import shodan
import socket
import json
import logging
import argparse
from urllib.parse import urlparse
import requests
from datetime import datetime
from bs4 import BeautifulSoup


#  Configuración
SHODAN_API_KEY = "" 
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

#  Extrae dominio limpio desde URL
def normalizar_dominio(url):
    dominio = urlparse(url).netloc or urlparse(url).path
    return dominio.strip("/")

#  Registros DNS clave
def get_dns_info(domain):
    tipos = ["A", "MX", "NS"]
    resultados = {}
    for tipo in tipos:
        try:
            respuesta = dns.resolver.resolve(domain, tipo)
            resultados[tipo] = [r.to_text() for r in respuesta]
        except Exception:
            resultados[tipo] = []
    return resultados


#  WHOIS 

def get_whois_info(domain):
    try:
        datos = whois.whois(domain)
        return {
            "registrar": datos.get("registrar"),
            "creation_date": str(datos.get("creation_date")),
            "expiration_date": str(datos.get("expiration_date")),
            "emails": datos.get("emails") if isinstance(datos.get("emails"), list) else [datos.get("emails")]
        }
    except Exception:
        return {}

# Shodan
def get_shodan_info(domain):
    try:
        ip = socket.gethostbyname(domain)
        api = shodan.Shodan(SHODAN_API_KEY)
        resultado = api.host(ip)
        return {
            "puertos_abiertos": resultado.get("ports", []),
            "servicios": [item.get("product") for item in resultado.get("data", []) if item.get("product")],
            "organizacion": resultado.get("org")
        }, ip
    except Exception:
        return {}, None

#  Subdominios desde crt.sh
def buscar_subdominios(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}"
        headers = {"User-Agent": "Mozilla/5.0"}
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")
        subdominios = set()
        for td in soup.find_all("td"):
            texto = td.get_text().strip()
            if texto.endswith(domain):
                subdominios.add(texto)
        return sorted(subdominios)
    except Exception:
        return []

#  Guarda JSON reducido
def guardar_reporte(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "w") as f:
            json.dump(datos, f, indent=4)
        logging.info(f"Reporte guardado en {nombre_archivo}")
    except Exception as e:
        logging.error(f"No se pudo guardar el reporte: {e}")


#  Ejecuta escaneo pasivo
def ejecutar_footprint(url):
    dominio = normalizar_dominio(url)
    logging.info(f"Dominio objetivo: {dominio}")
    dns_info = get_dns_info(dominio)
    whois_info = get_whois_info(dominio)
    shodan_info, ip = get_shodan_info(dominio)
    subdominios = buscar_subdominios(dominio)

    reporte = {
        "dominio": dominio,
        "ip": ip,
        "dns": dns_info,
        "whois": whois_info,
        "shodan": shodan_info,
        "subdominios": subdominios
    }
    fecha = str(datetime.now())
    MT = fecha.replace(":", "-")
    guardar_reporte(f"Reporte_escaneo_pasivo_{MT}.json", reporte)

# CLI
def main():
    url = input("Ingresa el URL: ")
    ejecutar_footprint(url)

