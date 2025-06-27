from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

# Lista global para almacenar resultados
resultados = []
dolar = 0

def agregar_resultado(nombre, precio, fuente):
    resultados.append({
        "id": len(resultados) + 1,
        "nombre": nombre,
        "precio_bs": precio,
        "precio_usd": precio,
        "fuente": fuente
    })

# Decorador que maneja driver
def with_driver(scrapper_function):
    def wrapper():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(options=options)
        try:
            scrapper_function(driver)
        finally:
            driver.quit()
    return wrapper

@with_driver
def bcv(driver):
    url = "https://www.bcv.org.ve/"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dolar_div = soup.find("div", id="dolar")
    dolar_txt = dolar_div.find("strong")
    dolar = float(dolar_txt.text.replace("Bs. ", "").replace(",", "."))

@with_driver
def farmascrapper(driver):
    url = "https://www.farmatodo.com.ve/buscar?product=flips&departamento=Alimentos+y+Bebidas&filtros="
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all("a", class_="content-product")
    for producto in productos:
        nombre_element = producto.find('p', class_='text-title')
        precio_element = producto.find('span', class_='price__text-price')

        if nombre_element and precio_element and "Flips" in nombre_element.text:
            agregar_resultado(nombre_element.text.strip(), precio_element.text.strip(), "Farmatodo")

@with_driver
def gammascrapper(driver):
    url = "https://gamaenlinea.com/es/search/Flips"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all("div", class_="product-item")
    for producto in productos:
        nombre = producto.find('h3')
        precio = producto.find('div', class_='cx-product-price')
        if nombre and precio and "FLIPS" in nombre.text:
            try:
                precio_text = precio.text.strip().split("Ref.")[1]
            except IndexError:
                precio_text = precio.text.strip()
            agregar_resultado(nombre.text.strip(), precio_text, "Gama")

@with_driver
def locatelscrapper(driver):
    url = "https://www.locatel.com.ve/flips?_q=flips&map=ft"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all("div", class_="vtex-search-result-3-x-galleryItem")
    for producto in productos:
        nombre = producto.find('span', class_='vtex-product-summary-2-x-productBrand--NombreProducto')
        precio = producto.find('div', class_='vtex-flex-layout-0-x-flexCol--PreciosVitrinaProducto')
        if nombre and precio and "FLIPS" in nombre.text:
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Locatel")

@with_driver
def farmahorrocrapper(driver):
    url = "https://farmahorro.com.ve/etiqueta-producto/flips/?v=6898b9cae725"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all('li', class_='one-product')
    for producto in productos:
        nombre = producto.find('h4')
        precio = producto.find('bdi')
        if nombre and precio and "Flips" in nombre.text:
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Farmahorro")

@with_driver
def farmadonscrapper(driver):
    url = "https://www.farmadon.com.ve/?s=flips&post_type=product&dgwt_wcas=1"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all('section', class_='product')
    for producto in productos:
        nombre = producto.find('h3', class_='product-name')
        precio = producto.find('bdi')
        if nombre and precio and "Flips" in nombre.text:
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Farmadon")

@with_driver
def caraotamarketscrapper(driver):
    url = "https://caraotamarket.com/106_flips"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all('article', class_='product-miniature')
    for producto in productos:
        nombre = producto.find('h2', class_='product-title')
        precio = producto.find('span', class_='price')
        if nombre and precio and "FLIPS" in nombre.text:
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Caraota Market")

@with_driver
def plazascrapper(driver):
    url = "https://sanbernardino.elplazas.com/catalogsearch/result/?q=flips"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all('li', class_='product-item')
    for producto in productos:
        nombre = producto.find('a', class_='product-item-link')
        precio = producto.find('span', class_='price')
        if nombre and precio and "FLIPS" in nombre.text:
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Plazas")

@with_driver
def mibodegascrapper(driver):
    url = "https://mibodega.com.ve/?s=flips&post_type=product&dgwt_wcas=1"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all('div', class_='product')
    for producto in productos:
        nombre = producto.find('a', class_='woocommerce-LoopProduct-link')
        precio = producto.find('bdi')
        if nombre and precio and "FLIPS" in nombre.text:
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Mi Bodega")

@with_driver
def super99scrapper(driver):
    url = "https://www.super99.com/catalogsearch/result/index/?cat=202&q=flips"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    productos = soup.find_all('div', class_='product')
    for producto in productos:
        nombre = producto.find('a', class_='product-item-link')
        precio = producto.find('span', class_='price')
        if nombre and precio and ("FLIPS" in nombre.text or "Flips" in nombre.text):
            agregar_resultado(nombre.text.strip(), precio.text.strip(), "Super99")

# Ejecutar scrapers
bcv()
#farmascrapper()
#gammascrapper()
#locatelscrapper()
#farmahorrocrapper()
#farmadonscrapper()
#caraotamarketscrapper()
#plazascrapper()
#mibodegascrapper()
#super99scrapper()

# Guardar resultados

# Excel
df = pd.DataFrame(resultados)
df.to_excel("productos_flips.xlsx", index=False)

# SQLite
conn = sqlite3.connect("productos_flips.db")
df.to_sql("productos_flips", conn, if_exists="replace", index=False)
conn.close()