import streamlit as st
import numpy as np 
import pandas as pd 

import warnings
warnings.filterwarnings("ignore")        
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
import seaborn as sns

from components.population import *

#get data
df = pd.read_csv('world-happiness-report-2021.csv')
df2 = pd.read_csv('world-happiness-report.csv')
pop = pd.read_csv('population_by_country_2020.csv')

safety = df.copy()

st.set_page_config(
    page_title="Population",
    page_icon="https://res.cloudinary.com/dhutys1vb/image/upload/v1685082988/hmik/favicon/android-chrome-192x192_bylewg.png",
)

# renaming columns for easier merge later
df.rename(columns={'Country name': 'Country'}, inplace=True)
df2.rename(columns={'Country name': 'Country'}, inplace=True)
pop.rename(columns={'Country (or dependency)': 'Country'}, inplace=True)

# merge on country
df = pd.merge(df, pop, on='Country')
# removing NA value

df=df[df['Urban Pop %'] != 'N.A.']

# Changing data types, removing % strings etc

df['Urban Pop %'] = df['Urban Pop %'].str.rstrip('%').astype('float') / 100.0
df['World Share'] = df['World Share'].str.rstrip('%').astype('float') / 100.0
df['Yearly Change'] = df['Yearly Change'].str.rstrip('%').astype('float') / 100.0
df['Fert. Rate'] = df['Fert. Rate'].astype('float')
df['Med. Age'] = df['Med. Age'].astype('float')

# Adding in some bins

df['Count'] = 1
df['pop_quantile'] = pd.qcut(df['Population (2020)'], 10, labels=False)
df['density_quantile'] = pd.qcut(df['Density (P/Km²)'], 10, labels=False)

merge_safety = df

st.title("Population Visualization")
st.write(
    '''
    Pada visualisasi halaman ini akan berfokus kepada visualisasi dengan
    penambahan dataset berupa total populasi di tahun 2020 dari setiap negara.
    '''
)
st.subheader("Happiness vs Median Age vs Population")
st.write(
    '''
    Perbandingan dari total populasi, rata2 umur dan juga tingkat kebahagiaan divisualisasikan sehingga perbandingan dan korelasi dari setiap fiturnya dapat dilihat di bawah.
    '''
)

# Visualisasi
st.pyplot(populationComparison(df))

st.write(
    '''
    Seperti yang dapat dilihat negara yang lebih bahagia cenderung memiliki masyarakat yang lebih tua dan lebih sedikit.\n
    Kami juga memberikan benua eropa sebagai perbandingan.
    '''
)

st.subheader("Happiness vs Median Age vs Fertility Rate")
st.write(
    '''
    Perbandingan selanjutnya membandingkan antara tingkat kebahagiaan, rata2 umur dan juga angka kelahiran. Hal ini dibandingkan untuk menemukan apakah sebuah negara dengan tingkat kelahiran yang tinggi dapat meningkatkan kebahagiaan atau tidak.\n
    '''
)

st.pyplot(fertilityComparison(df))

st.write(
    '''
    Berkaitan dengan visualisasi sebelumnya, hal yang berkaitan dengan tingkat populasi ataupun pertumbuhan berkaitan dalam mempengaruhi tingkat kebahagiaan sebuah negara
    '''
)

st.subheader("Happiness vs Density")
st.write(
    '''
    Selanjutnya kami mencoba melihat bagaimana pengaruh kepadatan penduduk suatu negara mempengaruhi tingkat kebahagiaan sebuah negara, sebelumnya telah diketahui bahwa peningkatan populasi dan jumlah populasi mempengaruhi tingkat kebahagiaan sebuah negara, maka dapat ditebak bahwa seharusnya tingkat kepadatan penduduk juga berpengaruh.
    '''
)

st.pyplot(densityComparison(df))

st.write(
    '''
    Mengejutkannya, kepadatan penduduk tidak mempengaruhi tingkat kebahagiaan sebuah negara.
    '''
)