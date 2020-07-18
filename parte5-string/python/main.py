from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
#url = ""

print(ExtratorArgumentosUrl.is_valid_url(url))
