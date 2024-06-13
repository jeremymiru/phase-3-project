import sqlite3

class Table:
    def __init__(self, id, number, capacity):
        self.id = id
        self.number = number
        self.capacity = capacity
d
    
    def create(number, capacity):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO tables (number, capacity)
        VALUES (?, ?)
        ''', (number, capacity))
        connection.commit()
        connection.close()

    
    def get_all():
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM tables')
        tables = cursor.fetchall()
        connection.close()
        return tables

    
    def update(table_id, number, capacity):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        UPDATE tables
        SET number = ?, capacity = ?
        WHERE id = ?
        ''', (number, capacity, table_id))
        connection.commit()
        connection.close()

    
    def delete(table_id):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        DELETE FROM tables WHERE id = ?
        ''', (table_id,))
        connection.commit()
        connection.close()
