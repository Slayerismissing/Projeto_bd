from db import criar_conexao        

#Deletar "FEITO" > Arrumar 
def deletar_equipe(id_equipe):
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'DELETE FROM equipes WHERE id_equipe=%s'
    try:
       cursor.execute(query, [id_equipe])
       conn.commit()
       print(f'Equipe com ID {id_equipe} removida com sucesso!')
       return True
    except Exception as e:
        conn.rollback()
        print(f'Erro ao deletar: {e}')
        return False
    finally:
        conn.close()


#update "FAZER"
def update_equipe(nome, id_equipe, regiao) :
    conn = criar_conexao()
    cursor = conn.cursor()
    query = 'UPDATE equipes SET nome=%s, regiao=%s WHERE id_equipe=%s'
    cursor.execute(query, [nome, regiao, id_equipe])
    conn.commit()
    conn.close()


#inserir "FEITO"
def inserir_equipe(nome, regiao, quantidade_integrantes, lider, nome_lider):

    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO equipes(nome, regiao, quant_integrantes, lider, nome_lider) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(query, (nome, regiao, quantidade_integrantes, lider, nome_lider))
        conn.commit()
        print('Dados de equipes inserido com sucesso!')
    except Exception as e:
        print(f'Erro ao inserir equipe: {e}')
    finally:
        cursor.close()
        conn.close()


#Tabela mostrar "FEITO"
def ler_equipes(id_equipe=None):
    conn = criar_conexao()
    cursor = conn.cursor()
    if id_equipe:
        query = 'SELECT * FROM equipes e WHERE e.id_equipe=%s'
        cursor.execute(query, [id_equipe])
        conn.commit()
        return cursor.fetchall()
    else:
        query = 'SELECT * FROM equipes e'
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()

