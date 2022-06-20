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

#----- use matplotlib to draw graphs ----------------
x = np.linspace(-8, 8, 1000)
fig = plt.figure(figsize=(6,3))
norm_y = norm.pdf(x) # Z
plt.plot(x, norm_y, color = 'r', label = "Z")
y = t.pdf(x, df[dof])
plt.plot(x, y, color = 'b', alpha = 0.5, label = "T("+ str(df[dof])+")")
# plt.title('$\sqrt{x}$')
plt.legend()

st.pyplot(fig)

#---- Use plotly to draw lines -------------
# fig2 = px.line(x = x, y = [norm_y, y]) # two lines
fig2 = px.line(x = x, y = y, title='T distribution')
# st.write(fig2)

st.plotly_chart(fig2)

# ----- Use plotly to draw lines with various attributes ----
d = st.slider('Slide to change the degree of freedom', \
    min_value=n[0], max_value=n[-1], value=n[10], step=1, key='plotly')
st.write("T(", np.round(df[d],1),")")

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

fig3.update_layout(title='T distribution with various degree of freedoms',
                   xaxis_title='x',
                   yaxis_title='y')

st.plotly_chart(fig3)

#----------- plotly + slider from plotly Doc ---

fig4 = go.Figure()
# Add traces, one for each slider step

# fig4.add_trace(go.Scatter(x=x, y=norm_y,
#                     mode='lines',
#                     name='Z',
#                     line=dict(color='firebrick', width=4)))
for step in df:
    fig4.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=4),
            # name="𝜈 = " + str(np.round(step,1)),
            name="nu = " + str(np.round(step,1)),
            x=x,
            y=t.pdf(x, step)))

fig4.add_trace(go.Scatter(x=x, y=norm_y,
                    mode='lines',
                    name='Z',
                    line=dict(color='firebrick', width=4)))
# Make 10th trace visible
fig4.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig4.data)):
    dof =str(np.round(df[i],1)) if i<len(fig4.data)-1 else "$infty$"
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig4.data)},
              {"title": "Slider switched to df: " + dof}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][-1] = True # the last trace always be visible
    steps.append(step)

sliders = [dict(
    active=20,
    currentvalue={"prefix": "Degree of freedom: "},
    pad={"t": 100},
    steps=steps
)]
fig4.update_xaxes(range=(-10,10))
fig4.update_yaxes(range=(0,0.5))
fig4.update_layout(
    sliders=sliders,
    # showlegend=False
)


st.plotly_chart(fig4)
