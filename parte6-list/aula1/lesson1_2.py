# 6.1.2 - Introduction to collections and list

idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

'''
print(idade1)
print(idade2)
print(idade3)
print(idade4)
'''

idades = [39, 30, 27, 18]

# print(type(idades))
# print(len(idades))
# print(idades[0])

idades.append(15)

# print(idades[4])
# print(idades[5])  # Out Of Range

'''
for idade in idades:
    print(idade)
'''

idades.remove(30)
idades.append(15)
idades.remove(15)
idades.append(27)  # inclui o valor no final da lista
idades.remove(27)  # Remove o primeiro registro com esse valor da lista
print(idades)
