class Banco:
    def __init__(self, nome_banco, contas, financiamento):
        self.__nome_banco = nome_banco
        self.__contas = contas
        self.__financiamento = financiamento
        self.__valor_totalF = 0
        self.__valor_totalA = 0

    # Get Metodo de Acesso
    @property
    def banco(self):
        return self.__nome_banco

    @property
    def contas(self):
        return self.__contas

    @property
    def financiamento(self):
        return self.__financiamento
    
    @property
    def total_valorf(self):
        return self.__valor_totalF

    @property
    def total_valorA(self):
        return self.__valor_totalA


    # Set Metodo de Alteração
    @banco.setter
    def banco(self, novo_banco):
        self.__nome_banco = novo_banco

    @contas.setter # Uso para teste
    def contas(self, nova_conta): # Uso para teste
        self.__contas = nova_conta # Uso para teste

    @financiamento.setter # Uso para teste
    def financiamento(self, novo_financiamento): # Uso para teste
        self.__financiamento = novo_financiamento # Uso para teste

    # Metodo de Uso
    def total_valor_contas(self):
        soma = 0
        for i in range(len(self.__contas)):
            soma += self.__contas[i].saldo #.saldo (Para o teste)
        return soma

    def financiamentos_cliente(self, cpf):
        tipo = []
        valor = []
        for i in range(len(self.__financiamento)):
            if cpf == self.financiamento[i].cliente.cpf:
                tipo.append(self.financiamento[i].imovel.tipo)
                valor.append(self.financiamento[i].imovel.valor)
        
        return "Tipo de financiamento respequitivamente: {} \nValor dos financiamentos respequitivamente: {}".format(tipo, valor)


               
        