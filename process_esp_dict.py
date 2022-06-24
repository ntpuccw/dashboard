import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def insert_data(conn, word, content):
    sql = "INSERT INTO word_content(word, content) VALUES(?,?)" 
    cur = conn.cursor()
    cur.execute(sql, (word, content))

database = r"espnaDict.sqlite"
# create a database connection
conn = create_connection(database)

with open('dic220611.txt', encoding='utf8') as f:
    lines = f.readlines()

# print(len(lines)
n = len(lines)
cnt = 0
# flag = 0
content = ''
for line in lines:
    # print(line)
    if not '\t' in line[0] :
        if cnt > 0:
            insert_data(conn, word, content)
            # print(word + content)
    
        word = line.replace('\n', '')
        # flag = 1
        content = ''
        cnt += 1
        # print(word)
    else:
        content += line.replace('\t', '')
        # print(line.replace('\t', ''))

conn.commit()
# print(cnt)