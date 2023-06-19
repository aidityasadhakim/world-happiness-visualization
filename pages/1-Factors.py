import streamlit as st
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

from components.life_expectancy import lifeExpectancyVisualization
from components.african_comparison import africanComparisonVisualization
from components.corruption import *

st.set_page_config(
    page_title="Factors",
    page_icon="https://res.cloudinary.com/dhutys1vb/image/upload/v1685082988/hmik/favicon/android-chrome-192x192_bylewg.png",
)

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

st.title("The Factors and differences")

# Visualisasi 1
st.subheader(
            '''
            Benua Eropa dan perbandingannya
            ''')
st.write(
    '''
         Setelah memperhatikan hasil dari urutan negara bahagia di halaman utama
         kita dapat melihat bahwa Benua Eropa menduduki tingkat teratas dalam indeks kebahagiaan
         sekarang, mari kita lihat perbandingannya.
    ''')

st.pyplot(lifeExpectancyVisualization(df))

# Visualisasi 2
st.subheader(
            '''
            Benua Afrika dan perbandingannya
            ''')
st.write(
    '''
         Selanjutnya kita ketahui bahwa 7 dari 10 negara terbawah
         diisi oleh negara yang terdapat di Benua Afrika, sekarang
         mari kita lihat perbandingannya.
    ''')

st.pyplot(africanComparisonVisualization(df))

# Visualisasi 3
st.subheader(
    '''
        Corruption vs Freedom of choice
    '''
)

st.write(
    '''
         Selanjutnya kita akan menganalisa perbandingan diantara
         tingkat korupsi dan tingkat kebebasan dalam memilih yang juga
         tentunya akan kita bandingkan dengan tingkat kebahagiaan
    ''')

st.pyplot(corruptionComparison(df))