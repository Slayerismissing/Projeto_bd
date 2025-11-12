from db import criar_conexao
import os 

def delete_equipe(id_equipe):
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'DELETE FROM equipes WHERE id_equipe=%s'
    try:
       cursor.execute(query, [id_equipe])
       conn.commit
       print(f'Equipe com ID {id_equipe} removida com sucesso!')
       return True
    except Exception as e:
        conn.rollback()
        print(f'Erro ao deletar: {e}')
        return False
    finally:
        conn.close()

def update_equipe(nome, id_equipe, regiao) :
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'UPDATE equipe SET nome=%s AND regiao=%s WHERE id_equipe=%s'
    return cursor.execute(query, [nome, regiao, id_equipe])

def tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'SELECT * FROM equipes e'
    conn.commit()
    cursor.execute(query)
    return cursor.fetchall()


os.system('cls')

equipes = tabela()
print('ID;\tNome\tRegião;\tInte:\tLíder;\tNome Líder;')
for i in equipes:
    print(i)




id_equipes = input('Digite o id do time que quer tirar: ')

id_equipes_int = int(id_equipes)

deletar = delete_equipe(id_equipes_int)









equipes = tabela()
print('\nTabela após exclusão:')
for i in equipes:
    print(i)



