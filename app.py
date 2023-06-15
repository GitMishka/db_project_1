import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn):
    create_table_query = """ CREATE TABLE IF NOT EXISTS contacts (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        phone text NOT NULL,
                                        email text NOT NULL
                                    ); """
    try:
        c = conn.cursor()
        c.execute(create_table_query)
    except Error as e:
        print(e)

def add_contact(conn, contact):
    sql = ''' INSERT INTO contacts(name,phone,email)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, contact)
    return cur.lastrowid

def get_all_contacts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def update_contact(conn, contact):
    sql = ''' UPDATE contacts
              SET name = ? ,
                  phone = ? ,
                  email = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()

def delete_contact(conn, id):
    sql = 'DELETE FROM contacts WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    conn = create_connection()

    if conn is not None:
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")

    while True:
        print("\n1. Add contact")
        print("2. View all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone: ")
            email = input("Enter the email: ")
            contact = (name, phone, email)
            add_contact(conn, contact)

        elif choice == "2":
            print("\nAll contacts:")
            get_all_contacts(conn)

        elif choice == "3":
            id = int(input("Enter the contact id to update: "))
            name = input("Enter the updated name: ")
            phone = input("Enter the updated phone: ")
            email = input("Enter the updated email: ")
            contact = (name, phone, email, id)
            update_contact(conn, contact)

        elif choice == "4":
            id = int(input("Enter the contact id to delete: "))
            delete_contact(conn, id)

        elif choice == "5":
            break

if __name__ == '__main__':
    main()
