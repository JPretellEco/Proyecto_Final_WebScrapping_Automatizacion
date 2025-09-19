from src.scrapers.falabella import scrape_falabella_selenium
from src.scrapers.hiraoka import scrape_hiraoka
from src.scrapers.mercado_libre import scrape_mercadolibre
from src.scrapers.ripley import scrap_ripley
from src.scrapers.coolbox import scrape_coolbox
from src.scrapers.plaza_vea import scrape_plazavea_selenium  # 🔹 Importamos el scraper de Plaza Vea

def buscar_producto(query, max_pages=3):
    resultados = []

    # 🔹 Scrape Falabella
    try:
        falabella = scrape_falabella_selenium(query)
        resultados.extend(falabella)
    except Exception as e:
        print("❌ Error Falabella:", e)

    # 🔹 Scrape Hiraoka
    try:
        hiraoka = scrape_hiraoka(query, max_pages=max_pages)
        resultados.extend(hiraoka)
    except Exception as e:
        print("❌ Error Hiraoka:", e)

    # 🔹 Scrape MercadoLibre
    try:
        mercadolibre = scrape_mercadolibre(query)
        resultados.extend(mercadolibre)
    except Exception as e:
        print("❌ Error MercadoLibre:", e)

    # 🔹 Scrape Ripley
    try:
        ripley = scrap_ripley(query, page=1)
        resultados.extend(ripley)
    except Exception as e:
        print("❌ Error Ripley:", e)

    # 🔹 Scrape Coolbox
    try:
        coolbox = scrape_coolbox(query)
        resultados.extend(coolbox)
    except Exception as e:
        print("❌ Error Coolbox:", e)

    # 🔹 Scrape Plaza Vea
    try:
        plazavea = scrape_plazavea_selenium(query)
        resultados.extend(plazavea)
    except Exception as e:
        print("❌ Error Plaza Vea:", e)

    # 🔹 Eliminar duplicados por link
    seen = set()
    resultados_unicos = []
    for r in resultados:
        if r['link'] not in seen:
            resultados_unicos.append(r)
            seen.add(r['link'])

    return resultados_unicos
