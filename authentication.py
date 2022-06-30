# Find out duolicate words
# SELECT word, content, COUNT(*)
# FROM word_content
# group by word
# HAVING COUNT(*) > 1

import streamlit as st
import sqlite3

db_file = r"test.sqlite"

def clear_form():
    st.session_state["new"] = ""
    st.session_state["content"] = ""

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def searchByWord(word):
    conn = create_connection()
    # sql = "select content from word_content where word='"+word+"'"
    # sql = "select word, content from word_content where word like'"+word+"%'"
    sql = "select word, content from word_content where word='"+word+"'"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

def insertData(word, content):
    conn = create_connection()
    sql = "INSERT INTO word_content(word, content) VALUES(?,?)" 
    cur = conn.cursor()
    cur.execute(sql, (word, content))
    conn.commit()
    conn.close()

def updateData(word, content):
    conn = create_connection()
    sql = "UPDATE  word_content SET content =? where word = ?" 
    cur = conn.cursor()
    cur.execute(sql, (content, word))
    conn.commit()
    conn.close()

def deleteData(word):
    conn = create_connection()
    sql = "DELETE FROM word_content WHERE word = ?" 
    cur = conn.cursor()
    cur.execute(sql, (word,))
    conn.commit()
    conn.close()

def display_content(df):
    if len(df) ==0:
        st.error("~ Nothing found in the dictionary ~")
        st.write('---')
        return "None"
    st.write(f"<p style='color:#FF4500'>{df[0][0]}</p>", unsafe_allow_html=True)
    content = st.text_area("中文辭義", df[0][1], height = 200, key = "update_delete")
    return content
# for multiple contents(not normal situation)
# def display_content(df):
#     if len(df) ==0:
#         st.write('~ Nothing Found ~')
#         st.write('---')
#         return
# # need to separate linebreak by \n
#     for j in range(len(df)):
#         lines = []
#         col1, col2 = st.columns((1,2))
#         tmp = df[j][1].split(sep='\n') 
#         with col1:
#             st.write(f"<p style='color:#FF4500'>{df[j][0]}</p>", unsafe_allow_html=True)
        
#         with col2:
#             content = st.text_area("content", df[j][1], height = 200, key = j) 
#             # for line in tmp:
#             #     st.write(line)
    
#         col1, col2 = st.columns((1,2))
#         with col1:
#             if st.button("提交修改 "+ df[j][0]+ " 內容", key = j):
#                 updateData(df[j][0], content)
#                 # df = searchByWord(df[j][0])
#                 # display_content(df)
#                 st.success("更新成功 ~")
#                 st.balloons()
            
#         with col2:
#             if st.button("提交刪除單字 "+ df[j][0], key = j):
#                 deleteData(df[j][0])
#                 st.success("刪除成功 ~")
#                 st.snow()
#         st.write('---')
# --------------------------------------------------------  
# check_password() is copyied from streamlit demo  
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.subheader("修改與刪除西語字彙與其中文辭義")
    with st.form("update_delete_form"):
        word = st.text_input('輸入欲修改或刪除的西文單字（完整單字）', '')
        c1, c2, c3 = st.columns(3)
        with c1:
            search = st.form_submit_button("查詢")
        with c2:
            update = st.form_submit_button("提交修改 "+ word)
        with c3:
            delete = st.form_submit_button("提交刪除 "+ word)
        # content = "None"
        if search:
            df = searchByWord(word)
            content = display_content(df)
            # if content =="None":
            #     print("check")
        if update:
            if 'update_delete' not in st.session_state:
                st.error("No content")
            else:
                content = st.session_state["update_delete"]
                updateData(word, content)
                st.success("更新成功 ~")
                st.balloons()
        if delete:
            if 'update_delete' not in st.session_state:
                st.error("No content ")
            else:
                deleteData(word)
                st.success("刪除成功 ~")
                st.snow()            
    # -------------------------------------
    # st.subheader("修改與刪除西語字彙與其中文辭義")
    # word = st.text_input('輸入欲修改或刪除的西文單字（完整單字）', '')
    # st.write('---')
    # df = searchByWord(word)
    # display_content(df)
    # --------------------------------------
    
    # if searchBtn :
    #     df = searchByWord(word)
    #     display_content(df)
    # col1, col2 = st.columns(2)
    # with col1:
    #     word = st.text_input('輸入西班牙語單字查詢中文辭義（完整單字）', 'España')
    # with col2:
    #     if st.button("查詢"):
    #         df = searchByWord(word)
    #         display_content(df)

    # st.write('---')
    # df = searchByWord(word)
    # display_content(df)
    
    # ----------- INSERT ----------------------------
    st.subheader("新增西語字彙與其中文辭義")
    with st.expander("打開查閱西文字彙編輯規則"):
     st.text("""
(m;f)
	1. 委員、代表； ~ político 政治委員
	El comisario europeo de Energía no asistió a la cumbre del año pasado. 去年，歐洲能源委員沒有出席峰會。
	2. 警察局長、警長
	El comisario pidió una mayor colaboración de la policía nacional en el caso. 警長呼籲在此案中加強國家警察的合作。
	3. 特派員
	4.  (Amér.) 檢察官
	5. (展覽等等的)主辦人、負責人、策展人
	El comisario de la exposición se encargó de redactar el programa de eventos. 展覽策展人負責起草活動計劃。
(vprnl) 沉醉於，全神貫注於: El niño se embarga en el juego todo el día.小孩整天沉迷於遊戲。
-menta
	(suf)表示"集合名詞"的意思，例如: vestimenta
-mento
	(suf)表示「動作」或「結果」，例如: impedimento, salvamento
	menú
	(m)(pl. menúes或 menús)
	1.菜單，菜譜
	2.菜餚(一桌菜的總稱)
	3.快餐、特餐；商業套餐
	4.日程，日程表
-metría
	(suf)表示「計量，測量」
-metro
	(suf)
	1.表示「計量，測量」
	2.表示「公尺，米」
-mienta
	(suf)用來構成某些集合名詞，如: herramientas
     """)
    with st.form("Insert_form"):
        new_word = st.text_input('輸入西班牙語單字', '', key = "new")
        new_content = st.text_area('輸入中文辭義', '', height = 200, key= "content")
        st.text(new_word)
        st.text(new_content)
        c1, c2, c3 = st.columns(3)
        with c1:
            confirmed = st.form_submit_button("確認內容")
        with c2:
            submitted = st.form_submit_button("提交新單字 "+ new_word)
        with c3:
            clearall = st.form_submit_button("清除以重新輸入", on_click=clear_form)

        if submitted:
        # if st.button("新增"):
            if new_word =='' or new_content == '':
                st.error('請輸入單字與中文辭義')
            else:
                insertData(new_word, new_content)
                st.success('新增成功 ~')
                st.snow()

# ------- demo codes --------------------------------------------
#     with st.form("my_form"):
#         st.write("Inside the form")
#         slider_val = st.slider("Form slider")
#         checkbox_val = st.checkbox("Form checkbox")

#         # Every form must have a submit button.
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             st.write("slider", slider_val, "checkbox", checkbox_val)
#             st.success('新增成功 ~')

# st.write("Outside the form")   