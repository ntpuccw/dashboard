import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st

# from textblob import TextBlob
# from googletrans import Translator
# from google_trans_new import google_translator  
# import googletrans
# import translators as ts  # streamlit has no such module


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
def searchByWord_zh(conn, word):
    # sql = "select content from word_content where word='"+word+"'"
    sql = "select word, content from word_content where content like'%"+word+"%'"
    # print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows
# def word_color(url):
    #  st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    #  st.markdown(f'<p style="color:#ffff00;font-size:20px;">{url}</p>', unsafe_allow_html=True)
def main():
    st.title("稀罕·西漢/漢西辭典")
    database = r"espnaDict.sqlite"
    conn = create_connection(database)
    
    word = st.text_input('輸入西班牙語單字查詢中文辭義（完整單字或前部分字母皆可）', 'españ')
    
    # print(TextBlob(word).detect_language())
    # translator = google_translator()
    # dt1 = translator.detect(word)
    # print(dt1)

    st.write('---')
    df = searchByWord(conn, word)
    if len(df) ==0:
        st.write('~ Nothing Found ~')
    else:
    # need to separate linebreak by \n
        for j in range(len(df)):
            col1, col2 = st.columns((1,2))
            tmp = df[j][1].split(sep='\n') 
            with col1:
                st.write(f"<p style='color:#FF4500'>{df[j][0]}</p>", unsafe_allow_html=True)
            for line in tmp:
                with col2:
                    st.write(line)
                    
    st.write('---')
    word_zh = st.text_input('輸入中文字查詢相關西文單字', '番紅花')
    st.write('---')
    df = searchByWord_zh(conn, word_zh)
    if len(df) ==0:
        st.write('~ Nothing Found ~')
    else:
    # need to separate linebreak by \n
        for j in range(len(df)):
            col1, col2 = st.columns((1,2))
            tmp = df[j][1].split(sep='\n') 
            with col1:
                st.write(f"<p style='color:#FF4500'>{df[j][0]}</p>", unsafe_allow_html=True)
            for line in tmp:
                with col2:
                    st.write(line)
                    
    st.write('---')
    st.write("[Created by Luisa Chang@ntu >>>](https://luisachangntu.me/)")
    
    # ----- Try to include other translators -------------------
    # # print(googletrans.LANGUAGES)
    # st.write("From other translators")
    # # translator = Translator()
    
    # # translator = google_translator()  
    # # translate_text = translator.translate('Hola mundo!', lang_src='es', lang_tgt='en') 
    # # result = translator.translate(word, src = 'es', dest='zh-tw')
    # # st.write(result.text)
    # # st.write(translate_text)
    # # print(translate_text)
    # col1, col2 = st.columns((1,2))
    # with col1:
    #     st.write('By Google')
    # with col2:
    #     text = ts.google('españolismo' , to_language = 'zh-TW', if_use_cn_host=True)
    #     st.write(text)
    # col1, col2 = st.columns((1,2))
    # with col1:
    #     st.write('By Microsoft Bing')
    # with col2:
    #     text = ts.bing(word , to_language = 'zh-Hant')
    #     st.write(text)
    # # text = ts.caiyun(word , to_language = 'zh', professional_field=None)
    # # text = ts.baidu(word , to_language = 'zh', professional_field='common')
    # # st.write("caiyun:\n" + text)
    # # st.write(ts.translate_html(word, translator=ts.google, to_language='zh-TW', n_jobs=-1))
    # st.write('---')
    
    conn.close()


if __name__ == '__main__':
    main()            