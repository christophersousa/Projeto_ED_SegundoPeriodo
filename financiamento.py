class Financiamento:
    def __init__(self, cliente, imovel, banco, valor_f):
        self.__cliente = cliente
        self.__imovel = imovel
        self.__banco = banco
        self.__valor_financiamento = valor_f
        self.__num_aport = 0

    #Metodos de Acesso
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def imovel(self):
        return self.__imovel

    @property
    def banco(self):
        return self.__banco
    
    @property
    def valor_financiamento(self):
        return self.__valor_financiamento
    
    @property
    def num_aport(self):
        return self.__num_aport
    
    #Metodos de Alteração

    @valor_financiamento.setter
    def valor_financiamento(self, novo_valor):
        self.__valor_financiamento = novo_valor
    
    @num_aport.setter
    def num_aport(self, novo_num):
        self.__num_aport = novo_num
    

    def receber_aporte(self, valor):
        valor_num = valor
        if  valor_num <= self.__valor_financiamento :
            self.__valor_financiamento -= valor_num
            self.__num_aport = valor_num
    
