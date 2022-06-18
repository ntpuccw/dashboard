import pandas as pd
import streamlit as st
import plotly.express as px

df = px.data.gapminder()

st.write(df)
year_opts = df['year'].unique().tolist()
year = st.selectbox('Which year to select', year_opts, 0)
# df = df[df['year'] == year]  

fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', size= 'pop', 
        color = 'continent', hover_name= 'continent', log_x = True,
        size_max = 55, range_x = [100, 100000], range_y = [25, 90],
        animation_frame= 'year', animation_group='country'
        )

fig.update_layout(width = 800)
st.write(fig)

covid = pd.read_csv ('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Code','Date', 'Confirmed', 'Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('Y%-%m-%d')
country_options = covid['Country'].unique().tolist()
st.write(covid)
date_options = covid['Date'].unique().tolist()
date = st.selectbox('which date to select ?', date_options, 100)
country = st.multiselect('Which country would like to see?', country_options, ['Brazil'])
covid = covid[covid['Country'].isin(country)]
# covid = covid[covid['Date']==date]
fig2= px.bar(covid, x = 'Country', y = 'Confirmed', color = 'Country', range_y = [0, 35000], 
        animation_frame= 'Date', animation_group='Country')

fig2.layout.updatemenus[0].buttons[0].args[1]['frame']['duration']=0
fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['duration']=5
fig2.update_layout(width = 800)
st.write(fig2)