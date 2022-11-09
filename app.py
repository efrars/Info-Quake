import json
from streamlit_lottie import st_lottie
import csv
import datetime
import numpy as np
import pandas as pd
import requests
import streamlit as st


st.set_page_config(

    page_title='EarthquakesTR',
    layout='wide'
)
add_selectboxMenu = st.sidebar.selectbox(

    'Areas of Interest',
    ['Recent Earthquakes', 'Most Destructive Earthquakes']
)

if add_selectboxMenu == 'Most Destructive Earthquakes':
    st.markdown("<h1 style='font-size:25px; text-align: center; color:red ; padding:30px; font-style:italic;'>"
                "Destructive Earthquakes of all time!</h1>",
                unsafe_allow_html=True)
    url1 = "https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/earthquakes?maxEqMagnitude=9&minEqMagnitude=7"
    response = requests.get(url1).json()
    earthquakes = response['items']

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            countryInput = st.text_input('Enter country name:').upper()

            i = 1
            with open('csv/magnitude.csv', 'w') as f:
                writer1 = csv.writer(f)
                writer1.writerow(['year', 'magnitude', 'latitude', 'longitude', ])
                dtf3 = []
                for x in earthquakes:
                    country = (x['country'][0:1632])
                    mag = (x['eqMagnitude'])
                    year1 = (x['year'])
                    country2 = country
                    if countryInput == country2:
                        latitude = earthquakes = str(x['latitude'])
                        longitude = earthquakes = str(x['longitude'])
                        data1 = year1, mag, latitude, longitude,
                        dtf3 = pd.DataFrame([[str(i)]], [[country2]], columns=['Total of Major Earthquakes'])
                        writer1.writerow(data1)
                        i = i + 1
                    continue

            if countryInput.isdigit():
                st.warning('Only letters can be entered. Please try again', icon="⚠️")
            elif countryInput:
                st.dataframe(dtf3)
                st.success('Country information been verified with the NOOA', icon="✅")
                st.caption('Count of total Major Earthquakes. Source: https://www.ngdc.noaa.gov/ ')

            if st.button('Click here for map visualization'):
                earthquakes_map = pd.read_csv('csv/magnitude.csv')
                df2 = pd.DataFrame(earthquakes_map, columns=['latitude', 'longitude'])
                st.map(df2)

        with col2:
            selection = st.radio('Which information you want to visualize?',
                                 ('Magnitude', 'Deaths', 'Economic Damage'))

            earthquakes_magnitude_year = pd.read_csv('csv/magnitude.csv')
            if selection == 'Magnitude':
                st.markdown(
                    "<h6 style='font-size:13px; text-align: center; color:gray;'>Magnitude & Year damaging earthquakes</h6>",
                    unsafe_allow_html=True)
                st.area_chart(data=earthquakes_magnitude_year, x='year', y='magnitude')
            url2 = "https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/earthquakes?maxEqMagnitude=9&minDamageAmountOrder=0&minDeathsTotal=0&minEqMagnitude=7"
            response = requests.get(url2).json()
            deaths = response['items']
            with open('csv/deaths.csv', 'w') as f:
                writer2 = csv.writer(f)
                writer2.writerow(['year', 'deaths'])
                for d in deaths:
                    country = (d['country'][0:1632])
                    death = (d['deathsTotal'])
                    year2 = (d['year'])
                    country2 = country
                    if countryInput == country2:
                        data2 = year2, death
                        writer2.writerow(data2)
            deathsDoc = pd.read_csv('csv/deaths.csv')
            if selection == 'Deaths':
                st.markdown(
                    "<h6 style='font-size:13px; text-align: center; color:gray;'>Deaths by Year</h6>",
                    unsafe_allow_html=True)
                st.bar_chart(data=deathsDoc, x='year', y='deaths',
                             use_container_width=True)
                st.caption('Count of total deaths by year. Source: https://www.ngdc.noaa.gov/ ')

            url3 = 'https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/earthquakes?maxEqMagnitude=9&minDamageMillionsDollars=0&minEqMagnitude=7'
            response = requests.get(url3).json()
            damageInMill = response['items']
            if selection == 'Economic Damage':
                with open('csv/economicDamage.csv', 'w') as f:
                    writer3 = csv.writer(f)
                    writer3.writerow(['year', 'damage in millions', ])
                    for a in damageInMill:
                        country = (a['country'][0:1632])
                        year3 = (a['year'])
                        country2 = country
                        if countryInput == country2:
                            damageInMillions = damageInMill = str(a['damageMillionsDollars'])
                            data3 = year3, damageInMillions,
                            writer3.writerow(data3)
                damageFile = pd.read_csv('csv/economicDamage.csv')
                st.markdown(
                    "<h6 style='font-size:13px; text-align: center; color:gray;'>Economic Damage in millions & years </h6>",
                    unsafe_allow_html=True)
                st.line_chart(data=damageFile, x='year', y='damage in millions', use_container_width=True)
                st.caption('Count of economical damage by year. Source: https://www.ngdc.noaa.gov/ ')

