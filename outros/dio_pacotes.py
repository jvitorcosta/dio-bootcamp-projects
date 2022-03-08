import requests

def retorna_dados_cep(cep):
    
    response = requests.get("https://viacep.com.br//ws//{}/json/".format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep["logradouro"])
    print(dados_cep["complemento"])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon))
    #response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto/")
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text
    

if __name__=='__main__':
    #1
    retorna_dados_cep("69082820")
    #2
    dados_pokemon = retorna_dados_pokemon("arceus")
    print(dados_pokemon['sprites']['front_shiny'])
    #3
    response = retorna_response('https://globallabs.academy/')
    print(response)
    
