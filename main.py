import random # Acesso ao "random".
from procurar import Procurar_cliente # Acesso ao arquivo "procurar", acesso a class "Procurar_cliente".
from procurar import Procurar_outra # Acesso ao arquivo "procurar", acesso a class "Procurar_outro".
from procurar import Procura_cpf # Acesso ao arquivo "procurar", acesso a class "Procurar_cpf".
from procurar import Procurar_identificador_imv # Acesso ao arquivo "procurar", acessando a class "Procurar_identificador_imv".
from cliente import Cliente # Acesso ao arquivo "cliente", acesso a class "Cliente".
from conta import Conta # Acesso ao arquivo "conta", acesso a class "Conta".
from banco import Banco # Acesso ao arquivo "banco", acesso a class "Banco".
from financiamento import Financiamento # Acesso ao arquivo "financiamento", acesso a class "Financiamento".
from imovel import Imovel # Acesso ao arquivo "imovel", acesso a class "Imovel".

clientes = [] # Espaço reservado para "clientes".
contas = [] # Espaço reservado para "contas".
imoveis = [] # Espaço reservado para "imoveis".
financiamentos = [] # Espaço reservado para "financiamentos".

# Cadastro declientes.
"""print()
print('*'*46)
print('Cadastrar clientes.\nPara finalizar o cadastro digite "Finalizar".') # Informação de cadastro e como sair depois do cadastro.
print('*'*46)
# Loop para o cadastro dos clientes.
while True:
    nome = input('\nNome: ').title() # Entrada do "Nome" do cliente.

    if nome == 'Finalizar' or nome == 'Sair' or nome == 'finalizar' or nome == 'sair': # Condição para sair do cadastro de cliente digitando ".
        break 

    cpf = input('Informe o CPF: ') # Entrada do "CPF" do cliente.
    salario = int(input('Salario: ')) # Entrada do "Salário" do cliente. 
    saldo = int(input('Saldo atual na conta: ')) # Entrada do "Saldo" do cliente.
    N_banco = 'Caixa' # Novo atributo "Nome do Banco" (Poderar ser solicitado para que seja cadastrado se necessário).
    agencia = random.randint(1000,9999) # Entrada da "Identificação da Agência" de forma aleatória realizada pelo "Import random" entre os intervalos de "1000 a 9999".
    Id = random.randint(10,99) # Entrada da "Identificação da Agência" de forma aleatória realizada pelo "Import random" entre os intervalos de "10 a 99".

    #Validar o CPF. 

    ident_cpf = Procura_cpf(cpf, clientes) # Uso do método "Procura_cpf", para verificar se o "CPF" cadastrado já existe.
    if cpf == ident_cpf: # Condição para a verificação.
        print()
        print('-'*20)
        print('CPF já cadastrado!!') # Mensagem de "CPF" existente.
        print('-'*20)
        continue # Informação para o programsa seguir para o próximo passo.

    #Emitir lista de clientes

    cliente_agencia = Cliente(nome, cpf, salario) # Formatação do array do "cliente_agencia" com "Nome, CPF e Salário".
    clientes.append(cliente_agencia) # Condição para alimentar as informações do tipo fila no novo atributo "cliente_agencia".

    #Emitir lista de contas dos clientes 
    conta_agencia = Conta(cliente_agencia, Id, saldo) # Formatação do array da "conta_agencia" com "cliente_agencia, Id da Conta e Saldo".
    contas.append(conta_agencia) # Condição para alimentar as informações do tipo fila no novo atributo "conta_agencia".
    

    print('Banco {}, agencia {}'.format(banco, agencia)) # Impressão das informações de "Bancoe Agência".
    print('O Id da conta do cliente será: {}'.format(Id))""" # Impressão da "Identificação" do cliente.

