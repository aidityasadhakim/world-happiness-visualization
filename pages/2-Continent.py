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

from components.continent import *

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

happiness_mean = df['Ladder score'].mean()

df['lower_happy'] = df['Ladder score'].apply(lambda x: 0 if x < happiness_mean else 1)

st.title('Continent Comparison')
st.subheader('Perbandingan Benua')

st.write(
    '''
    Selanjutnya kita akan membahas lebih lanjut terkait perbandingan antar benua
    mencari faktor-faktor tertinggi di setiap benua dan membandingkannya
    dengan satu sama lain
    '''
)

st.pyplot(continetComparison(df))

st.pyplot(factorComparison(df))

regionComparisonMap(df)