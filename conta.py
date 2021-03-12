class Conta:
    def __init__(self, cliente, ident, saldo):
        self.__cliente = cliente
        self.__id = ident
        self.__saldo = saldo
    
    #Metodo de Acesso
    @property
    def cliente(self):
        return self.__cliente
    @property
    def identificador (self):
        return self.__id
    
    @property
    def saldo (self):
        return self.__saldo

    #Metodo de Alteração
    @identificador.setter
    def identificador(self, novo_id):
        self.__id = novo_id
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    #Metodos de Uso
    def creditar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if (self.__saldo >= valor):
            self.__saldo -= valor
            return True
        else:
            return False
    
    def transferencia(self, outra_c, valor):
        outra_conta = outra_c
        
        if (self.__saldo >= valor):
            self.__saldo -= valor
            outra_conta.creditar(valor)
            return True

        else:
            return False


