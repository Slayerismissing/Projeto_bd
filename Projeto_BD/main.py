from db import criar_conexao
import interfaces.equipes_interface as interface_equipes
import os

conn = criar_conexao()

#todo: separar as interfaces do main
while True:
    os.system('cls')
    opcao = input('Digite o que deseja modificar: \n 1- Equipes \n 2- Jogadores \n 3- Sair \n') 
    if opcao == '1':
        interface_equipes.interface_equipes()
    elif opcao == '2':
        continue # todo: interface_jogadores.interface_jogadores()
    elif opcao == '3':
        break
    else:
        print('Opção inválida. Tente novamente.')
if conn:
    conn.close()