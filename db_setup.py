import sqlite3
import os

DB_FILE = "database.db"

def reset_database():
    # Delete the existing DB file if it exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print("Old database deleted.")

    # Create a new database and setup tables
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create your tables here (example table 'users')
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value REAL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("New database created and reset.")

def main():
    reset_database()

    # Now the database is empty and ready for new data
    # You can add your user input and processing logic here
    print("Database reset and ready. Add your logic!")

if __name__ == "__main__":
    main()
