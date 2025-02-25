import pandas as pd
from joblib import load
import os
import sys
import json

PATH = os.path.dirname(os.path.abspath(__file__))

# Vamos a esperar que la información nos llegue en formato JSON para la predicción
data_file = sys.argv[1]

with open(data_file) as json_file:
    data_json = json.load(json_file)

# ---------------------------------- Construcción de diccionario base ---------------------------------------
# Tenemos que de alguna forma pasar del json de entrada a las columnas que tiene el modelo
dict_df = dict()

# Tenemos que, basicamente, hacer un OneHot encoding de forma manual

### Barrios ###
# Rellenamos todos los posibles barrios
with open(str(PATH) + "/Utils/barrios.json") as json_file:
    barrios = json.load(json_file)

# Generamos columnas para cada uno de los barrios
for neighborhood in barrios.values():
    dict_df["location_neighbourhood_"+neighborhood] = 0

### Characteristics ###
characteristics = ["balcony", "yard", "rooftop", "garage"]
for char in characteristics:
    dict_df["characteristincs_"+char] = 0

### Amenities ###
amenities = ["sum", "amoblado", "cancha_paddle", "cancha_tenis", "gimnasio", "hidromasaje", "laundry", "microcine", "parrilla", "piscina", "sala_de_juegos", "sauna", "solarium", "spa", "estacionamiento_visitas", "centros_comerciales_cercanos", "parques_cercanos", "escuelas_cercanas"]
for am in amenities:
    dict_df["amenities_"+am] = 0

### Columnas extra que tenemos ###
dict_df["antiquity"] = 0
dict_df["ambience"] = 0
dict_df["bedrooms"] = 0
dict_df["bathrooms"] = 0
dict_df["surface_total"] = 0
dict_df["centros_comerciales_cercanos"] = 0
dict_df["parques_cercanos"] = 0
dict_df["escuelas_cercanas"] = 0


# ---------------------------------- Rellenamos el diccionario base con info que nos llego ---------------------------------------

### Tenemos que ahora tomar el json que nos llega del "cliente" y pasarlo a nuestro formato
# Rellenamos los campos directos
dict_df["antiquity"] = data_json["antiguedad"]
dict_df["ambience"] = data_json["ambientes"]
dict_df["bedrooms"] = data_json["cuartos"]
dict_df["bathrooms"] = data_json["banos"]
dict_df["surface_total"] = data_json["superficie_total"]

# Llenamos el barrio
dict_df["location_neighbourhood_"+data_json["barrio"]] = 1

# Llenamos las caracteristicas que nos hayan llegado
for char in data_json["caracteristicas"]:
    dict_df["characteristincs_"+char] = 1

# Llenamos las amenities que nos hayan llegado
for am in data_json["amenities"]:
    dict_df["amenities_"+am] = 1


# ---------------------------------- Utilización del modelo --------------------------------------- 

# Cargamos el modelo para ser utilizado
model = load(str(PATH) + '/Models/gboost_model7.joblib')

# Pasamos el diccionario a un dataframe para ser utilizado
df = pd.DataFrame({k: [v] for k, v in dict_df.items()})

