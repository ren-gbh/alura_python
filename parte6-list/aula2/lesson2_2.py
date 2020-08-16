from contaCorrente import ContaCorrente

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
# print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
# print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
conta_do_gui.deposita(100)
print(contas[0])
print(conta_do_gui)
print(contas[2])

contas[2].deposita(300)
print(conta_do_gui)