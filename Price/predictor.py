import pandas as pd
from joblib import load
import sys
import json

# Vamos a esperar que la información nos llegue en formato JSON para la predicción
data_file = sys.argv[1]

with open(data_file) as json_file:
    data_json = json.load(json_file)

print("La información inicial es la siguiente")
print(data_json)

# ---------------------------------- Construcción de diccionario base ---------------------------------------
# Tenemos que de alguna forma pasar del json de entrada a las columnas que tiene el modelo
dict_df = dict()

# Tenemos que, basicamente, hacer un OneHot encoding de forma manual

### Barrios ###
# Rellenamos todos los posibles barrios
with open("Input/barrios.json") as json_file:
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
model = load('Models/gboost_model.joblib')

# Pasamos el diccionario a un dataframe para ser utilizado
df = pd.DataFrame({k: [v] for k, v in dict_df.items()})

# Debemos ordenar las columnas de la misma forma que estan en el modelo
df = df[['characteristincs_balcony', 'characteristincs_yard', 'characteristincs_rooftop', 'characteristincs_garage', 'amenities_amoblado', 'amenities_cancha_paddle', 'amenities_cancha_tenis', 'amenities_gimnasio', 'amenities_hidromasaje', 'amenities_laundry', 'amenities_microcine', 'amenities_parrilla', 'amenities_piscina', 'amenities_sala_de_juegos', 'amenities_sauna', 'amenities_solarium', 'amenities_spa', 'amenities_sum', 'amenities_centros_comerciales_cercanos', 'amenities_parques_cercanos', 'amenities_escuelas_cercanas', 'amenities_estacionamiento_visitas', 'antiquity', 'ambience', 'bedrooms', 'bathrooms', 'surface_total', 'location_neighbourhood_Abasto', 'location_neighbourhood_Agronomía', 'location_neighbourhood_Almagro', 'location_neighbourhood_Almagro Norte', 'location_neighbourhood_Almagro Sur', 'location_neighbourhood_Balvanera', 'location_neighbourhood_Congreso', 'location_neighbourhood_Once', 'location_neighbourhood_Barracas', 'location_neighbourhood_Barrio Norte', 'location_neighbourhood_La isla', 'location_neighbourhood_Parque las Heras', 'location_neighbourhood_Recoleta', 'location_neighbourhood_Belgrano', 'location_neighbourhood_Boedo', 'location_neighbourhood_Caballito', 'location_neighbourhood_Chacarita', 'location_neighbourhood_Coghlan', 'location_neighbourhood_Colegiales', 'location_neighbourhood_Constitución', 'location_neighbourhood_Flores', 'location_neighbourhood_Floresta', 'location_neighbourhood_La boca', 'location_neighbourhood_La paternal', 'location_neighbourhood_Liniers', 'location_neighbourhood_Mataderos', 'location_neighbourhood_Microcentro', 'location_neighbourhood_Monserrat', 'location_neighbourhood_Monte Castro', 'location_neighbourhood_Nuñez', 'location_neighbourhood_Palermo', 'location_neighbourhood_Parque Avellaneda', 'location_neighbourhood_Parque Centenario', 'location_neighbourhood_Parque Chacabuco', 'location_neighbourhood_Parque Chas', 'location_neighbourhood_Parque Patricios', 'location_neighbourhood_Pompeya', 'location_neighbourhood_Primera Junta', 'location_neighbourhood_Puerto Madero', 'location_neighbourhood_Retiro', 'location_neighbourhood_Saavedra', 'location_neighbourhood_San Cristobal', 'location_neighbourhood_San Nicolas', 'location_neighbourhood_San Telmo', 'location_neighbourhood_Velez Sarsfield', 'location_neighbourhood_Versalles', 'location_neighbourhood_Villa Crespo', 'location_neighbourhood_Villa del Parque', 'location_neighbourhood_Villa Devoto', 'location_neighbourhood_Villa General Mitre', 'location_neighbourhood_Villa Lugano', 'location_neighbourhood_Villa Luro', 'location_neighbourhood_Villa Ortuzar', 'location_neighbourhood_Villa Pueyrredon', 'location_neighbourhood_Villa Real', 'location_neighbourhood_Villa Riachuelo', 'location_neighbourhood_Villa Santa Rita', 'location_neighbourhood_Villa Soldati', 'location_neighbourhood_Villa Urquiza']]

prediction = model.predict(df)

print("Resultado Prediccion: ")
print(prediction)