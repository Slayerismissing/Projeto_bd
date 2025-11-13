from db import criar_conexao

#Inserir as equipes no banco de dados(Conexão)
def inserir_usuario(nome, regiao, quantidade_integrantes, lider='', nome_lider=''):

    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO equipes(nome, regiao, quant_integrantes, lider, nome_lider) VALUES (%s, %s, %s, %s, %s)'
        if quantidade_integrantes > 10:
            return 'Não pode mais de 10 pessoas na equipe'
        if lider == 'sim':
            True
        else:
            pass
        cursor.execute(query, (nome, regiao, quantidade_integrantes, lider, nome_lider))
        conn.commit()
        print('Dados de equipes inserido com sucesso!')
    except Exception as e:
        print(f'Erro ao inserir equipe: {e}')
    finally:
        cursor.close()
        conn.close()


#inserir as equipes no VsCode pra fazer a conexão com o banco de dados
nome_equipe = input('Qual será o nome da equipe: ')
regiao = input('Qual a região de vocês: ')
quant_integrantes = int(input('Quantos serão da equipe?: '))
lider = input('O time já tem um líder? Sim ou Não?: ').lower()

if lider.endswith('sim'):
   nome_lider = input('dê o nome do líder: ')
   informacoes = inserir_usuario(nome_equipe, regiao, quant_integrantes, lider, nome_lider)
   print(informacoes)
else:
    print('Não foi dado um nome de líder')
    informacoes = inserir_usuario(nome_equipe, regiao, quant_integrantes)
    print(informacoes)

