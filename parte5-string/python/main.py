# from extratorArgumentosUrl import ExtratorArgumentosUrl
import re

'''
url = "https://bitebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"

argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor = argumentos_url.extrai_valor()
print(moeda_destino, moeda_origem,valor)
'''

padrao = "[0123456789][0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]"

email1 = "Meu número é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é meu celular"
email4 = "HUEHUEHUE 93543-1254 hhdsauhduaishiduasha"

retorno = re.search(padrao, email4)
print(retorno)
print(retorno.group())
