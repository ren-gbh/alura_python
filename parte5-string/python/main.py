from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"

argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor = argumentos_url.extrai_valor()
print(moeda_destino, moeda_origem, valor)
print(len(argumentos_url))
