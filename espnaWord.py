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
    # sql = "select content from word_content where word='"+word+"'"
    sql = "select word, content from word_content where word like'"+word+"%'"
    # print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows
    # names = [description[0] for description in cur.description]
    # df = pd.DataFrame(rows)
    # df.columns = names
    # return df    

# def word_color(url):
    #  st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    #  st.markdown(f'<p style="color:#ffff00;font-size:20px;">{url}</p>', unsafe_allow_html=True)
def main():
    # xxx('notice')
    database = r"espnaDict.sqlite"
    conn = create_connection(database)
    # with st.container():
        
    #     # st.write("---")
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    word = st.text_input('Search by WORD', 'españ')
    st.write('---')
    # word = 'absoluto'
    # word = 'abandonar'
    # word = 'china'
    df = searchByWord(conn, word)
    if len(df) ==0:
        st.write('~ Nothing Found ~')
    else:
        # col1, col2 = st.columns((1,2))
    # need to separate linebreak by \n
    # df = df[0][0].replace('\\n','\n ')
        for j in range(len(df)):
            col1, col2 = st.columns((1,2))
            tmp = df[j][1].split(sep='\n')
            with col1:
                # st.write(df[j][0])
                st.write(f"<p style='color:#ffff00'>{df[j][0]}</p>", unsafe_allow_html=True)
            for i in tmp:
                # print(i)
                with col2:
                    st.write(i)
                    # st.write('---')
    # df = """{}""".format(df)
    # df = f"{df}"
    # print(df)
    # st.write(df[0][0])
    
    # t = "[('(tr)\n 1. 拋棄，放棄，丟棄:\n ~ a sus hijos \n2. xxx"
    # print(t.replace('\\n', '\n'))
    # st.write(t)
    st.write('---')
    conn.close()

if __name__ == '__main__':
    main()            