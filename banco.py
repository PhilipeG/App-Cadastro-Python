import sqlite3

class Database:
    def __init__(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS vacinacao(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME_PACIENTE TEXT,CPF TEXT,DT_NASCIMENTO TEXT,RESP_APLIC TEXT)''')
            self.conn.commit()
        except Exception as e:
            print(f'Erro na criação da tabela: {e}')

    def leitura(self):
        try:
            self.cursor.execute('SELECT ID, NOME_PACIENTE, CPF, DT_NASCIMENTO, RESP_APLIC FROM vacinacao')
            item = self.cursor.fetchall()
            for linha in item:
                print(linha)        
        except sqlite3.Error as e:
            print('Erro ao buscar o Paciente: ', e)

    def cadastro(self,NOME_PACIENTE, CPF, DT_NASCIMENTO, RESP_APLIC):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO vacinacao (NOME_PACIENTE, CPF, DT_NASCIMENTO, RESP_APLIC) VALUES (?, ?, ?, ?)', (NOME_PACIENTE, CPF, DT_NASCIMENTO, RESP_APLIC ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Erro ao cadastrar O Paciente: {e}')
        finally:
            if cursor:
                cursor.close()

    def remover(self, ID):
        try:
            cursor = self.conn.cursor()
            self.cursor.execute('DELETE FROM vacinacao WHERE ID = ?', (ID ))
            self.conn.commit()
            self.conn.execute('VACUUM')
        except sqlite3.Error as e:
            print(f'Erro ao remover o Paciente: {e}')
        finally:
            if cursor:
                cursor.close()

    def alterar(self, NOME_PACIENTE, CPF, DT_NASCIMENTO ):
        try:
            cursor = self.conn.cursor()
            alterar_query = 'UPDATE vacinacao set NOME = ?, CPF = ?, DT_NASCIMENTO= ?, WHERE id_aluno = ?'
            self.cursor.execute(alterar_query, (NOME_PACIENTE, CPF, DT_NASCIMENTO))
            self.conn.commit()
            print('Atualizado com sucesso!')
        except sqlite3.Error as e:
            print(f'Erro ao alterar o Paciente: {e}')
        finally:
            if cursor:
                cursor.close()

    def __def__(self):
        self.conn.close()


if __name__ == '__main__':
    print("teste")
    db = Database('vacinacao.db')

    db.cadastro('Karl Franz', 8, 0, "JOAO")

    print('\n-----Lista alunos----')
    db.leitura()

    db.remover(1)

    print('\n-----Lista alunos apos remoção----')
    db.leitura()

    db.alterar(2, 'Tyron', 8.5)

    print('\n-----Lista alunos apos alterar----')
    db.leitura()