import sqlite3
import json  

def create_textbook_table():
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE textbooks
                          (
                             title TEXT, 
                             author TEXT, 
                             subject TEXT, 
                             summary TEXT, 
                             link TEXT
                           )''')
    connection.commit()
    connection.close()
        
def add_textbook(title, author, subject, summary, link):
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    row_values = '(' + title + ', ' + author + ', ' + subject + ', ' + summary + ', ' + link + ')'
    cursor.execute("INSERT INTO textbooks VALUES " + row_values)
    connection.commit()
    connection.close()
    
def get_textbooks_json():
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    rows = cursor.execute("SELECT * FROM textbooks")
    return json.dumps(rows)
    
if __name__ == '__main__':
    create_textbook_table()
    