import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

import numpy as np 
import pandas as pd 

import warnings
warnings.filterwarnings("ignore")        
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
import seaborn as sns
import squarify

from components.header import *
from components.happiest import *
from components.happiest_comparison import *

#get data
df = pd.read_csv('world-happiness-report-2021.csv')
df2 = pd.read_csv('world-happiness-report.csv')
pop = pd.read_csv('population_by_country_2020.csv')

safety = df.copy()

# renaming columns for easier merge later
df.rename(columns={'Country name': 'Country'}, inplace=True)
df2.rename(columns={'Country name': 'Country'}, inplace=True)
pop.rename(columns={'Country (or dependency)': 'Country'}, inplace=True)

#might use later 
temporal = df2.groupby(['year','Country'])['Life Ladder'].mean().unstack().T
temporal = temporal.fillna(0).astype(int)

st.set_page_config(
    page_title="Home",
    page_icon="https://res.cloudinary.com/dhutys1vb/image/upload/v1685082988/hmik/favicon/android-chrome-192x192_bylewg.png",
)

st.title("World Happiness Visualization")

st.write(
    '''
    Selamat datang di visualisasi World Happiness yang bertujuan untuk menganalisa dan menampilkan beragam visualisasi terkait kebahagiaan negara negara yang terdapat di dunia, tidak hanya itu, visualisasi ini juga akan memberikan insight terkait apa saja yang mempengaruhi tingkat kebahagiaan sebuah negara.
    '''
)

st.subheader("World Index Visualization")
st.write(
    '''
    Pertama-tama mari lihat 10 negara paling bahagia dan 10 negara paling tidak bahagia
    '''
)

st.pyplot(headerVisualization())

past_winners = df2.loc[df2.groupby("year")["Life Ladder"].idxmax()]
past_bottom = df2.loc[df2.groupby("year")["Life Ladder"].idxmin()]

hap = df.groupby('Country')['Ladder score'].mean().sort_values(ascending=False)[:10]
unhap = df.groupby('Country')['Ladder score'].mean().sort_values(ascending=True)[:10]
top_bottom = hap.append(unhap, ignore_index=False).sort_values(ascending=True)

# Visualisasi kedua
st.pyplot(happiestVisualization(top_bottom))

st.subheader("Negara Bahagia vs Negara Tidak Bahagia")
st.write(
    '''
    Visualisasi di awal memberikan insight terkait 10 negara terbahagia dan 10 negara paling tidak bahagia, ditampilkan bahwa 9 dari 10 negara paling bahagia terletak di eropa sedangkan 7 dari 10 negara paling tidak bahagia terletak di Africa
    '''
)

st.subheader("Side by side comparison")
st.write(
    '''
    Agar lebih jelas maka mari visualisasikan perbandingan secara side by side antara 10 negara teratas dan 10 negara terbawah
    '''
)
# Visualisasi ketiga
st.pyplot(happiestComparisonVisualization(df))

st.subheader("Why?")
st.markdown(
    f'''
    Kenapa? Merupakan pertanyaan yang akan pertama kali timbul setelah melihat visualisasi diatas, mengapa negara yang terletak di Eropa cenderung lebih bahagia dan negara yang terletak di Afrika cenderung tidak bahagia?\nApa saja faktor yang dapat mempengaruhi hal-hal tersebut? Mari kita analisis lebih di halaman selanjutnya
    '''
)

