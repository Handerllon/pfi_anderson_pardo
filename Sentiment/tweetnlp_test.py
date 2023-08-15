# Test para probar tweetnlp

# tweetnlp provee herramiento para análisis de tweets. De Aquí se pueden obtener modelos y dataset
# la base de tweetnlp es la info de "huggingface", link que ya revisamos antes.

# Como bonus, provee análisis multilingual. Podríamos probar si funcionan mejor tweets en español traducidos
# o directamente el análisis en español

# https://github.com/cardiffnlp/tweetnlp/blob/main/tweetnlp/text_classification/model.py

import tweetnlp

model = tweetnlp.Sentiment(multilingual=True)
result = model.sentiment("El mercado esta hecho un desastre", return_probability=True)
print(str(result))