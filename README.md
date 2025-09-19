
---

````markdown
# 🛒 Comparador de Precios

Este es mi proyecto personal: una aplicación web hecha con **Flask** que me permite comparar precios de productos en distintas tiendas online de Perú.  
La idea es escribir el nombre de un producto (por ejemplo: *“redmi note 9”*) y que la aplicación busque automáticamente en varias tiendas, mostrándome los precios y enlaces.

Actualmente estoy scrapeando estas páginas:

* Falabella  
* Hiraoka  
* Mercado Libre  
* Ripley  
* Coolbox  
* Plaza Vea  

---

## 🚀 Cómo instalarlo en **Windows**

1. Clonar el repositorio:

```bash
git clone https://github.com/JPretellEco/Proyecto_Final_WebScrapping_Automatizacion.git
cd Proyecto_Final_WebScrapping_Automatizacion
````

2. Crear el entorno virtual:

```bash
python -m venv venv
```

3. Activar el entorno virtual (Windows):

```bash
venv\Scripts\activate
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

5. Entrar a la carpeta `src` y correr la aplicación Flask:

```bash
cd src
python app.py
```

6. Abrir el navegador en:

```
http://127.0.0.1:5000
```

---

## 📦 Estructura de mi proyecto

```
Proyecto_Final_WebScrapping_Automatizacion/
│
├── .gitignore            # Archivos y carpetas ignoradas por Git
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias de Python
│
├── src/                  # Código fuente principal
│   ├── app.py              # Aplicación Flask
│   ├── core/
│   │   └── search.py       # Lógica principal que orquesta los scrapers
│   ├── scrapers/
│   │   ├── coolbox.py
│   │   ├── falabella.py
│   │   ├── hiraoka.py
│   │   ├── mercado_libre.py
│   │   ├── plaza_vea.py
│   │   └── ripley.py
│   ├── static/             # Logos e imágenes
│   ├── templates/          # HTML con Jinja2
│   │   └── index.html
│   └── notebooks/          # (opcional) pruebas y desarrollo en Jupyter
│
└── tests/                  # Pruebas unitarias
```

---

## 📚 Dependencias

Mi archivo `requirements.txt` incluye:

```txt
Flask==3.0.3
selenium==4.25.0
webdriver-manager==4.0.2
beautifulsoup4==4.12.3
requests==2.32.3
lxml==5.3.0
html5lib==1.1
```

---

## ⚠️ Notas importantes

* El scraping funciona mientras las páginas no cambien su estructura HTML.
* Para **Selenium** necesito tener **Google Chrome** instalado.

  * El paquete `webdriver-manager` descarga automáticamente el **ChromeDriver** compatible.
* Algunas páginas pueden bloquear el scraping si detectan demasiado tráfico, así que lo uso solo con fines educativos.

---

```
