from db import criar_conexao

def delete_equipe(id_equipe):
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'DELETE FROM equipes WHERE id_equipe=%s'
    return cursor.execute(query, [id_equipe])

def update_equipe(nome, id_equipe, regiao) :
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'UPDATE equipe SET nome=%s AND regiao=%s WHERE id_equipe=%s'
    return cursor.execute(query, [nome, regiao, id_equipe])

for 


