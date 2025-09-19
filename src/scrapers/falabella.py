from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_falabella_selenium(query, max_scrolls=10, max_results=50):
    print(f"\n🛍️ Resultados de Falabella para: {query}")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    resultados = []

    try:
        url = f"https://www.falabella.com.pe/falabella-pe/search?Ntt={query.replace(' ', '+')}"
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.pod-link"))
        )

        prev_count = 0
        for i in range(max_scrolls):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(3)

            productos_actuales = driver.find_elements(By.CSS_SELECTOR, "a.pod-link")
            print(f"🔄 Scroll {i+1}: {len(productos_actuales)} productos detectados")

            if len(productos_actuales) == prev_count:
                break
            prev_count = len(productos_actuales)

        for item in productos_actuales[:max_results]:
            try:
                titulo = item.find_element(By.CLASS_NAME, "pod-subTitle").text.strip()
                precio = item.find_element(By.CSS_SELECTOR, "li[data-event-price] span").text.strip()
                link = item.get_attribute("href")

                resultados.append({
                    "titulo": titulo,
                    "precio": precio,
                    "link": link,
                    "origen": "Falabella"
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
