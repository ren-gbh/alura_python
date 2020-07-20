from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"

argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor = argumentos_url.extrai_valor()
print(moeda_destino, moeda_origem,valor)

