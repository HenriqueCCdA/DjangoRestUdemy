import requests


headers = { 'Authorization': 'Token 0d70411aa592ab7157c781605f6221154d0882e4'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}5/', headers=headers)

# Testando o código de status HTTP 204
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0
