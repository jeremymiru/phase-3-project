import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

 f
from models.customer import Customer
from models.table import Table
from models.reservation import Reservation
from datetime import datetime

def create_customer():
    name = input("Enter customer name: ")
    phone = input("Enter customer phone: ")
    email = input("Enter customer email: ")
    Customer.create(name, phone, email)
    print(f"Customer {name} added successfully.")

def create_table():
    number = int(input("Enter table number: "))
    capacity = int(input("Enter table capacity: "))
    Table.create(number, capacity)
    print(f"Table {number} with capacity {capacity} added successfully.")

def create_reservation():
    customer_id = int(input("Enter customer ID: "))
    table_id = int(input("Enter table ID: "))
    reservation_date = input("Enter reservation date (YYYY-MM-DD HH:MM): ")
    time_slot = input("Enter time slot: ")
    Reservation.create(customer_id, table_id, reservation_date, time_slot)
    print(f"Reservation for customer ID {customer_id} at table ID {table_id} on {reservation_date} at {time_slot} added successfully.")

def view_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}, Email: {customer[3]}")

def view_tables():
    tables = Table.get_all()
    for table in tables:
        print(f"ID: {table[0]}, Number: {table[1]}, Capacity: {table[2]}")

def view_reservations():
    reservations = Reservation.get_all()
    for reservation in reservations:
        print(f"ID: {reservation[0]}, Customer ID: {reservation[1]}, Table ID: {reservation[2]}, Date: {reservation[3]}, Time Slot: {reservation[4]}")

def update_customer():
    customer_id = int(input("Enter customer ID to update: "))
    name = input("Enter new customer name: ")
    phone = input("Enter new customer phone: ")
    email = input("Enter new customer email: ")
    Customer.update(customer_id, name, phone, email)
    print(f"Customer ID {customer_id} updated successfully.")

def update_table():
    table_id = int(input("Enter table ID to update: "))
    number = int(input("Enter new table number: "))
    capacity = int(input("Enter new table capacity: "))
    Table.update(table_id, number, capacity)
    print(f"Table ID {table_id} updated successfully.")

def update_reservation():
    reservation_id = int(input("Enter reservation ID to update: "))
    customer_id = int(input("Enter new customer ID: "))
    table_id = int(input("Enter new table ID: "))
    reservation_date = input("Enter new reservation date (YYYY-MM-DD HH:MM): ")
    time_slot = input("Enter new time slot: ")
    Reservation.update(reservation_id, customer_id, table_id, reservation_date, time_slot)
    print(f"Reservation ID {reservation_id} updated successfully.")

def delete_customer():
    customer_id = int(input("Enter customer ID to delete: "))
    Customer.delete(customer_id)
    print(f"Customer ID {customer_id} deleted successfully.")

def delete_table():
    table_id = int(input("Enter table ID to delete: "))
    Table.delete(table_id)
    print(f"Table ID {table_id} deleted successfully.")

def delete_reservation():
    reservation_id = int(input("Enter reservation ID to delete: "))
    Reservation.delete(reservation_id)
    print(f"Reservation ID {reservation_id} deleted successfully.")

def main():
    while True:
        print("\n1. Create Customer")
        print("2. Create Table")
        print("3. Create Reservation")
        print("4. View Customers")
        print("5. View Tables")
        print("6. View Reservations")
        print("7. Update Customer")
        print("8. Update Table")
        print("9. Update Reservation")
        print("10. Delete Customer")
        print("11. Delete Table")
        print("12. Delete Reservation")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_table()
        elif choice == "3":
            create_reservation()
        elif choice == "4":
            view_customers()
        elif choice == "5":
            view_tables()
        elif choice == "6":
            view_reservations()
        elif choice == "7":
            update_customer()
        elif choice == "8":
            update_table()
        elif choice == "9":
            update_reservation()
        elif choice == "10":
            delete_customer()
        elif choice == "11":
            delete_table()
        elif choice == "12":
            delete_reservation()
        elif choice == "13":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
