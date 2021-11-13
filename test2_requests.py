# Para poder hacer peticiones a diferentes endpoints
import requests

# Para poder mostrar los datos en formato JSON
import json

# Endpoint al que queremos hacer una petición
url = 'https://ammtp.pythonanywhere.com/testapp/post_example'

# Obtenemos la respuesta de la petición al endpoint anterior
response = requests.post(url)

# Mostramos el estado de la petición anterior
print('Status: ', response.status_code)

# Mostramos la respuesta de la petición anterior
print('Response: ', response.text)

# Obtenemos un diccionario con los datos de la respuesta de la petición anterior
diccionarioDatos = response.json()
# Mostramos los datos del diccionario
print('Respuesta en formato diccionario: ', diccionarioDatos)

# Mostramos el campo 'Accept' de la respuesta de la petición anterior
print('Accept: ', diccionarioDatos['request']['headers']['Accept'])

# Mostramos el campo 'Body' de la respuesta de la petición anterior
print('Body: ', diccionarioDatos['request']['body'])