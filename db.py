import pymysql
connection = pymysql.connect(host="localhost", user="root", passwd="00000000", database="testes", port=3306)
cursor = connection.cursor()

#inserting data to db
def add_text(name, idade, email):
    cursor.execute("INSERT INTO form(ID, Nome, Idade, Email) VALUES (DEFAULT, %s, %s, %s)", (name, idade, email))
    connection.commit()
    return 1


def get_data():
    cursor.execute("SELECT * FROM form")
    rows = cursor.fetchall()    
    return rows