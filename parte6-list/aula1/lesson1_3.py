idades = [39, 18, 15, 27]

# print (28 in idades)
# print(15 in idades)

if 15 in idades:
    idades.remove(15)

if 28 in idades:
    idades.remove(28)

idades.append(19)
idades.insert(0, 20)

idades = [20, 39, 18]
idades.extend([27, 19])

'''
idades_no_ano_que_vem = []


for idade in idades:
    # print("Recebi o elemento ", elemento)
    # print(idade + 1)
    idades_no_ano_que_vem.append(idade + 1)
'''

def proximo_ano(idade):
    return idade + 1

idades_no_ano_que_vem = [proximo_ano(idade) for idade in idades]

print(idades_no_ano_que_vem)
print([idade for idade in idades if idade > 21])
print(idades)

