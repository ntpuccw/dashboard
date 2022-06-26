import sqlite3
from sqlite3 import Error
import pandas as pd
import streamlit as st
# import requests
# from streamlit_lottie import st_lottie

# from textblob import TextBlob
# from googletrans import Translator
# from google_trans_new import google_translator  
# import googletrans
# import translators as ts  # streamlit has no such module

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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

def display_content(df):
    if len(df) ==0:
        st.write('~ Nothing Found ~')
        return
# need to separate linebreak by \n
    for j in range(len(df)):
        col1, col2 = st.columns((1,2))
        tmp = df[j][1].split(sep='\n') 
        with col1:
            st.write(f"<p style='color:#FF4500'>{df[j][0]}</p>", unsafe_allow_html=True)
        for line in tmp:
            with col2:
                st.write(line)
# def word_color(url):
    #  st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    #  st.markdown(f'<p style="color:#ffff00;font-size:20px;">{url}</p>', unsafe_allow_html=True)
def main():
    # left_column, right_column = st.columns((3, 1))
    # with left_column:
    #     st.title("LUISA · 西漢/漢西辭典")
    #     st.subheader("Diccionario Español-Chino / Chino-Español")
    # with right_column:
    #     lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_Jmpjal.json")
    #     st_lottie(lottie_coding, height=200, key="coding")
    st.title("LUISA · 西漢/漢西辭典")
    st.subheader("Diccionario Español-Chino / Chino-Español")
    database = r"espnaDict.sqlite"
    conn = create_connection(database)
    
    word = st.text_input('輸入西班牙語單字查詢中文辭義（完整單字或前部分字母皆可）', 'españ')
    st.write('---')
    df = searchByWord(conn, word)
    display_content(df)
    st.write('---')

    word_zh = st.text_input('輸入中文字查詢相關西文單字', '番紅花')
    st.write('---')
    df = searchByWord_zh(conn, word_zh)
    display_content(df)
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
    st.write("""<p style='font-size:15px;'>
    網頁設計維護：José Saúl Yang ‧ Eva Chen ‧ Úlises Chuang ‧ 
    Urbano Lee ‧ Morgan Kao ‧ Yuan-Ying Wang ‧ Pin Fang Chen ‧ 
    Kuan Hao Chiao
    </p>""", unsafe_allow_html=True)
    st.write("""<p style='font-size:15px;'>資料搜集翻譯：Luisa Chang ‧ José Saúl Yang ‧ Pedro Chang ‧ 
    Andrés Wu ‧ Vicente Hung ‧ Benito Wang ‧ Lolita Kuang ‧ Adrián Chou ‧ Danial Hou ‧ Bernardo Lin ‧ 
    Eva Chen ‧ Enrique Lin ‧ Aurora Tsai ‧ Esther Huang ‧ Judy Yang ‧ 
    Yolanda Cheng ‧ Rafael Lin ‧ Henry Yang ‧ Sofía Liu ‧ Aiden Chuang ‧ 
    Ellen Chuang ‧ Carlos Chang ‧ Esperanza Hou ‧ Daniel Yen ‧ Gonzalo Yang ‧ 
    Jessica Fan ‧ Emma Chou ‧ Pilar Hsu ‧ Paola Huang ‧ Felipe Chen ‧ 
    Irene Chien ‧ Alberto Chang ‧ Jaime Kao ‧ Inés Hung ‧ Linda Wang ‧ 
    Diego Chen ‧ Margarita Yao ‧ Ke Ru Lai
    </p>""", unsafe_allow_html=True)
    st.write('---')
    conn.close()


if __name__ == '__main__':
    main()            