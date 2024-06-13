import sqlite3

class Reservation:
    def __init__(self, id, customer_id, table_id, reservation_date, time):
        self.id = id
        self.customer_id = customer_id
        self.table_id = table_id
        self.reservation_date = reservation_date
        self.time = time

    
    def create(customer_id, table_id, reservation_date, time):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO reservations (customer_id, table_id, reservation_date, time)
        VALUES (?, ?, ?, ?)
        ''', (customer_id, table_id, reservation_date, time))
        connection.commit()
        connection.close()

    
    def get_all():
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM reservations')
        reservations = cursor.fetchall()
        connection.close()
        return reservations

    
    def update(reservation_id, customer_id, table_id, reservation_date, time):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        UPDATE reservations
        SET customer_id = ?, table_id = ?, reservation_date = ?, time = ?
        WHERE id = ?
        ''', (customer_id, table_id, reservation_date, time, reservation_id))
        connection.commit()
        connection.close()
k
    
    def delete(reservation_id):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()
        cursor.execute('''
        DELETE FROM reservations WHERE id = ?
        ''', (reservation_id,))
        connection.commit()
        connection.close()
