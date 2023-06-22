#Aplicación de web scraping utilizando Python y BeautifulSoup,
#para recolectar todas las imágenes de una página web (https://par4.nl/product-categorie/gebruikte-golfballen/page/") y guardarlas en un archivo CSV.

import requests
from bs4 import BeautifulSoup
import csv

# URL base de la página web a analizar
base_url = "https://par4.nl/product-categorie/gebruikte-golfballen/page/"

# Número máximo de páginas a analizar
max_pages = 14

# Crear un archivo CSV para guardar las URLs de las imágenes
with open('imagenes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])

    # Iterar a través de las páginas
    for page in range(1, max_pages + 1):
        url = base_url + str(page) + "/"

        # Realizar la solicitud HTTP
        response = requests.get(url)

        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las etiquetas de imagen
        images = soup.find_all('img')

        # Guardar las URLs de las imágenes en el archivo CSV
        for img in images:
            img_url = img['src']
            if img_url.endswith('.jpg'):
                writer.writerow([img_url])

print("Las URLs de las imágenes en formato JPG se han guardado en 'imagenes.csv'.")
