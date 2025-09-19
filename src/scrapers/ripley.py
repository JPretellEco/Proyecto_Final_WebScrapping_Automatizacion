from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random
import urllib.parse

def scrap_ripley(query, page=1):
    """
    Función para extraer productos de Ripley usando un término de búsqueda (query).
    
    Args:
        query (str): Palabra clave para buscar productos.
        page (int): Número de página a scrapear (por defecto 1).
    
    Returns:
        list[dict]: Lista de productos con información de título, marca, precio, link y origen.
    """
    
    # Construir URL de búsqueda
    query_encoded = urllib.parse.quote(query)
    url = f"https://simple.ripley.com.pe/search/{query_encoded}?sort=relevance_desc&page={page}"
    
    # Configuración de Selenium
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Espera aleatoria para simular comportamiento humano
    time.sleep(random.uniform(3, 6))
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    
    resultados = []
    
    productos = soup.find_all("div", class_="catalog-product-details")
    
    for producto in productos:
        titulo = producto.find("div", class_="catalog-product-details__name").text.strip()
        
        marca_tag = producto.find("div", class_="brand-logo")
        marca = marca_tag.text.strip() if marca_tag else "GENÉRICO"
        
        precio_tag = producto.find("li", class_="catalog-prices__offer-price")
        precio = precio_tag.text.strip() if precio_tag else "No disponible"
        
        link_tag = producto.find("a", href=True)
        link = "https://simple.ripley.com.pe" + link_tag['href'] if link_tag else "No disponible"
        
        resultado = {
            "titulo": titulo,
            "marca": marca,
            "precio": precio,
            "link": link,
            "origen": "Ripley"
        }
        
        resultados.append(resultado)
    
    return resultados

