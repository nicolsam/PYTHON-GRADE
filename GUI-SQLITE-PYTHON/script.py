# Objetivo: Criar um gerenciador de frutas simples :)
import tkinter
import sqlite3 as sgbd

class Database():
    def __init__(self, database):
        self.database = database

    def connect(self):

        try: 
            self.connection = sgbd.connect(self.database)
            self.cursor = self.connection.cursor()

        except (Exception, sgbd.Error) as err:
            if(self.connection):
                print("Falha na conexão com o Banco de Dados: ", err)


    def select_all(self, table):
        try: 
            
            self.connect()
            self.cursor.execute(f'SELECT * FROM {table}')

            return self.cursor.fetchall()

        except sgbd.DatabaseError as err:
            print(f'Erro no Banco de Dados: {err}')
        
        finally:

            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("Conexão com Banco de dados finalizada.")
                
    def select_by_id(self, table, id):

        try:

            self.connect()
            self.cursor.execute(f'SELECT * FROM {table} WHERE id = {id}');
        
            return self.cursor.fetchone()

        except sgbd.DatabaseError as err:
            print(f'Erro no Banco de Dados: {err}')
        
        finally:

            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("Conexão com Banco de dados finalizada.")

    def insert_fruit(self, id, name, color):
        try:

            self.connect()
            self.cursor.execute('INSERT INTO frutas VALUES (?, ?, ?)', (id, name, color))

            self.connection.commit()

        except (sgbd.IntegrityError, sgbd.DatabaseError) as err:
            print(f'Erro no Banco de Dados: {err}')

        finally:

            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("Conexão com Banco de dados finalizada.")

    def update_fruit(self, id, name, color):

        try:

            self.connect()
            self.cursor.execute('UPDATE frutas SET name = ?, color = ? WHERE id = ?', (
                name, color, id
            ))

            self.connection.commit();

            

        except sgbd.DatabaseError as err:
            print(f'Erro no Banco de Dados: {err}')

        finally:

            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("Conexão com Banco de dados finalizada.")
        
        fruta = self.select_by_id('frutas', id)

        return fruta;

    def delete_fruit(self, id):

        try: 

            self.connect()
            self.cursor.execute('DELETE FROM frutas WHERE id = ?', (id,))

            print('Fruta deletada :(')

            self.connection.commit()

        except (
            Exception, 
            sgbd.IntegrityError, 
            sgbd.DatabaseError
        ) as err:
            print(f'Erro no Banco de Dados: {err}')
        
        finally:

            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("Conexão com Banco de dados finalizada.")


database = Database('frutas.db')

database.delete_fruit(4)

database.insert_fruit(4, 'Açaí', 'Preta');

frutas = database.select_all('frutas')

for fruta in frutas:
    print(fruta)

fruta = database.select_by_id('frutas', 4)
print('Fruta ID 4: ', fruta)

fruta_updated = database.update_fruit(4, 'Acerola', 'Vermelha')
print('Fruta ID 4 UPDATE: ', fruta_updated)

