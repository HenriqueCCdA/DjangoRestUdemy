import requests


headers = { 'Authorization': 'Token 0d70411aa592ab7157c781605f6221154d0882e4'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    'titulo': 'Novo Curso de Scrum 3',
    'url': 'http://www.geekuniversity.com.br/ncs3'
}

resultado = requests.put(url=f'{url_base_cursos}5/',
                        headers=headers,
                        data=curso_atualizado)

# Testando o código de status HTTP 200
assert resultado.status_code == 200

# Testandi se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']
