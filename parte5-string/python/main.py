# Mãos na massa - Encontrando o texto após o caractere "?"
url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1:])

# Exemplo com split
'''
argumento = "moedaorigem=real"
listaargumentos = argumento.split("=")
print(listaargumentos)
'''

# Exemplo com find
'''
argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real"
index = argumento.find("=")
substring = argumento[index + 1:]
print(substring)
'''

# Exemplo com fatiamento e indices
'''  
argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real"
#............012345678910
substring = argumento[5:11]
print(substring)
'''