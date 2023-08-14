import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1873"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE game_score")
mycursor.execute("USE game_score")

Q1 = "CREATE TABLE user (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(45), passwd VARCHAR(45))"
Q2 = "CREATE TABLE score (user_id INT PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES user(id), game1 INT DEFAULT 0, game2 INT DEFAULT 0)"
# relação entre tabelas user e score é de 1:1 (uma entrada de score por usuário), com isso, neste caso, é possível utilizar a própria foreign key como primary key da tabela. 

mycursor.execute(Q1)
mycursor.execute(Q2)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

users = [("tim", "techwithtim"),
         ("joe", "joey123"),
         ("sarah", "sarah89")]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

Q3 = "INSERT INTO user (name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO score (user_id, game1, game2) VALUES (%s, %s, %s)"

for y, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[y])

db.commit()

mycursor.execute("SELECT * FROM user")
for z in mycursor:
    print(z)

mycursor.execute("SELECT * FROM score")
for w in mycursor:
    print(w)
