import re

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

email1 = "Meu número é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é meu celular"
email4 = "HUEHUEHUE 935431254 dhasuidhiusahduia 98761234 hhdsauhduaishiduasha 98761234"

retorno = re.findall(padrao, email4)
print(retorno)
