from db import criar_conexao
import interfaces.equipes_interface as interface_equipes

conn = criar_conexao()

#todo: separar as interfaces do main
while True:
    opcao = input('Digite a opção desejada: 1- Inserir equipe, 2- Deletar equipe, 3-') 
    if opcao == '1':
        interface_equipes.interface_inserir_equipe()
    elif opcao == '2':
        interface_equipes.interface_deletar_equipe()
    elif opcao == '3':
        break
    else:
        print('Opção inválida. Tente novamente.')
if conn:
    conn.close()