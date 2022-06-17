import pandas as pd
import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# df= pd.read_excel('../../Data/Iris.xls')
st.write("""
    # My First App
    Hello World !* $\int_0^5 f(x) dx= x^2 + \\pi$
    """)
# st.line_chart(df["Sepal Length"])
# # st.line_chart(df["Sepal Width"])
# number = st.slider("Pick a number", 0, 100)

x = np.linspace(-5, 5, 1000)
y = norm.pdf(x, loc = 0, scale = 1)
# fig, ax = plt.subplots(figsize = (4, 3))
fig = plt.figure(figsize=(6,3))
plt.plot(x,y)
st.pyplot(fig)
# plt.show()


