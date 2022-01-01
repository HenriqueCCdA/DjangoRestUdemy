import requests


headers = { 'Authorization': 'Token bf60f0a4c68813e17640d99ab3a1cb64332fff87'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes'

resultado = requests.get(url=url_base_cursos, headers=headers)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registos
assert resultado.json()['count'] == 7

# Testando se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Programação para Web com Django Framework'
