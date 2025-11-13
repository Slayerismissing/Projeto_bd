import services.service_equipe as service_equipe
import os
os.system('cls')

#Interface para inserir equipes
def interface_inserir_equipe():
    nome_equipe = input('Qual será o nome da equipe: ')
    regiao = input('Qual a região de vocês: ')

    #Não pode mais de 10 pessoas na equipe
    while True:
        quant_integrantes = int(input('Quantos serão da equipe?: '))
        if quant_integrantes > 10:
            print('Não pode mais de 10 pessoas na equipe')
            continue
        break
    
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

def interface_deletar_equipe():
    equipes = service_equipe.tabela()
    print('ID;\tNome\tRegião;\tInte:\tLíder;\tNome Líder;')
    for i in equipes:
        print(i)

    id_equipes = input('Digite o id do time que quer tirar: ')

    id_equipes_int = int(id_equipes)

    service_equipe.deletar_equipe(id_equipes_int)

    equipes = service_equipe.tabela()
    print('\nTabela após exclusão:')
    for i in equipes:
        print(i)