else:
    def load_lottiefile(filepath: str):
        with open(filepath,'r') as b:
            return json.load(b)


    load_lottie_earthquake = load_lottiefile('lottie files/earth.json')


    st.markdown(
        "<h1 style='font-size:40px; text-align: center; color:red ; padding:30px; font-style:italic;'>Info-Quake</h1>",
        unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<h5 style='font-size:20px; color:red;'> What are Earthquakes? </h5>",
                        unsafe_allow_html=True)
            st.markdown(
                "<p style='font-size:13px; color:white;'> An earthquake is an intense shaking of Earth’s surface. "
                "The shaking is caused by movements in Earth’s outermost layer. </p>",
                unsafe_allow_html=True)
            st.caption('Source from: Nasa.gov')

        with col2:
            st_lottie(
                load_lottie_earthquake,
                height=150,
                key="earthquake"
            )
            st.markdown(
                "<h6 style='font-size:13px; text-align: right; color:gray;'> Earth Animation: Jam Visual</h6>",
                unsafe_allow_html=True)

    url2 = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
    response = requests.get(url2).json()
    live_feed = response['features']

    with open('csv/earthquakes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['location', 'magnitude', 'date', 'time', 'latitude', 'longitude', ])
        for i in live_feed:
            coordinates = (i['geometry'])
            properties = (i['properties'])
            timestamp = (properties['time'])
            place = (properties['place'])
            magnitude = (properties['mag'])
            magnitude1 = magnitude
            dateOfE = datetime.datetime.fromtimestamp(timestamp / 1000).date()
            timeOfE = datetime.datetime.fromtimestamp(timestamp / 1000).time()
            longitude = coordinates['coordinates'][0]
            latitude = coordinates['coordinates'][1]
            data = place, magnitude, dateOfE, timeOfE, latitude, longitude,
            writer.writerow(data)
            continue

    with st.container():
        col1, col2 = st.columns(2)
        earthquakes_feed = pd.read_csv('csv/earthquakes.csv')
        df = pd.DataFrame(earthquakes_feed, columns=['latitude', 'longitude'])

        df2 = pd.DataFrame(earthquakes_feed, columns=['magnitude'])

        with col1:
            st.markdown(
                "<h6 style='font-size:13px; text-align: center; color:gray; "
                "text-decoration:underline;'> Recent Earthquakes Data </h6>",
                unsafe_allow_html=True)
            st.dataframe(earthquakes_feed)
            st.caption('Source by: https://earthquake.usgs.gov/ ')

        with col2:
            st.markdown(
                "<h6 style='font-size:13px; text-align: center; color:gray; "
                "text-decoration:underline;'> Recent Earthquakes Locations </h6>",
                unsafe_allow_html=True)
            st.map(df)
