import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE


# Cria a tabela primeiro
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Agora, execute os comandos DELETE
# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso 
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Registrar valores nas colunas da tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
)

cursor.execute(sql, ('Sem nome', 3))
cursor.executemany(sql, (
    ('Joãozinho', 3),
    ('Maria', 2),
    ('Helena', 4),
    ('Joana', 5),
))
connection.commit()



if __name__ == '__main__':
    print(sql)

    cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "3" '              
    )

    cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "1" '              
    )

    cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="QUALQUER", weight=67.89 '
    'WHERE id = "2" '              
    )
    connection.commit()

    cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'              
    )    

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()  # Fechar o cursor antes de fechar a conexão
    connection.close()
