import sqlite3
import json  

def create_textbook_table():
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS textbooks (title TEXT, author TEXT, subject TEXT, summary TEXT, link TEXT)''')
    connection.commit()
    connection.close()
        
def add_textbook(arguments):
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO textbooks VALUES (?, ?, ?, ?, ?)", arguments)
    connection.commit()
    connection.close()
    
def get_textbooks_json():
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    rows = cursor.execute("SELECT * FROM textbooks")
    return json.dumps(rows)
    
if __name__ == '__main__':
    create_textbook_table()
    