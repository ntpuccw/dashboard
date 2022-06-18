# From "streamlit hello"

import matplotlib.pyplot as plt
from scipy.stats import t
import streamlit as st
import numpy as np
import time

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
df1 = np.linspace(0.1, 1, 10)
df2 = np.arange(2, 31)
df = np.hstack((df1, df2))
# print(df)

x = np.linspace(-5, 5, 1000)
fig = plt.figure(figsize=(6,3))

for i in df:
    y = t.pdf(x, i)
    plt.plot(x, y, color = 'b', alpha = 0.5)
    # status_text.text("%i%% degree of freedom" % i)
    # time.sleep(0.05)
    # plt.show()
    plt.pause(0.5)

# st.pyplot(fig)
plt.show()
# for i in df:
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
# st.button("Re-run")