# Debemos ordenar las columnas de la misma forma que estan en el modelo
df = df[['characteristincs_balcony', 'characteristincs_yard', 'characteristincs_rooftop', 'characteristincs_garage', 'amenities_amoblado', 'amenities_cancha_paddle', 'amenities_cancha_tenis', 'amenities_gimnasio', 'amenities_hidromasaje', 'amenities_laundry', 'amenities_microcine', 'amenities_parrilla', 'amenities_piscina', 'amenities_sala_de_juegos', 'amenities_sauna', 'amenities_solarium', 'amenities_spa', 'amenities_sum', 'amenities_estacionamiento_visitas', 'antiquity', 'ambience', 'bedrooms', 'bathrooms', 'surface_total', 'centros_comerciales_cercanos', 'parques_cercanos', 'escuelas_cercanas', 'location_neighbourhood_Abasto', 'location_neighbourhood_Agronomía', 'location_neighbourhood_Almagro', 'location_neighbourhood_Almagro Norte', 'location_neighbourhood_Almagro Sur', 'location_neighbourhood_Balvanera', 'location_neighbourhood_Congreso', 'location_neighbourhood_Once', 'location_neighbourhood_Barracas', 'location_neighbourhood_Barrio Norte', 'location_neighbourhood_La isla', 'location_neighbourhood_Parque las Heras', 'location_neighbourhood_Recoleta', 'location_neighbourhood_Belgrano', 'location_neighbourhood_Belgrano Barrancas', 'location_neighbourhood_Belgrano C', 'location_neighbourhood_Belgrano La Imprenta', 'location_neighbourhood_Belgrano R', 'location_neighbourhood_Boedo', 'location_neighbourhood_Caballito', 'location_neighbourhood_Caballito Barrio Ingles', 'location_neighbourhood_Caballito Cid Campeador', 'location_neighbourhood_Caballito Norte', 'location_neighbourhood_Caballito Parque Rivadavia', 'location_neighbourhood_Caballito Primera Junta', 'location_neighbourhood_Caballito Sur', 'location_neighbourhood_Chacarita', 'location_neighbourhood_Coghlan', 'location_neighbourhood_Colegiales', 'location_neighbourhood_Constitución', 'location_neighbourhood_Flores', 'location_neighbourhood_Flores Norte', 'location_neighbourhood_Flores Sur', 'location_neighbourhood_Floresta', 'location_neighbourhood_Floresta Norte', 'location_neighbourhood_Floresta Sur', 'location_neighbourhood_La boca', 'location_neighbourhood_La paternal', 'location_neighbourhood_Liniers', 'location_neighbourhood_Mataderos', 'location_neighbourhood_Microcentro', 'location_neighbourhood_Monserrat', 'location_neighbourhood_Monte Castro', 'location_neighbourhood_Núñez', 'location_neighbourhood_Núñez Lomas', 'location_neighbourhood_Núñez River', 'location_neighbourhood_Palermo', 'location_neighbourhood_Palermo Botanico', 'location_neighbourhood_Palermo Boulevard', 'location_neighbourhood_Palermo Chico', 'location_neighbourhood_Palermo Hollywood', 'location_neighbourhood_Palermo Las Cañitas', 'location_neighbourhood_Palermo Pacifico', 'location_neighbourhood_Palermo Plaza Italia', 'location_neighbourhood_Palermo Soho', 'location_neighbourhood_Palermo Viejo', 'location_neighbourhood_Parque Avellaneda', 'location_neighbourhood_Parque Centenario', 'location_neighbourhood_Parque Chacabuco', 'location_neighbourhood_Parque Chas', 'location_neighbourhood_Parque Patricios', 'location_neighbourhood_Pompeya', 'location_neighbourhood_Primera Junta', 'location_neighbourhood_Puerto Madero', 'location_neighbourhood_Retiro', 'location_neighbourhood_Retiro Catalinas', 'location_neighbourhood_Retiro Plaza San Martín', 'location_neighbourhood_Saavedra', 'location_neighbourhood_San Cristóbal', 'location_neighbourhood_San Nicolás', 'location_neighbourhood_Tribunales', 'location_neighbourhood_San Telmo', 'location_neighbourhood_Velez Sarsfield', 'location_neighbourhood_Versalles', 'location_neighbourhood_Villa Crespo', 'location_neighbourhood_Villa del Parque', 'location_neighbourhood_Villa Devoto', 'location_neighbourhood_Villa General Mitre', 'location_neighbourhood_Villa Lugano', 'location_neighbourhood_Villa Luro', 'location_neighbourhood_Villa Ortúzar', 'location_neighbourhood_Villa Pueyrredón', 'location_neighbourhood_Villa Real', 'location_neighbourhood_Villa Riachuelo', 'location_neighbourhood_Villa Santa Rita', 'location_neighbourhood_Villa Soldati', 'location_neighbourhood_Villa Urquiza']]

prediction = model.predict(df)

import requests
res = requests.get("https://dolarapi.com/v1/dolares/blue")
dolar_blue = res.json()["compra"]

print(prediction[0]*dolar_blue)
