import sqlite3;

print('Conectando no Banco de dados')

# Criar uma conexão com o banco de dados utilizando a função CONNECT
connection = sqlite3.connect('frutas.db')

# Utilizar a conexão para criar um cursor, que será utilizado para enviar comandos ao banco de dados
cursor = connection.cursor()

try:

    # Utilizar o cursor para enviar comandos ao banco de dados (DELETE)
    cursor.execute('DELETE FROM frutas WHERE id = 4')
    print('DELETANDO fruta COM id = 4')

    # Utilizar o cursor para enviar comandos ao banco de dados (INSERT)
    cursor.execute('INSERT INTO frutas VALUES(?, ?, ?)', (4, 'Abacate', 'Verde'))
    print('INSERINDO fruta')

    # Utilizar o cursor para enviar comandos ao banco de dados (SELECT)
    # SQLite não cria uma transação para o comando SELECT, logo não é necessário executar o commit.
    cursor.execute('''
        SELECT * FROM frutas;
    ''')

    for registro in cursor.fetchall():
        print(registro)

    # Efetivar as mudanças no banco de dados utilizando o método COMMIT da conexão
    connection.commit()
    
# Tratando erros de integridade do banco de dados
except sqlite3.IntegrityError as err:
    print('Fruta já existente') 

except sqlite3.DatabaseError as err:
    print(f'Erro no Banco de Dados: {err}')
    connection.rollback();

finally:

    if connection:
        # Fechar o cursor e a conexão
        cursor.close()
        connection.close()

