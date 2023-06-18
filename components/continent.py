import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import geopandas
import matplotlib.colors
import pycountry
import pandas as pd
import streamlit as st

def continetComparison(df):
    background = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    continent_score = df.groupby('Regional indicator')['Healthy life expectancy','Logged GDP per capita','Perceptions of corruption','Freedom to make life choices','Ladder score'].mean().reset_index()

    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    color_map = ['#e7e9e7' for _ in range(10)]
    color_map[9] =  high_c # color highlight
    color_map[5] =  high_c
    color_map[8] =  low_c
    color_map[6] =  low_c

    ax.set_facecolor(background)
    sns.scatterplot(data=continent_score, x=continent_score['Healthy life expectancy'], y=continent_score['Ladder score'],hue=continent_score['Regional indicator'], alpha=0.9,ec='black',palette=color_map,size=df["Ladder score"], legend=False, sizes=(5, 600))

    ax.set_xlabel("Life Expectancy",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Happiness Index Score",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)
        
    ax.text(55,7.5,'Happiness Score & Life Expectancy by Continent',fontfamily='sansserif',fontsize=17,weight='bold',color='#323232')
    ax.text(55,7.3,'There are clear distinctions, with four stand-out continents',fontfamily='monospace',fontweight='light',fontsize=12,color='gray')

    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')

    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    for i, txt in enumerate(continent_score['Regional indicator']):
        ax.annotate(txt, (continent_score['Healthy life expectancy'][i]+0.5, continent_score['Ladder score'][i]),fontfamily='monospace')
        
    return fig

def factorComparison(df):
    background = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    continent_score = df.groupby('Regional indicator')['Healthy life expectancy','Logged GDP per capita','Perceptions of corruption','Freedom to make life choices','Ladder score'].mean().reset_index().mean().sort_values(ascending=True)[:10]
    df_bottom = df.groupby('Country')['Logged GDP per capita','Perceptions of corruption','Freedom to make life choices','Social support','Ladder score'].mean().sort_values(by='Ladder score',ascending=True)[:10]

    df_bottom['Logged GDP per capita'] = df_bottom['Logged GDP per capita']/10
    df_bottom['Ladder score'] = df_bottom['Ladder score']/5

    categorical = [var for var in df.columns if df[var].dtype=='O']
    continuous = [var for var in df.columns if df[var].dtype!='O']

    #refined
    continuous = ['Logged GDP per capita',
    'Social support',
    'Healthy life expectancy',
    'Freedom to make life choices',
    'Generosity',
    'Perceptions of corruption']

    background_color = '#fbfbfb'
    fig = plt.figure(figsize=(12, 6), dpi=150,facecolor=background_color)
    gs = fig.add_gridspec(2, 3)
    gs.update(wspace=0.2, hspace=0.5)

    plot = 0
    for row in range(0, 2):
        for col in range(0, 3):
            print("ax"+str(plot))
            locals()["ax"+str(plot)] = fig.add_subplot(gs[row, col])
            locals()["ax"+str(plot)].set_facecolor(background_color)
            locals()["ax"+str(plot)].tick_params(axis='y', left=False)
            locals()["ax"+str(plot)].get_yaxis().set_visible(False)
            locals()["ax"+str(plot)].set_axisbelow(True)
            for s in ["top","right","left"]:
                locals()["ax"+str(plot)].spines[s].set_visible(False)
            plot += 1

    plot = 0

    Yes = df[df['lower_happy'] == 1]
    No = df[df['lower_happy'] == 0]

    for variable in continuous:
            sns.kdeplot(Yes[variable], ax=locals()["ax"+str(plot)], color=high_c,ec='black', shade=True, linewidth=1.5, alpha=0.9, zorder=3, legend=False)
            sns.kdeplot(No[variable],ax=locals()["ax"+str(plot)], color=low_c, shade=True, ec='black',linewidth=1.5, alpha=0.9, zorder=3, legend=False)
            locals()["ax"+str(plot)].grid(which='major', axis='x', zorder=0, color='gray', linestyle=':', dashes=(1,5))
            locals()["ax"+str(plot)].set_xlabel(variable, fontfamily='monospace')
            plot += 1
            
    Xstart, Xend = locals()['ax0'].get_xlim()
    Ystart, Yend = locals()['ax0'].get_ylim()

    locals()['ax0'].text(Xstart, Yend+(Yend*0.5), 'Differences between happy & unhappy countries', fontsize=17, fontweight='bold', fontfamily='sansserif',color='#323232')
    locals()['ax0'].text(Xstart, Yend+(Yend*0.25), 'There are large differences, with GDP & Social Support being clear\nperhaps more interesting though, unhappy countries appear to be more generous', fontsize=12, fontweight='light', fontfamily='monospace',color='gray')

    return fig

def regionComparisonMap(df):
    background_color = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    #data prep
    geo_temp = df

    #source: https://melaniesoek0120.medium.com/data-visualization-how-to-plot-a-map-with-geopandas-in-python-73b10dcd4b4b

    def alpha3code(column):
        CODE=[]
        for country in column:
            try:
                code=pycountry.countries.get(name=country).alpha_3
            # .alpha_3 means 3-letter country code 
            # .alpha_2 means 2-letter country code
                CODE.append(code)
            except:
                CODE.append('None')
        return CODE
    # create a column for code 
    geo_temp['CODE']=alpha3code(geo_temp['Country'])


    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    world.columns=['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']
    merge=pd.merge(world,geo_temp,on='CODE')


    ###

    # Custom colour map
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [low_c,high_c])

    ax = world.plot(figsize=(20,15), linewidth=0.25, edgecolor=background_color, color='lightgray')
    ax.axis('off')
    ax.set_facecolor(background_color)
    merge.plot(column='lower_happy',figsize=(20, 15),legend=False,cmap=cmap,ax=ax)


    ax.text(-175,112,'Where are the happiest countries?',fontsize=30,fontweight='bold',fontfamily='sansserif',color='#323232')
    ax.text(-175,102,'We clearly see where the happy & unhappy countries are',color='gray',fontfamily='monospace',fontsize=20)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    # return ax