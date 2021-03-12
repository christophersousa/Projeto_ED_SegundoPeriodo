class Imovel:
    def __init__(self, tipo, valor, codigo):
        self.__tipo = tipo
        self.__valor = valor
        self.__codigo = codigo
        self.__total_financiamento = []
        self.__juros = 0
        self.__prazos = []


    # Get Metodo de Acesso.
    @property
    def tipo(self):
        return self.__tipo

    @property
    def valor(self):
        return self.__valor

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def valor_financiamento(self):
        return self.__total_financiamento
    
    @property
    def juros(self):
        return self.__juros
    
    @property
    def prazo(self):
        return self.__prazos

    # Set Metodo de Alteração
    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    def Financiamento_imovel(self, prazo):

        if self.__valor <= 500000:

            t = prazo #O prazo em anos
            i = 7/100 # 10% ao ano
            c = self.__valor # valor do imovel
            j = c*i*t # gerar juros
            total = j + c
            self.__total_financiamento.append(total)
            self.__juros = j
        else:
            t = prazo #O prazo em anos
            i = 8/100 # 10% ao ano
            c = self.__valor # valor do imovel
            j = c*i*t # gerar juros
            total = j + c
            self.__total_financiamento.append(total)
            self.__juros = j
        return j + c
    
    def Mensal (self, valor, prazo):
        mes = prazo * 12
        self.__prazos.append(mes)
        return valor / mes 



        