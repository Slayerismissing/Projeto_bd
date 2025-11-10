from config.db import criar_conexao

conn = criar_conexao()

if conn:
    conn.close()