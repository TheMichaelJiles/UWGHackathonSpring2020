import sqlite3
import json  
# import xlrd

# def load_csv_data():
#     loc = ('./resources/data.xlsx')
#     wb = xlrd.open_workbook(loc)
#     sheet = wb.sheet_by_index(0)
    
#     connection = sqlite3.connect('ore.db')
#     cursor = connection.cursor()
#     for i in range(4000):
#         subject = sheet.cell_value(i, 1)
#         courseid = sheet.cell_value(i, 2)
#         summary = sheet.cell_value(i, 5)
#         author = sheet.cell_value(i, 9)
#         title = sheet.cell_value(i, 10)
#         tag = sheet.cell_value(i, 7)

#         if title == "NO TEXT REQUIRED":
#             continue

#         row = [title, author, subject, summary, 'no-link', courseid, tag]
    
#         cursor.execute("INSERT INTO textbooks VALUES (?, ?, ?, ?, ?, ?, ?)", row)
#         connection.commit()
#         print(str(i) + '/4000')
#     connection.close()

def create_textbook_table():
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS textbooks (title TEXT, author TEXT, subject TEXT, summary TEXT, link TEXT, courseid TEXT, tag TEXT)''')
    connection.commit()
    connection.close()

def fetch_match(term, searchType):
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
        rowDict['courseid'] = row[5]
        rowDict['tag'] = row[6]
        rows.append(rowDict)

    matches = []
    for row in rows:
        related_column = row[searchType]
        if term.lower() in related_column.lower():
            matches.append(row)
    
    json_match = json.dumps(matches)
    return json_match

def add_textbook(arguments):
    connection = sqlite3.connect('ore.db')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO textbooks VALUES (?, ?, ?, ?, ?, ?, ?)", arguments)
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
        rowDict['courseid'] = row[5]
        rowDict['tag'] = row[5]
        rows.append(rowDict)
    json_string = json.dumps(rows)
    return json_string
    
if __name__ == '__main__':
    create_textbook_table()
    load_csv_data()