# Cadastro de "Clientes" para teste.
# Entrada dos dados do primeiro Cliente para teste.
nome = 'Christopher' # Entrada do "Nome" do cliente 1.
cpf = '150.456.893-09' # Entrada do "CPF" do cliente 1.
salario = 1500 # Entrada do "Salário" do cliente 1.
saldo = 2500 # Entrada do "Saldo" do cliente 1.
Id = random.randint(10,99) # Gerando o "Id" do cliente 1 de forma aleatória pelo método "import random" entre os intervalos de "10 a 99".

# Gerar lista do primeiro cliente para teste.
cliente_1 = Cliente(nome, cpf, salario) # Formatação do array do "cliente_1" com "Nome, CPF e Salário".
clientes.append(cliente_1) # Condição para alimentar as informações do tipo fila no novo atributo "cliente_1".

# Gerar lista da conta do primeiro cliente para teste.
conta_1 = Conta(cliente_1, Id, saldo) # Formatação do array do "conta_1" com "Informações do cliente, Id da conta e Saldo".
contas.append(conta_1) # Condição para alimentar as informações do tipo fila no novo atributo "conta_1".

# Entrada dos dados do segundo Cliente para teste.
nome = 'Renato' # Entrada do "Nome" do cliente 2.
cpf = '240.768.652-77' # Entrada do "CPF" do cliente 2.
salario = 2000 # Entrada do "Salário" do cliente 2.
saldo = 5000 # Entrada do "Saldo" do cliente 2.
Id = random.randint(10,99) # Gerando o "Id" do cliente 2 de forma aleatória pelo método "import random" entre os intervalos de "10 a 99".

# Gerar lista do segundo cliente para teste.
cliente_2 = Cliente(nome, cpf, salario) # Formatação do array do "cliente_2" com "Nome, CPF e Salário".
clientes.append(cliente_2) # Condição para alimentar as informações do tipo fila no novo atributo "cliente_2.

# Gerar lista da conta do segundo cliente para teste.
conta_2 = Conta(cliente_2, Id, saldo) # Formatação do array do "conta_2" com "Informações do cliente, Id da conta e Saldo".
contas.append(conta_2) # Condição para alimentar as informações do tipo fila no novo atributo "conta_2".

# Entrada dos dados do terceito Cliente para teste.
nome = 'Thiago' # Entrada do "Nome" do cliente 3.
cpf = '856.194.527-24' # Entrada do "CPF" do cliente 3.
salario = 10000 # Entrada do "Salário" do cliente 3.
saldo = 50000 # Entrada do "Saldo" do cliente 3.
Id = random.randint(10,99) # Gerando o "Id" do cliente 3 de forma aleatória pelo método "import random" entre os intervalos de "10 a 99".

# Gerar lista do terceiro cliente para teste.
cliente_3 = Cliente(nome, cpf, salario) # Formatação do array do "cliente_3" com "Nome, CPF e Salário".
clientes.append(cliente_3) # Condição para alimentar as informações do tipo fila no novo atributo "cliente_3.

# Gerar lista da conta do terceiro cliente para teste.
conta_3 = Conta(cliente_3, Id, saldo) # Formatação do array do "conta_3" com "Informações do cliente, Id da conta e Saldo".
contas.append(conta_3) # Condição para alimentar as informações do tipo fila no novo atributo "conta_3".

# Inicio das operações.
print('\nVamos começar nossas operações') # Informando ao usuário que as operações será iniciada.

banco = Banco("CAIXA", contas, financiamentos) # Novo atributo "banco" com a formatação "Nome do Banco (default "CAIXA"), Contas da Agência e Financiamentos"

