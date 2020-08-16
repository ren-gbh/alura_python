from contaCorrente import ContaCorrente

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(('Paulo', 39, 1979))
print(usuarios)
print(usuarios[0])

# usuarios[0][0] = 'Guilherme Silveira'

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)
#print(contas)

for conta in contas:
    print(conta)

#conta.append(5344534)

contas[0].deposita(300)

for conta in contas:
    print(conta)