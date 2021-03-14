import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=postgres')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT False
        );
''')

cursor.execute('''
    INSERT INTO table2(id, completed)
    VALUES (%s, %s);
''', (1, True))


SQL = '''INSERT INTO table2(id, completed)
    VALUES (%(id)s, %(completed)s);'''
selectSQL = 'SELECT * FROM table2'
data = {
    'id': 2,
    'completed': False
}
data2 = {
    'id': 3,
    'completed': True
}

cursor.execute(SQL, data)
cursor.execute(SQL, data2)

cursor.execute(selectSQL)

result = cursor.fetchmany(2)
print('FetchMany: ', result)

result2 = cursor.fetchone()
print('FetchOne: ', result2)

# Commit the transaction
connection.commit()

# Close the connection
cursor.close()
connection.close()