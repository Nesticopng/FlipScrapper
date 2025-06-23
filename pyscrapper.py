from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

def farmascrapper():
    try:
        url = "https://www.farmatodo.com.ve/buscar?product=flips&departamento=Alimentos+y+Bebidas&filtros="
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        productos = soup.find_all("a", class_="content-product")
        for producto in productos:
            nombre_element = producto.find('p', class_='text-title')
            precio_element = producto.find('span', class_='price__text-price')
            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "Flips" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

farmascrapper()

def gammascrapper():
    try:
        url = "https://gamaenlinea.com/es/search/Flips"
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tasa_html = soup.find("span", class_="currency-reference")
        tasa_html_text = tasa_html.text
        valor_bs = tasa_html_text.split("Bs.")[1].strip()
        print(f"1$ = {valor_bs}")
        productos = soup.find_all("div", class_="product-item")
        for producto in productos:
            nombre_element = producto.find('h3')
            precio_element = producto.find('div', class_='cx-product-price')
            if not precio_element or not nombre_element:
                continue
            precio = precio_element.text.strip().split("Ref.")[1]
            nombre = nombre_element.text.strip()
            if "FLIPS" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

gammascrapper()

def locatelscrapper():
    try:
        url = "https://www.locatel.com.ve/flips?_q=flips&map=ft"
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        productos = soup.find_all("div", class_="vtex-search-result-3-x-galleryItem")
        for producto in productos:
            nombre_element = producto.find('span', class_='vtex-product-summary-2-x-productBrand--NombreProducto')
            precio_element = producto.find('div', class_='vtex-flex-layout-0-x-flexCol--PreciosVitrinaProducto')

            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "FLIPS" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

locatelscrapper()

def farmahorrocrapper():
    try:
        url = "https://farmahorro.com.ve/etiqueta-producto/flips/?v=6898b9cae725"
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        productos = soup.find_all('li', class_='one-product')

        for producto in productos:
            nombre_element = producto.find('h4')
            precio_element = producto.find('bdi')

            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "Flips" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

farmahorrocrapper()

def farmadonscrapper():
    try:
        url = "https://www.farmadon.com.ve/?s=flips&post_type=product&dgwt_wcas=1"

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        productos = soup.find_all('section', class_='product')

        for producto in productos:
            nombre_element = producto.find('h3', class_='product-name')
            precio_element = producto.find('bdi')

            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "Flips" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

farmadonscrapper()

def caraotamarketscrapper():
    try:
        url = "https://caraotamarket.com/106_flips"

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        productos = soup.find_all('article', class_='product-miniature')

        for producto in productos:
            nombre_element = producto.find('h2', class_='product-title')
            precio_element = producto.find('span', class_='price')

            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "FLIPS" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

caraotamarketscrapper()

def plazascrapper():
    try:
        url = "https://sanbernardino.elplazas.com/catalogsearch/result/?q=flips"

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        productos = soup.find_all('li', class_='product-item')

        for producto in productos:
            nombre_element = producto.find('a', class_='product-item-link')
            precio_element = producto.find('span', class_='price')

            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "FLIPS" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

plazascrapper()

def mibodegascrapper():
    try:
        url = "https://mibodega.com.ve/?s=flips&post_type=product&dgwt_wcas=1"

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        productos = soup.find_all('div', class_='product')

        for producto in productos:
            nombre_element = producto.find('a', class_='woocommerce-LoopProduct-link')
            precio_element = producto.find('bdi')

            if not precio_element or not nombre_element:
                continue
            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()
            if "FLIPS" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

mibodegascrapper()

def super99scrapper():
    try:
        url = "https://www.super99.com/catalogsearch/result/index/?cat=202&q=flips"

        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        productos = soup.find_all('div', class_='product')

        for producto in productos:
            nombre_element = producto.find('a', class_='product-item-link')
            precio_element = producto.find('span', class_='price')

            if not precio_element or not nombre_element:
                continue

            nombre = nombre_element.text.strip()
            precio = precio_element.text.strip()

            if "FLIPS" in nombre or "Flips" in nombre:
                print(f"Producto: {nombre}, Precio: {precio}")
    finally:
        driver.quit()

super99scrapper()