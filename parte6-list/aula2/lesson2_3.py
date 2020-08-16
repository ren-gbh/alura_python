from contaCorrente import ContaCorrente

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(900)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
# print(contas[0], contas[1])
# deposita_para_todas(contas)
# print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])
# deposita_para_todas(contas)

guilherme = ('Guilherme', 37, 1981) #tupla
daniela = ('Daniela', 31, 1987)
# guilherme.append(6754)

conta_do_gui = (15, 1000)
conta_do_gui[1]
# conta_do_gui[1] += 100

def deposita(conta): #variacao "funcional" (separando o comportamento dos dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

deposita(conta_do_gui)
conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)
