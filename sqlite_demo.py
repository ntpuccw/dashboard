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
    return df


def main():
    database = r"database.sqlite"

    # create a database connection
    conn = create_connection(database)
    with conn:
        df = select_table(conn, 'Authors')
        st.write(df)


    conn.close()

if __name__ == '__main__':
    main()            