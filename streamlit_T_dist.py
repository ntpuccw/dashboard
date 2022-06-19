# From "streamlit hello"

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import t, norm
import streamlit as st
import numpy as np
import time

df1 = np.linspace(0.1, 1, 10)
df2 = np.arange(2, 31)
df = np.hstack((df1, df2))
n = range(len(df))

dof = st.slider('Degree of Freedom', min_value=n[0], max_value=n[-1], value=n[10], step=1)
st.write("T(", df[dof],")")

x = np.linspace(-5, 5, 1000)
fig = plt.figure(figsize=(6,3))
norm_y = norm.pdf(x) # Z
plt.plot(x, norm_y, color = 'r', label = "Z")
y = t.pdf(x, df[dof])
plt.plot(x, y, color = 'b', alpha = 0.5, label = "T("+ str(df[dof])+")")
plt.legend()

st.pyplot(fig)

# fig2 = px.line(x = x, y = [norm_y, y])
fig2 = px.line(x = x, y = y, title='T distribution')
# st.write(fig2)

st.plotly_chart(fig2)


d = st.slider('Slide to change the degree of freedom', \
    min_value=n[0], max_value=n[-1], value=n[10], step=1, key='plotly')
st.write("T(", df[d],")")

y = t.pdf(x, df[d])

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=norm_y,
                    mode='lines',
                    name='Z',
                    line=dict(color='firebrick', width=4)))
fig3.add_trace(go.Scatter(x=x, y=y,
                    mode='lines',
                    name='T',
                    line=dict(color='royalblue', width=4)))

st.plotly_chart(fig3)