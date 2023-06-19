import streamlit as st
import numpy as np 
import pandas as pd 

import warnings
warnings.filterwarnings("ignore")        
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
import seaborn as sns

from components.life_expectancy_asean import lifeExpectancyVisualization
from components.corruption_asean import *

st.set_page_config(
    page_title="ASEAN",
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

df3 = df.loc[df['Regional indicator'] == "Southeast Asia"]

# df3 = df[df["Regional indicator" == "Southeast Asia"]]

st.title("The Factors and differences")

# Visualisasi 1
st.subheader(
            '''
            Perbandingan pada benua Asia Tenggara
            ''')
st.write(
    '''
         Selanjutnya kita akan mencoba memvisualisasikan data kebahagiaan
         pada negara yang terletak di area Asia Tenggara
    ''')

st.pyplot(lifeExpectancyVisualization(df3))

# Visualisasi 2
st.subheader(
    '''
        Corruption vs Freedom of choice
    '''
)

st.write(
    '''
         Dibawah ini merupakan perbandingan data kebahagiaan,
         kebebasan memilih dan tingkat korupsi di negara Asean
    ''')

st.pyplot(corruptionComparison(df3))