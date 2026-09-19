import os
import requests

API_KEY = os.environ.get("EXCHANGE_RATE_API_KEY", "")


def obtener_tasa_moneda(base, destino):
    if not API_KEY:
        print("Falta EXCHANGE_RATE_API_KEY")
        return None
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data["conversion_rates"].get(destino)
    print("Error al obtener los datos")
    return None


def convertir_moneda():
    base = input("Ingrese la moneda de origen (ej. USD): ").upper()
    destino = input("Ingrese la moneda de destino (ej. EUR): ").upper()
    cantidad = float(input("Ingrese la cantidad a convertir: "))
    tasa = obtener_tasa_moneda(base, destino)
    if tasa:
        print(f"{cantidad} {base} es igual a {cantidad * tasa:.2f} {destino}")
    else:
        print("No se pudo realizar la conversión")


if __name__ == "__main__":
    convertir_moneda()
