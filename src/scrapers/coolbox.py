from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

def scrape_coolbox(query):
    url = f"https://www.coolbox.pe/audifonos?_q={query}&map=ft"

    # Configuración de Selenium
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(random.uniform(3, 6))  # Espera aleatoria para cargar la página

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    resultados = []
    productos = soup.find_all("div", class_="coolboxpe-store-search-0-x-galleryItem")

    for producto in productos:
        # Título
        titulo_tag = producto.find("section", class_="vtex-product-summary-2-x-container")
        titulo = titulo_tag.get("aria-label") if titulo_tag else "No disponible"

        # Marca
        marca_tag = producto.find("span", class_="vtex-store-components-3-x-productBrandName")
        marca = marca_tag.text.strip() if marca_tag else ""

        # Agregar marca al final del título
        if marca:
            titulo = f"{titulo} - {marca}"

        # Precio
        precio_tag = producto.find("span", class_="vtex-product-price-1-x-sellingPriceValue")
        if precio_tag:
            precio_texto = precio_tag.text.strip()
            # Limpiar texto y convertir a float
            precio = precio_texto.replace("S/", "").replace("\xa0", "").replace(",", "")
            try:
                precio = float(precio)
            except:
                precio = None
        else:
            precio = None

        # Link
        link_tag = producto.find("a", href=True)
        link = "https://www.coolbox.pe" + link_tag['href'] if link_tag else "No disponible"

        # Envío
        envio_tag = producto.find("p", class_="coolboxpe-store-logistic-0-x-shippingTagDay")
        envio = envio_tag.text.strip() if envio_tag else "No disponible"

        resultados.append({
            "titulo": titulo,
            "precio": precio,
            "link": link,
            "origen": "Coolbox"
        })

    return resultados
