# DELETE data 

import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def searchByWord(conn, word):
    sql = "select content from word_content where word='"+word+"'"
    # print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows
    # names = [description[0] for description in cur.description]
    # df = pd.DataFrame(rows)
    # df.columns = names
    # return df    


def main():
    database = r"espnaDict.sqlite"
    conn = create_connection(database)
    # with st.container():
        
    #     # st.write("---")
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    word = st.text_input('Search by WORD', 'abandonar')
    # word = 'absoluto'
    # word = 'abandonar'
    df = searchByWord(conn, word)
    if len(df) ==0:
        # print('Nothing Found')
        st.write('~ Nothing Found ~')
    else:
    # need to separate linebreak by \n
    # df = df[0][0].replace('\\n','\n ')
        df = df[0][0].split(sep='\n')
        for i in df:
            st.write(i)
    # df = """{}""".format(df)
    # df = f"{df}"
    # print(df)
    # st.write(df[0][0])
    
    # t = "[('(tr)\n 1. 拋棄，放棄，丟棄:\n ~ a sus hijos \n2. xxx"
    # print(t.replace('\\n', '\n'))
    # st.write(t)

    conn.close()

if __name__ == '__main__':
    main()            