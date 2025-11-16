from db import criar_conexao
import interfaces.equipes_interface as interface_equipes
import interfaces.usuarios_interface as interface_usuario
import os

conn = criar_conexao()

#todo: separar as interfaces do main
while True:
    
    os.system('cls')
    logado = False
    while not logado:
        logado = interface_usuario.tela_de_autenticacao()

    print('\n ---Menu Principal---')

    opcao = input('Digite o que deseja modificar: \n 1- Torneios \n 2- Equipes \n 3- Jogadores \n 4- Sair \n') 
    if opcao == '1':
        # todo: interface_torneios.interface_torneios()
        continue
    elif opcao == '2':
        interface_equipes.interface_equipes()
    elif opcao == '3':
        continue # todo: interface_jogadores.interface_jogadores()
    elif opcao == '4':
        break
    else:
        print('Opção inválida. Tente novamente.')
if conn:
    conn.close()