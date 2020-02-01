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
    
    rows = []
    for row in cursor.execute("SELECT * FROM textbooks"):
        rowDict = {}
        rowDict['title'] = row[0]
        rowDict['author'] = row[1]
        rowDict['subject'] = row[2]
        rowDict['summary'] = row[3]
        rowDict['link'] = row[4]
        rows.append(rowDict)
    json_string = json.dumps(rows)
    return json_string
    
if __name__ == '__main__':
    create_textbook_table()
    