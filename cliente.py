class Cliente:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf 
        self.__salario = salario
        self.__financiamento = []
        
    
    #Metodos de Acessos
    @property
    def nome_cliente(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def salario(self):
        return self.__salario
    
    @property
    def financiamento(self):
        return self.__financiamento
    
    
    #Metodos de Alteração
    @nome_cliente.setter
    def nome_cliente (self, novo_nome):
        self.__nome = novo_nome
    
    @cpf.setter
    def cpf (self, novo_cpf):
        self.__cpf = novo_cpf
    
    @salario.setter
    def salario (self, novo_salario):
        self.__salario = novo_salario

    def adicionar_financiamento(self, valor):
        self.__financiamento.append(valor)
    
     
    def total_financiamento(self):
        soma = 0
        for i in range(len(self.__financiamento)):
            soma += self.__financiamento[i]
        return soma
            
    


