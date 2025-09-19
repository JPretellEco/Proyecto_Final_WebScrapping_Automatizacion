from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def scrape_plazavea_selenium(query, max_scrolls=10, max_results=50):
    print(f"\n🛍️ Resultados de Plaza Vea para: {query}")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    resultados = []

    try:
        url = f"https://www.plazavea.com.pe/search/?_query={query.replace(' ', '%20')}"
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Showcase__content"))
        )

        prev_count = 0
        for i in range(max_scrolls):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(3)

            productos_actuales = driver.find_elements(By.CSS_SELECTOR, "div.Showcase__content")
            print(f"🔄 Scroll {i+1}: {len(productos_actuales)} productos detectados")

            if len(productos_actuales) == prev_count:
                break
            prev_count = len(productos_actuales)

        for item in productos_actuales[:max_results]:
            try:
                titulo_tag = item.find_element(By.CSS_SELECTOR, "button.Showcase__name")
                titulo = titulo_tag.text.strip() if titulo_tag else None

                precio_tag = item.find_element(By.CSS_SELECTOR, "div.Showcase__salePrice span.price")
                precio_texto = precio_tag.text.strip() if precio_tag else "No disponible"

                # 🔹 Mantener "S/" y limpiar solo el "un" u otros textos al final
                precio = re.match(r"(S/\s*[\d.,]+)", precio_texto)
                precio = precio.group(1) if precio else precio_texto

                link_tag = item.find_element(By.CSS_SELECTOR, "a.Showcase__link")
                link = link_tag.get_attribute("href") if link_tag else None

                resultados.append({
                    "titulo": titulo,
                    "precio": precio,
                    "link": link,
                    "origen": "Plaza Vea"
                })

                print(f"{titulo}\n{precio} — {link}\n")

            except Exception:
                continue

    except Exception as e:
        print("❌ Error general:", e)

    finally:
        driver.quit()

    # Eliminar duplicados por link
    seen = set()
    resultados_unicos = []
    for r in resultados:
        if r['link'] not in seen:
            resultados_unicos.append(r)
            seen.add(r['link'])

    return resultados_unicos
