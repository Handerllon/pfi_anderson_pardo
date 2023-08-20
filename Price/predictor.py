import pandas as pd
from joblib import load
import sys
import json

# Cargamos el modelo para ser utilizado
model = load('Models/gboost_model.joblib')

# Vamos a esperar que la información nos llegue en formato JSON para la predicción
data_file = sys.argv[1]

with open(data_file) as json_file:
    data_json = json.load(json_file)

print(data_json)

# Que pinta va a tener la información que nos llegue? Seguramente sea algo como
"""
{
    "características": ["balcony", "yard", "rooftop", "garage"],
    "amenities": ["amoblado", "cancha_paddle", "cancha_tenis", "gimnasio", "hidromasaje", "laundry", "microcine", "parrilla", "piscina", "sala_de_juegos", "sauna", "solarium", "spa", "estacionamiento_visitas"],
    "lat": number,
    "lon": number,
    "antiguedad": 30,
    "ambientes": 2,
    "cuartos": 1,
    "baños": 1,
    "superficie_total": 57,
    "barrio": "Abasto",
    "localidad": "Buenos Aires"
    }
"""

# Las columnas que tenemos que tener para la predicción son las siguientes:
model_columns = ['characteristincs_balcony', 'characteristincs_yard', 'characteristincs_rooftop', 'characteristincs_garage', 'amenities_amoblado', 'amenities_cancha_paddle', 'amenities_cancha_tenis', 'amenities_gimnasio', 'amenities_hidromasaje', 'amenities_laundry', 'amenities_microcine', 'amenities_parrilla', 'amenities_piscina', 'amenities_sala_de_juegos', 'amenities_sauna', 'amenities_solarium', 'amenities_spa', 'amenities_sum', 'amenities_centros_comerciales_cercanos', 'amenities_parques_cercanos', 'amenities_escuelas_cercanas', 'amenities_estacionamiento_visitas', 'antiquity', 'ambience', 'bedrooms', 'bathrooms', 'surface_total', 'title_char_count', 'desc_char_count', 'location_neighbourhood_Abasto', 'location_neighbourhood_Agronomía', 'location_neighbourhood_Almagro', 'location_neighbourhood_Balvanera', 'location_neighbourhood_Barracas', 'location_neighbourhood_Barrio Norte', 'location_neighbourhood_Belgrano', 'location_neighbourhood_Boedo', 'location_neighbourhood_Caballito', 'location_neighbourhood_Chacarita', 'location_neighbourhood_Coghlan', 'location_neighbourhood_Colegiales', 'location_neighbourhood_Constitución', 'location_neighbourhood_Flores', 'location_neighbourhood_Floresta', 'location_neighbourhood_La boca', 'location_neighbourhood_La paternal', 'location_neighbourhood_Liniers', 'location_neighbourhood_Mataderos', 'location_neighbourhood_Microcentro', 'location_neighbourhood_Monserrat', 'location_neighbourhood_Monte Castro', 'location_neighbourhood_Nuñez', 'location_neighbourhood_Palermo', 'location_neighbourhood_Parque Avellaneda', 'location_neighbourhood_Parque Chacabuco', 'location_neighbourhood_Parque Patricios', 'location_neighbourhood_Puerto Madero', 'location_neighbourhood_Retiro', 'location_neighbourhood_Saavedra', 'location_neighbourhood_San Cristobal', 'location_neighbourhood_San Nicolas', 'location_neighbourhood_San Telmo', 'location_neighbourhood_Velez Sarsfield', 'location_neighbourhood_Versalles', 'location_neighbourhood_Villa Crespo', 'location_neighbourhood_Villa Devoto', 'location_neighbourhood_Villa Lugano', 'location_neighbourhood_Villa Luro', 'location_neighbourhood_Villa Ortuzar', 'location_neighbourhood_Villa Pueyrredon', 'location_neighbourhood_Villa Real', 'location_neighbourhood_Villa Urquiza', 'location_neighbourhood_Villa del Parque', 'location_locality_Buenos Aires']

# Tenemos que de alguna forma pasar del json de entrada a las columnas