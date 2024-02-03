# this class will export the tickets into a SQL database system
# Add into the database when it is created and update the database when it is updated.  Not  compulsory though.
# We could just add it at the end only when it is resolved.

# Class that offers data persistence via SQLite
import sqlite3


class DBService:
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(f'{filename}.db')
        self.c = self.conn.cursor()

    def create_table(self): # this method creates a table to accommodate the resolved ticket objects
        query = '''CREATE TABLE IF NOT EXISTS tickets
        (ticket_id INT PRIMARY KEY NOT NULL,
        timestamp DATETIME NOT NULL,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        department TEXT NOT NULL,
        contact_no VARCHAR(25) NOT NULL,
        issue_desc TEXT NOT NULL,
        priority INT NOT NULL,
        status TEXT NOT NULL);'''

        self.c.execute(query)
        self.conn.commit()

    def db_add(self, obj): # this adds a ticket/node object into the already existing database
        query = f'''
                INSERT INTO tickets (ticket_id, timestamp, username, email, department, contact_no, issue_desc, priority,
                status)
                VALUES ('{obj.get_ticketid()}', '{obj.timestamp}', '{obj.user_name}', '{obj.email}', '{obj.department}', 
                '{obj.contact_no}', '{obj.description}', '{obj.priority}', '{obj.ticket_status}');'''

        self.c.execute(query)
        self.conn.commit()

    # def update_db(self):



