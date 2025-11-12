from db import criar_conexao

def inserir_usuario(nome, regiao, quantidade_integrantes):

    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO equipes(nome, regiao, quant_integrantes) VALUES (%s, %s, %s)'
        if quantidade_integrantes > 10:
            return 'Não pode mais de 10 pessoas na equipe'
        cursor.execute(query, (nome, regiao, quantidade_integrantes))
        conn.commit()
        print('Dados de equipes inserido com sucesso!')
    except Exception as e:
        print(f'Erro ao inserir equipe: {e}')
    finally:
        cursor.close()
        conn.close()

nome_equipe = input('Qual será o nome da equipe: ')

regiao = input('Qual a região de vocês: ')

quant_integrantes = int(input('Quantos serão da equipe?: '))

informacoes = inserir_usuario(nome_equipe, regiao, quant_integrantes)

print(informacoes)