from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar"

argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()

print(moeda_destino, moeda_origem)