ind = None # Start do atributo "ind".
# Loop para entrada nos "Menus das Transações".
while True:
    # Formatação do "Menu Principal".
    operações = '\nOpção 1 = Entrar na conta \nOpção 2 = Sistema bancario \nDigite a operação escolhida: ' 
    
    c = int(input(operações)) # Apresentando o "Menu Principal" para que seja feita a escolha entre "Opção 1 ou 2".

    if c == 1: # Se escolhida a "Opção 1" o programa entra aqui.

        name_user = input('\nDigite seu nome: ').title() # Entrada do "Nome" do Cliente.
        cpf_user = input('Informe o CPF: ') # Entrada do "CPF" do Cliente.
        ind = Procurar_cliente(cpf_user, name_user, clientes) # Se "Nome e CPF" estiver corretos, será procurada a "Id do Cliente".

        if name_user == clientes[ind].nome_cliente and cpf_user == clientes[ind].cpf: # Se os dados apresentados forem corretos, será mostrado o "Menu das Transações".
            while True:
                # Formatação do "Menu das Transações".
                menu = '\nOpção 1 = Saldo Atual \nOpção 2 = Sacar \nOpção 3 = Depositar \nOpção 4 = Transferência \nOpção 5 = Financiamento de imoveis \nOpção 6 = Log Off \nDigite sua opção: '
                acao = int(input(menu)) # Apresentando o "Menu Principal" para que seja feita a escolha entre "Opção 1, 2, 3, 4, 5 ou 6".

                if acao == 1: # Se "Opção 1" for escolhida, poderár ver o "Saldo da Conta".
                    print('\nSaldo atual: {}'.format(contas[ind].saldo)) # Impressão do "Saldo da Conta" do cliente.
                
                elif acao == 2: # Se "Opção 2" for escolhida poderá realizar "Saque".
                    
                    valor = float(input('\nValor: ')) # Entrada do "Valor do Saque".
                    print(contas[ind].sacar(valor)) # Impressão do "Valor do Saque" e diminue o "Valor do Saque" pelo método "Sacar".
                    print('Saldo atualizado: {}'.format(contas[ind].saldo)) #Impressão do "Saldo" atualizado da conta.
                
                elif acao == 3: # Se "Opção 3" for escolhida poderá realizar um "Deposito".
  
                    valor = float(input('\nValor: ')) # Entrada do "Valor do Deposito".
                    contas[ind].creditar(valor) # Adição do "Valor do Deposito" no "Saldo da Conta" pelo método "Creditar".
                    print('Saldo atualizado: {}'.format(contas[ind].saldo)) # Impressão do "Saldo da Conta" atualizado.
                
                elif acao == 4: # Se "Opção 4" for escolhida poderar realizar uma "Transferência entre Contas".
 
                    outra_conta = input('\nDigite o CPF do titular da outra conta: ') # Entrada do "CPF" da conta que será realizado a transferência.
                    ind_cont = Procurar_outra(outra_conta, clientes) # Novo atributo para procurar a outra conta pelo "CPF" informado.
                    valor = float(input('\nValor: ')) # Entrada do valor a ser transferido.
                    contas[ind].transferencia( contas[ind_cont], valor) # Verifica se tem "Saldo" para a transferência pelo método "Transferencia".
                    print('Saldo atualizado: {}'.format(contas[ind].saldo)) # Impressão do "Saldo Atualizado" com o valor descontado da transferência.
                    print('Nome:{}\nRecebeu:R$ {}'.format(contas[ind_cont].cliente.nome_cliente, valor)) # Impressão do "Nome" de quem recebeu a transferência e o "Valor" recebido.


                elif acao == 5: # Se "Opção 5" for escolhida poderar realizar uma "Financiamento".

                    tipo = input('\nTipo de imovel: ').title() # Entrada do "Tipo" do financiamento.
                    valor_imv = float(input('Valor do imovel: ')) # Entrada do "Valor" do empréstimo.
                    parcelas = int(input('Prazo em anos: ')) # Entrada do "Prazo" do financiamento (OBS. valor em anos).
                    codigo_imv = random.randint(100, 1000) # Gerando o "Código do Imovel" de forma aleatória pelo método "import random" entre os intervalos de "100 a 1000".
                    imovel = Imovel(tipo, valor_imv, codigo_imv) # Novo atributo para a formatação da class "Imovel" com "Tipo, Valor e Código".
                    imoveis.append(imovel) # Condição para alimentar as informações do tipo fila no atributo "imovel". 
                    ident_imv = Procurar_identificador_imv(codigo_imv,imoveis) # Novo atributo para a procura do "Código" do imóvel.
                    result = imoveis[ident_imv].Financiamento_imovel(parcelas) # Novo atribudo para mostrar a quantidade de parcelas do financiamento.
                    print() # Formatação
                    print('-'*42) # Formatação
                    # Impressão em forma de lista do: "Tipo de Financiamento, Valor e as Parcelas".
                    print('Tipo de imovel: {} \nValor: R$ {}  \nParcelado em {} anos'.format(imoveis[ident_imv].tipo, imoveis[ident_imv].valor, parcelas))
                    print('\nO valor total do financiamento será: R$ {}'.format(result)) # Impressão do "Valor Total" do financiamento.
                    print('Valor das parcelas: R$ {}'.format(imoveis[ident_imv].Mensal(result, parcelas))) # Impressão do "Valor das Parcelas" a pagar.
                    print('-'*42) # Formatação

                    conf = input('\nDeseja efetuar o financiamento: ').upper() # Entrada da confirmação para finaliazar o financiamento.
                    if conf == 'SIM' or conf == 'YES' or conf == 'S': # Condição para confirmar o financiamento.
                        conf_name = input('\nNome: ').title() # Entrada do "Nome" para vonfirmar o financiamento
                        conf_cpf = input('CPF: ') # Entrada do "CPF" para vonfirmar o financiamento
                        if conf_name == clientes[ind].nome_cliente and conf_cpf == clientes[ind].cpf: # Validação do "Nome" e "CPF" para finalizar o financiamento.
                            financiamento = Financiamento(clientes[ind], imoveis[ident_imv], banco, result) # Gera o resultado dio financiamento.
                            financiamento.receber_aporte(imoveis[ident_imv].juros) # Será realizado o calculo do valor dos "Juros".
                            financiamentos.append(financiamento) # Armazenamento do financiamento no array do "Financiamento" com o tipo fila.
                            clientes[ind].adicionar_financiamento(result) # Armazenamento do "Valor" no array do "Financiamento" com o tipo fila.                   
                            print('\nFinanciamento realizado') # Impressão de que o "Financiamento" foi realizado com sucesso.
                            
                        else: # Se algum dado não estiver correto, o programa vem para este ponto.
                            print('Cpf ou Nome Invalido!!') # Impressão de mensagem de erro para o "Cliente".
                            continue # Ocorre o retorno para "Opção 5".

                    else: # Condição se o "Cliente" não confirmar o financimanto.
                        print('Operação cancelada!') # Impressão de mensagem de cancelamento para o "Cliente".
                        imoveis.pop() # Será descartado os dados se o "Cliente" não confirmar o financiamento.

                elif acao == 6: # Se "Opção 6" sai do "Menu das Transações".
                    break # "Menu das Transações" sai do loop.

        else: # Se os dados informados não forem encontrados na busca o programa volta ao início.
            print('Nome ou Cpf invalido') # O cliente é informado que os dados informados não estão corretos. 
            continue # O programa volta para o "Menu Pincipal".   
             
    elif c == 2: # Se "Opção 2" poderar entrar no "Sistema Bancário".
        print('Seja bem vindo ao sistema bancario') # Impressão da mensagem de "Boas Vindas".
        # Formatação do  "Menu do Sistema Bancário" para a escolha da opção "1 ou 2".
        banco_operation = int(input('\nOpção 1 = Financiamentos dos clientes \nOpção 2 = Contas dos clientes \nDigite a operação escolhida: '))

        if banco_operation == 1: # Se "Opção 1" poderar entrar no "Sistema Bancário".
            while True:
                print('Para acessar o Sistema financeiro digite: \nPara sair digite "Finalizar"') # Impressão de mensagem para que operação o "Cliente" deseja realizar.
                name_cliente = input('\nNome do cliente: ').title() # Entrada do "Nome" do cliente.

                if name_cliente == 'Finalizar' or name_cliente == 'Sair': # Condição para sar do "Menu".
                    break # "Menu do Sistema Bancário" sai do loop.

                cpf_cliente = input('CPF: ') # Entrada do "CPF" do cliente.

                ind = Procurar_cliente(cpf_cliente, name_cliente, clientes) # Procura se o "Nome" do cliente faz parte da lista de clientes.
                ind_cpf = Procura_cpf(cpf_cliente, clientes) # Procura se o "CPF" do cliente existe no "Banco".

                if name_cliente == clientes[ind].nome_cliente and cpf_cliente == clientes[ind].cpf: # Condição para validação do "Nome e CPF" do cliente.
                    print('Resultado') # Impressão do resultado.
                    print('\nNome do cliente: {}'.format(clientes[ind].nome_cliente)) # Após validação será exibido o "Nome" do cliente.
                    print('CPF: {}'.format(clientes[ind].cpf)) # Após validação será exibido o "CPF" do cliente.
                    print('Id da conta: {}'.format(contas[ind].identificador)) # Após validação será exibido o "ID" do cliente.
                    print('\nValor total do financiamentos: {}'.format(clientes[ind].total_financiamento())) # Após validação será exibido o "Valor Total de Financiamento" do cliente.
                    print(banco.financiamentos_cliente(ind_cpf)) # Impressão Do financiamento do cliente.

                else:
                    print('Nome ou Cpf invalido!!') # Impressão de mensagemde erro se algum dado não for validado.
                    continue # O programa volta para o "Menu Sistema Bancário". 


        else:
            # Formatação do  "Menu Sistema Bancário do Cliente " para a escolha da opção "1 ou 2".
            banco_clientes = int(input('\nOpção 1 = Conta cliente \nOpção 2 = Valor acumulado \nDigite a operação escolhida: '))

            if banco_clientes == 1: # Se "Opção 1" poderar "Consultar" dados do cliente.
                print('\nBem vindo ao Sistema bancario do cliente:"') # Impressão da mensagem de "Boas Vindas".

                n_cliente = input('\nNome do cliente: ').title() # Entrada do "Nome" do cliente.

                if n_cliente == 'Finalizar' or n_cliente == 'Sair': # Condição para sar do "Menu".
                    break # "Menu Sistema Bancário do Cliente" sai do loop.

                c_cliente = input('CPF: ') # Entrada do "CPF" do cliente.
                ind = Procurar_cliente(c_cliente, n_cliente, clientes) # Verifica se o "CPF" informado é cadastrado.
                if n_cliente == clientes[ind].nome_cliente and c_cliente == clientes[ind].cpf: # Condição se o "CPF" fora encontrado.
                    print() # Formatação.
                    print('-'*25) # Formatação.
                    print('Resultado') # Formatação.
                    print('\nNome do cliente: {}'.format(contas[ind].cliente.nome_cliente)) # Impressão do "Nome do Cliente".
                    print('CPF: {}'.format(contas[ind].cliente.cpf)) # Impressão do "CPF do Cliente".
                    print('Id da conta: {}'.format(contas[ind].identificador)) # Impressão do "ID do Cliente".
                    print('Saldo atual: {}'.format(contas[ind].saldo)) # Impressão do "Saldo do Cliente".
                    print('-'*25) # Formatação.
            
            elif  banco_clientes == 2: # Se "Opção 2" poderar "Consultar" o "Salto" de todos os clientes do "Banco".
                print('O valor acumulado de todas contas cadastradas no banco é: ') # Impressão da mensagem do "Saldo do Banco".                
                print(f'\nR$ {banco.total_valor_contas()} ') # Impressão do "Valor Total" do "Saldo" de todos os clientes.              

                    


                
    
    

    


    
        

    