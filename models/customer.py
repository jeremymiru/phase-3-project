import sqlite3

class Customer:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    
    def create(name, phone, email):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO customers (name, phone, email)
        VALUES (?, ?, ?)
        ''', (name, phone, email))
        connection.commit()
        connection.close()

    
    def get_all():
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()
        connection.close()
        return customers

    
    def update(customer_id, name, phone, email):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        UPDATE customers
        SET name = ?, phone = ?, email = ?
        WHERE id = ?
        ''', (name, phone, email, customer_id))
        connection.commit()
        connection.close()

    
    def delete(customer_id):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        DELETE FROM customers WHERE id = ?
        ''', (customer_id,))
        connection.commit()
        connection.close()
