# Proyecto Final de Ingeniería - Anderson & Pardo

En la carpeta `price` podemos encontrar los trabajos realizados relacionados a la predicción de precio de alquiler.  

- `exploration.ipynb` contiene lo que podría llamarse el ETL. Este notebook realiza la conexión a la base de datos y genera un archivo en limpio que será utilizado para las predicciones
- `machine_learning.ipynb` contiene las distintas pruebas de los modelos de machine learning que se fueron utilizando para las predicciones
- `Models` contiene el modelo entrenado en formato de archivo
- `predictor.py` es el archivo que se utilizará para generar predicciones a partir de nueva información

## Forma de utilización

Instalar primero los requerimientos presentes en `requirements.txt`

```
python3 predictor.py <PATH_A_JSON_A_PREDECIR>
```

El archivo json a predecir debe tener el siguiente formato

```
{
    "caracteristicas": ["balcony", "yard", "rooftop", "garage"],
    "amenities": ["sum", "amoblado", "cancha_paddle", "cancha_tenis", "gimnasio", "hidromasaje", "laundry", "microcine", "parrilla", "piscina", "sala_de_juegos", "sauna", "solarium", "spa", "estacionamiento_visitas", "centros_comerciales_cercanos", "parques_cercanos", "escuelas_cercanas"],
    "lat": -30,
    "lon": -30,
    "antiguedad": 30,
    "ambientes": 2,
    "cuartos": 1,
    "banos": 1,
    "superficie_total": 57,
    "barrio": "Abasto",
    "localidad": "Buenos Aires"
    }
```

Notar que `caracteristicas` y `amenities` son listas con las características y amenities del inmueble. Estas deben ser algunas de las que estan en la lista. El resto de la información puede interpretarse por el nombre.

Una vez ejecutado, el script ejecutará la prediccion utilizando el modelo y devolverá el resultado en dolares.
