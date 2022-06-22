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

def select_table(conn, tbname):
    sql = 'select * from ' + tbname
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    names = [description[0] for description in cur.description]
    df = pd.DataFrame(rows)
    df.columns = names
    return df

def searchByTitle(conn, title):
    sql = "select id, title, eventtype from papers where title like '%" + title+"%'"
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    names = [description[0] for description in cur.description]
    df = pd.DataFrame(rows)
    df.columns = names
    return df    


def main():
    database = r"database.sqlite"
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            table_opts = ['Authors', 'Paperauthors', 'Papers']
            # tbname = st.text_input('Search by Table name', 'authors')
            tbname = st.selectbox('Select a Table:', table_opts, 0)

        # create a database connection
        conn = create_connection(database)
        with conn:
            df = select_table(conn, tbname)
            st.write(df)

    with st.container():
        st.write("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            title = st.text_input('Search by Title', 'network')
        df = searchByTitle(conn, title)
        st.write(df)
    




    conn.close()

if __name__ == '__main__':
    main()            