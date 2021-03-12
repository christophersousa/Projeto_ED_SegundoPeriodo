
def Procurar_cliente(cpf, nome, c):
    for i in range(len(c)):
        if cpf == c[i].cpf and nome == c[i].nome_cliente:
            return i 

def Procurar_outra (cpf, conta):
    for i in range(len(conta)):
        if cpf == conta[i].cpf :
            return i 

def Procura_cpf (cpf, conta):
    for i in range(len(conta)):
        if cpf == conta[i].cpf:
            return conta[i].cpf

def Procurar_identificador_imv (id, conta):
    for i in range(len(conta)):
        if id == conta[i].codigo:
            return i
