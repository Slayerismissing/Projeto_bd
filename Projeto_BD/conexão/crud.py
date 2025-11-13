from db import criar_conexao

# Deletar equipes
def delete_equipe(id_equipe):
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'DELETE FROM equipes WHERE id_equipe = %s'
    cursor.execute(query, [id_equipe])
    if cursor.rowcount == 0:
        print(f'Nenhuma equipe encontrada com ID {id_equipe}')
        conn.rollback()
        conn.close()
        return False
    conn.commit()
    print(f'Equipe com ID {id_equipe} removida com sucesso!')
    conn.close()
    return True
        
       

# att as esquipes
def update_equipe(nome, regiao, lider, nome_lider, id_equipe) :
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'UPDATE equipes SET nome=%s, regiao=%s, lider=%s, nome_lider=%s WHERE id_equipe=%s'
    try:
        cursor.execute(query, [nome, regiao, lider, nome_lider, id_equipe])
        conn.commit()
        print(f'Equipe {id_equipe} atualizada com sucesso!')
        return True
    except Exception as e:
        conn.rollback()
        print(f'Erro ao atualizar: {e}')
        return False
    finally:
        conn.close()

# Usar para mostrar a tebla no for
def tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'SELECT * FROM equipes e'
    cursor.execute(query)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# Se caso não houver equipes
def mostrar_tabela(equipes):
    if not equipes:
        print("\nNenhuma equipe encontrada.")
        return


equipes = tabela()
for i in equipes:
    print(i)

id_equipes = int(input('Digite o id do time que quer tirar: '))

deletar = delete_equipe(id_equipes)

equipes = tabela()
print('\nTabela após exclusão:')
for i in equipes:
    print(i)



