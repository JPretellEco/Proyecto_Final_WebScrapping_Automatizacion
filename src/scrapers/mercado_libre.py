import requests
from bs4 import BeautifulSoup


def scrape_mercadolibre(query):
    print(f"\n📦 Resultados de MercadoLibre para: {query}")

    url = f"https://listado.mercadolibre.com.pe/{query.replace(' ', '-')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Error al obtener resultados de MercadoLibre")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("li.ui-search-layout__item")

    resultados = []

    for item in items[:10]:  # Máximo 10 productos
        try:
            titulo = item.select_one("a.poly-component__title").get_text(strip=True)
            precio = item.select_one("div.poly-price__current span.andes-money-amount__fraction").get_text(strip=True)
            link = item.select_one("a.poly-component__title")["href"]

            resultados.append({
                "titulo": titulo,
                "precio": f"S/ {precio}",
                "link": link,
                "origen": "MercadoLibre"
            })

            print(f"{titulo}\nS/ {precio} — {link}\n")

        except Exception as e:
            print("⚠️ Producto con error:", e)
            continue

    return resultados