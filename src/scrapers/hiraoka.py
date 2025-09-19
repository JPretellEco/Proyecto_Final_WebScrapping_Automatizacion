import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def scrape_hiraoka(query, max_pages=3):
    resultados_hiraoka = []

    for page in range(1, max_pages + 1):
        url = f"https://hiraoka.com.pe/gpsearch/?p={page}&q={quote_plus(query)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        items = soup.find_all("div", class_="product-item-info")
        if not items:
            break

        for item in items:
            # Nombre
            nombre_tag = item.find("strong", class_="product name product-item-name")
            titulo = nombre_tag.get_text(strip=True) if nombre_tag else None

            # Link del producto
            link_tag = nombre_tag.find("a") if nombre_tag else None
            link = link_tag['href'] if link_tag else None

            # Precio
            precio_tag = item.find("span", class_="price-wrapper")
            precio = precio_tag.get_text(strip=True).replace("\xa0"," ") if precio_tag else "No disponible"

            # Guardar en diccionario
            resultados_hiraoka.append({
                "titulo": titulo,
                "precio": precio,
                "link": link,
                "origen": "Hiraoka"
            })

    # Eliminar duplicados por link
    seen = set()
    resultados_unicos = []
    for r in resultados_hiraoka:
        if r['link'] not in seen:
            resultados_unicos.append(r)
            seen.add(r['link'])

    return resultados_unicos
