import requests


# GET Avaliacoes

# avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTTP
# print(avaliacoes.status_code)

# Acessando os dados da reposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessaando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta pagina
# print(avaliacoes.json()['results'])

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando somente o nome da pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][0]['nome'])

# GET Avaliacao
# avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/7/')

# print(avaliacoes.json())

# GET Curso

headers = { 'Authorization': 'Token bf60f0a4c68813e17640d99ab3a1cb64332fff87'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos', headers=headers)

print(cursos.status_code)
print(cursos.json())