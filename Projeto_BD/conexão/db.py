import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname= 'aula',
            user='postgres',
            password='jdkljdkl@kblc2006',
            host='localhost',
            port='5432'
        )
        print('Conexão realizada com sucesso!')
        return conn
    except Exception as e:
        print(f'Erro de conexão: {e}')
        return None