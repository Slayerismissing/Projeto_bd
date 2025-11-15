import services.service_equipe as service_equipe
import os

#Interface principal de equipes
def interface_equipes():
    os.system('cls')
    while True:
        print('---Interface de Equipes---')
        print('1 - Inserir equipe')
        print('2 - Deletar equipe')
        print('3 - Atualizar equipe')
        print('4 - Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            interface_inserir_equipe()
        elif opcao == '2':
            interface_deletar_equipe()
        elif opcao == '3':
            interface_update_equipe()
        elif opcao == '4':
            break
        else:
            print('Opção inválida. Tente novamente.')


#Interface para inserir equipes
def interface_inserir_equipe():
    os.system('cls')
    nome_equipe = input('Qual será o nome da equipe: ')
    regiao = input('Qual a região de vocês: ')

    #Não pode mais de 10 pessoas na equipe
    while True:
        try:
            quant_integrantes = int(input('Quantos serão da equipe?: '))
            if quant_integrantes > 10:
                print('Não pode mais de 10 pessoas na equipe')
                continue
            break
        except ValueError:
            print('Por favor, insira um número válido.')
    
    #Se tiver líder, pedir o nome do líder
    while True:
        opcao_lider = input('O time tem líder? \n 1-Sim ou 2-Não?: ')
        if opcao_lider == '1' or opcao_lider == '2':
            lider = opcao_lider == '1'
            if lider:
                nome_lider = input('Qual o nome do líder: ')
            else:
                nome_lider = None
            retorno_inserir = service_equipe.inserir_equipe(nome_equipe, regiao, quant_integrantes, lider, nome_lider)
            print(retorno_inserir)
            break
        else:
            print('Opção inválida. Insira 1 para sim ou 2 para não')


#Deletar a equipe
def interface_deletar_equipe():
    id_equipes = ''
    while id_equipes != 'exit':
        print('---Deletar Equipe---')
        print('Digite exit para voltar ao menu anterior')
        equipes = service_equipe.ler_equipes()

        id_equipes_validos = []
        print('Equipes disponíveis:')
        for equipe in equipes:
            #Resgata todos os ids para validação
            id_equipes_validos.append(equipe[0])
            print(f'id: {equipe[0]}\tNome: {equipe[1]}\tRegião: {equipe[2]}\tIntegrantes: {equipe[3]}\tLíder: {equipe[4]}\tNome Líder: {equipe[5]}')
        id_equipes = input('Digite o id do time que quer tirar: ')

        #Garantir que o id seja um inteiro
        try:
            id_equipes_int = int(id_equipes)
        except ValueError:
            print("ID inválido. Por favor, insira um número inteiro.")
            continue
    
        #Garantir que o id exista
        if id_equipes_int not in id_equipes_validos:
            print("ID não encontrado. Por favor, insira um ID válido.")
            continue

        service_equipe.deletar_equipe(id_equipes_int)

        equipes = service_equipe.ler_equipes()
        print('\nTabela após exclusão:')
        for i in equipes:
            print(i)


#Dar update na equipe
def interface_update_equipe():
    pass