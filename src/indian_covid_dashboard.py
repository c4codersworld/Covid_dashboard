import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# To Set background image
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1469050624972-f03b8678e363?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# To load indian_covid_tilelie data
country_data_timeline = pd.read_csv("../data/indian_covid_timeline.csv") 

# To load state_covid_data data 
sdata = pd.read_csv("../data/state_covid_data.csv") 
# Sort state wise data based on the confirmed case in descending order for find the most COVID-19 having states.
state_sort_data = sdata.sort_values(by=['Confirmed'], ascending=False)

st.markdown("<h1 style='text-align: left; color: red;'>Covid-19 Dashboard For India</h1>",unsafe_allow_html=True)
st.markdown('The dashboard visualizes the Covid-19 condition in India')
st.sidebar.title("Visualization Selector")

# Selectbox for bar chart
bar_select = st.sidebar.selectbox('Visualization type', ['All', 'Confirmed','Recovered','Deaths'], key='1')
# Selectbox for line chart
line_select = st.sidebar.selectbox('Visualization type', ['All', 'Confirmed','Recovered','Deaths'],key='2')

# Condition for selecting specific bar chart
if bar_select=='All':
    st.markdown("<h3 style='text-align: left; color: blue;'>Most COVID States</h1>",unsafe_allow_html=True)
    fig = go.Figure(data=[
    go.Bar(name='Confirmed', x=state_sort_data['State'][:5], y=state_sort_data['Confirmed'][:5]),
    go.Bar(name='Recovered', x=state_sort_data['State'][:5], y=state_sort_data['Recovered'][:5]),
    go.Bar(name='Deaths', x=state_sort_data['State'][:5], y=state_sort_data['Deaths'][:5])])
    st.plotly_chart(fig)

if bar_select=='Confirmed':
    st.markdown("<h3 style='text-align: left; color: blue;'>Most COVID Confirmed States</h1>",unsafe_allow_html=True)
    fig = go.Figure(data=[
    go.Bar(name='Confirmed', x=state_sort_data['State'][:5], y=state_sort_data['Confirmed'][:5])])
    st.plotly_chart(fig)

if bar_select=='Recovered':
    st.markdown("<h3 style='text-align: left; color: blue;'>Most COVID Recovered States</h1>",unsafe_allow_html=True)
    state_sort_data = sdata.sort_values(by=['Recovered'], ascending=False)
    fig = go.Figure(data=[
    go.Bar(name='Recovered', x=state_sort_data['State'][:5], y=state_sort_data['Recovered'][:5])])
    st.plotly_chart(fig)

if bar_select=='Deaths':
    st.markdown("<h3 style='text-align: left; color: blue;'>Most COVID Deaths States</h1>",unsafe_allow_html=True)
    state_sort_data = sdata.sort_values(by=['Deaths'], ascending=False)
    fig = go.Figure(data=[
    go.Bar(name='Deaths', x=state_sort_data['State'][:5], y=state_sort_data['Deaths'][:5])])
    st.plotly_chart(fig)



# Condition for selecting specific line chart
if line_select == 'All':
    st.markdown("<h3 style='text-align: left; color: blue;'>Daily Confirmed, Recovered Cases , Daily Deaths</h1>",unsafe_allow_html=True)
    fig = px.line(country_data_timeline, x="Date", y=["Daily Confirmed","Daily Recovered","Daily Deaths"])
    st.plotly_chart(fig)


if line_select == 'Confirmed':
    st.markdown("<h3 style='text-align: left; color: blue;'>Daily Confirmed</h1>",unsafe_allow_html=True)
    fig = px.line(country_data_timeline, x="Date", y=["Daily Confirmed"])
    st.plotly_chart(fig)

if line_select == 'Recovered':
    st.markdown("<h3 style='text-align: left; color: blue;'>Daily Confirmed</h1>",unsafe_allow_html=True)
    fig = px.line(country_data_timeline, x="Date", y=["Daily Recovered"])
    st.plotly_chart(fig)

if line_select == 'Deaths':
    st.markdown("<h3 style='text-align: left; color: blue;'>Daily Deaths</h1>",unsafe_allow_html=True)
    fig = px.line(country_data_timeline, x="Date", y=["Daily Deaths"])
    st.plotly_chart(fig)

# For Indian map
st.markdown("<h3 style='text-align: left; color: blue;'>COVID Spread In India</h1>",unsafe_allow_html=True)
st_data  = sdata[['State','Confirmed']]
fig = px.choropleth(
    st_data,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Confirmed',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig)
