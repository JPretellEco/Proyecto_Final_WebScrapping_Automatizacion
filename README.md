# 🛒 Comparador de Precios

## 📖 Descripción del proyecto
Este es un proyecto personal: una aplicación web desarrollada con **Flask** que permite comparar precios de productos en distintas tiendas online de Perú.  

El usuario escribe el nombre de un producto (por ejemplo: `redmi note 9`) y la aplicación busca automáticamente en varias tiendas, mostrando los precios y enlaces directos a las publicaciones.

Actualmente, la aplicación realiza scraping en:

- Falabella  
- Hiraoka  
- Mercado Libre  
- Ripley  
- Coolbox  
- Plaza Vea  

---

## 📦 Estructura del proyecto

```
Proyecto_Final_WebScrapping_Automatizacion/
│
├── .gitignore              # Archivos y carpetas ignoradas por Git
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias de Python
│
├── src/                    # Código fuente principal
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

## 🛠️ Herramientas utilizadas

- **Python 3.11+**
- **Flask** → para la aplicación web  
- **Selenium** + **webdriver-manager** → para automatizar el navegador  
- **BeautifulSoup4**, **lxml**, **html5lib** → para extraer y procesar el HTML  
- **Requests** → para obtener contenido de páginas sin necesidad de navegador  
- **Jinja2** → para los templates de la interfaz  

Dependencias incluidas en `requirements.txt`:

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

## 🎯 Objetivo real que soluciona

Este proyecto busca resolver el problema de **la dispersión de precios en el mercado online peruano**.  

Los usuarios suelen perder tiempo entrando a cada tienda para comparar precios de un mismo producto. Con esta aplicación:  

✅ Se automatiza la búsqueda.  
✅ Se centraliza la información en una sola interfaz.  
✅ Se facilita la comparación y la toma de decisiones de compra.  

---

## 🚀 Instalación y uso en Windows

1. **Clonar el repositorio:**

```bash
git clone https://github.com/JPretellEco/Proyecto_Final_WebScrapping_Automatizacion.git
cd Proyecto_Final_WebScrapping_Automatizacion
```

2. **Crear el entorno virtual:**

```bash
python -m venv venv
```

3. **Activar el entorno virtual (Windows):**

```bash
venv\Scripts\activate
```

4. **Instalar las dependencias:**

```bash
pip install -r requirements.txt
```

5. **Entrar a la carpeta `src` y correr la aplicación Flask:**

```bash
cd src
python app.py
```

6. **Abrir el navegador en:**

```
http://127.0.0.1:5000
```

---

## ⚠️ Notas importantes

- El scraping funciona siempre que las páginas no cambien su estructura HTML.  
- Para **Selenium** se necesita **Google Chrome** instalado.  
  - `webdriver-manager` descarga automáticamente la versión compatible de **ChromeDriver**.  
- Algunas páginas pueden limitar el acceso si detectan demasiado tráfico. Este proyecto es solo con fines **educativos**.  

---
