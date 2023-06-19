import streamlit as st
import numpy as np 
import pandas as pd 

import warnings
warnings.filterwarnings("ignore")        
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
import seaborn as sns

from components.changes import *

#get data
df = pd.read_csv('world-happiness-report-2021.csv')
df2 = pd.read_csv('world-happiness-report.csv')
pop = pd.read_csv('population_by_country_2020.csv')

safety = df.copy()

st.set_page_config(
    page_title="Changes",
    page_icon="https://res.cloudinary.com/dhutys1vb/image/upload/v1685082988/hmik/favicon/android-chrome-192x192_bylewg.png",
)

# renaming columns for easier merge later
df.rename(columns={'Country name': 'Country'}, inplace=True)
df2.rename(columns={'Country name': 'Country'}, inplace=True)
pop.rename(columns={'Country (or dependency)': 'Country'}, inplace=True)

st.title("Changes")
st.write(
    '''
    Pada halaman ini, akan dibahas terkait perubahan setiap negara setiap tahunnya, perubahan ini akan menampilkan bagaimana setiap negara berubah setiap tahunnya. Dataset yang digunakan kali ini merupakan kumpulan dari data kebahagiaan negara dari tahun 2005 hingga 2020. Lihatlah visualisasi dari perubahan beberapa negara paling bahagia dan paling tidak bahagia dibawah.
    '''
)

st.pyplot(changesLine(df2))

st.write(
    '''
    Setelah diperhatikan, negara yang kaya tetap kaya seiring perubahan waktu, namun negara yang miskin justru menjadi semakin miskin seiring perubahan waktu, sedangkan negara yang berada di tengah seperti Indonesia, mengalami beberapa lika liku namun tetap dapat bertahan di posisi tengah
    '''
)