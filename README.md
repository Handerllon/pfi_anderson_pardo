
# Valorar.ar - Exploration

Repositorio de pruebas para la solución Valorar.ar. Contiene tanto trabajos de análisis exploratorio como modelado de machine learning

### Requerimientos

- Python 3.10 +

### Instalación
Antes de comenzar con la instalación, se deben configurar las variables de entorno a ser utilizadas por la aplicación. Crear una copia del archivo `.env_example` y llamarla `.env`. Completar el archivo con la información requerida.

Realizar la instalación de las librerias con el siguiente comando:  
`pip install -r requirements.txt`  

### Guía de Repositorio
El repositorio se encuentra dividido en dos carpetas principales, **Price** y **Sentiment**.

#### Price
Aquí se podran encontrar los distintos trabajos realizados en relación a la estimación de precio de alquiler. 

Dentro de la carpeta *Exploration* se podrán encontrar los distintos notebooks que fueron utilizados tanto para realizar un análisis de datos sobre la informacion como para las tareas de normalización.

A partir de estos, se generaron los llamados *Processors* que son versiones cortas del proceso de normalización, utilizado como forma de ETL.

Tenemos también el archivo `machine_learning.ipynb`. Aquí se realizaron las distintas pruebas de los modelos de machine learning a ser utilizados en la solución. En este archivo se podrán encontrar los modelos finales utilizados y los distintos parámetros utilizados para las tareas de búsqueda de hiperparámetros o *grid search*

El archivo `best_model.ipynb` contiene el modelo que mejor performa hasta la fecha.

Por último, se encuentra el archivo `predictor.py`, el cual genera una estimación de precio de renta a partir de nueva información, utilizando el mejor modelo generado a partir de las tareas de machine learning.

#### Sentiment
Aquí se podrán encontrar las tareas tanto de recolección de notas periodisticas como el "cálculo" de opinion.

El archivo principal es `sentiment_processor.py`. Este archivo se encarga de realizar tareas de scrapping de los diarios Clarín, Página 12, La Nación, Ámbito Financiero e Infobae en busca de noticias relacionadas al mercado inmobiliario.

Una vez que se recoleccionan las noticias, se analiza la opinion de la misma para luego dejar la información en la base de datos.