#Aplicación que descargue las imágenes de un archivo "imagenes.csv" 
#y las guarde en una carpeta determinada.

import csv
import requests
import os

# Carpeta de destino para guardar las imágenes
carpeta_destino = "carpeta_destino"

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Ruta del archivo imagenes.csv
archivo_csv = "imagenes.csv"

# Abrir el archivo CSV y leer las URLs de las imágenes
with open(archivo_csv, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Omitir la primera fila (encabezado)

    # Iterar a través de las filas del archivo CSV
    for row in reader:
        img_url = row[0]  # Obtener la URL de la imagen

        # Obtener el nombre de archivo de la URL
        nombre_archivo = img_url.split("/")[-1]

        # Generar la ruta completa para guardar la imagen
        ruta_guardado = os.path.join(carpeta_destino, nombre_archivo)

        # Descargar la imagen y guardarla en la carpeta de destino
        response = requests.get(img_url)
        with open(ruta_guardado, 'wb') as img_file:
            img_file.write(response.content)

print("Las imágenes se han descargado en la carpeta especificada.")
