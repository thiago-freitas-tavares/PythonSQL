import mysql.connector                  # lembrar de importar as bibliotecas sempre que reiniciar o arquivo no VS Code.

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1873",
    database="xidiomas_vscode"          # antes de criar o database essa linha não pode existir.
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE xidiomas_vscode")
mycursor.execute("USE xidiomas_vscode") # se o database já existe e for referenciado no mysql.connector.connect, essa linha pode ser retirada.
mycursor.execute("CREATE TABLE curso (curso_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, curso VARCHAR(45), valor DECIMAL(10, 2))")
mycursor.execute("CREATE TABLE aluno (aluno_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nome VARCHAR(45), email VARCHAR(45))")
mycursor.execute("CREATE TABLE venda (venda_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, data_venda DATE, curso_id INT, aluno_id INT)")

mycursor.execute("DESCRIBE curso")      # o cursor realiza uma query apontando para cada coluna da tabela curso.
for x in mycursor:                      # precisamos de um loop para poder visualizar todos os outputs.
    print(x)                            # outputs('nome da coluna', 'tipo de variável', 'Null: Yes or Not', 'Primary Key or Empty', 'extra: ex. auto-increment')

mycursor.execute("INSERT INTO curso (curso, valor) VALUES (%s,%s)", ('Inglês', 1200))        # não precisa incluir o id, pois ele se auto-incrementa.
mycursor.execute("INSERT INTO curso (curso, valor) VALUES (%s,%s)", ('Espanhol', 1000))
mycursor.execute("INSERT INTO curso (curso, valor) VALUES (%s,%s)", ('Francês', 900))

mycursor.execute("INSERT INTO aluno (nome, email) VALUES (%s,%s)", ('Eliane', 'eliane@gmail.com'))
mycursor.execute("INSERT INTO aluno (nome, email) VALUES (%s,%s)", ('João', 'j.123@hotmail.com'))
mycursor.execute("INSERT INTO aluno (nome, email) VALUES (%s,%s)", ('Pedro', 'pedrinho@gmail.com'))

mycursor.execute("INSERT INTO venda (data_venda, curso_id, aluno_id) VALUES (%s,%s,%s)", ('2022-01-10', 1, 1))
mycursor.execute("INSERT INTO venda (data_venda, curso_id, aluno_id) VALUES (%s,%s,%s)", ('2022-01-10', 2, 1))
mycursor.execute("INSERT INTO venda (data_venda, curso_id, aluno_id) VALUES (%s,%s,%s)", ('2022-01-10', 3, 1))
mycursor.execute("INSERT INTO venda (data_venda, curso_id, aluno_id) VALUES (%s,%s,%s)", ('2022-01-13', 1, 2))
mycursor.execute("INSERT INTO venda (data_venda, curso_id, aluno_id) VALUES (%s,%s,%s)", ('2022-01-21', 2, 3))

db.commit()                             # dados inseridos precisam ser comitados.

mycursor.execute("ALTER TABLE aluno ADD COLUMN sexo ENUM('M', 'F', '0') NOT NULL")
mycursor.execute("ALTER TABLE aluno DROP sexo")
mycursor.execute("ALTER TABLE aluno CHANGE nome first_name VARCHAR(45)")

mycursor.execute("DESCRIBE aluno")
# print(mycursor.fetchone())            # fetchone retorna a descrição da primeira coluna. fetchall retorna a descrição de todas as colunas.
for w in mycursor:
    print(w)

mycursor.execute("SELECT venda_id, aluno_id, data_venda FROM venda WHERE aluno_id = '1' ORDER BY curso_id DESC")
for y in mycursor:
    print(y)
