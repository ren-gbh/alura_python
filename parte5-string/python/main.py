from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=500"

argumentos_url = ExtratorArgumentosUrl(url)
argumentos_url2 = ExtratorArgumentosUrl(url2)
print(id(argumentos_url))
print(id(argumentos_url2))
print(argumentos_url == argumentos_url2)
