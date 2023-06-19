import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as grid_spec
import seaborn as sns

background = "#fbfbfb"
low_c = '#dd4124'
high_c = '#009473'

def populationComparison(df):    
    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    ax.set_facecolor(background)
    sns.scatterplot(data=df, x='Med. Age', y='Ladder score',hue=df['Regional indicator'] == 'Southeast Asia',palette=cmap, alpha=0.9,ec='black',linewidth=1.3,size=df["Population (2020)"]*1000, legend=True, sizes=(5, 2500))

    ax.set_xlabel("Median age",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Happiness Index Score",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)

    start, end = ax.get_xlim()
        
    ax.text(start,9.2,'Happiness Score, Median Age, and Population',fontfamily='sansserif',fontsize=17,weight='bold',color='#323232')
    ax.text(start,8.5,'It appears that the happier countries have older populations,\nand less people in general',fontfamily='monospace',fontweight='light',fontsize=12,color='gray')


    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Outside of ASEAN')
    L.get_texts()[2].set_text('ASEAN')
    L.get_texts()[3].set_text('Population')
    L.get_texts()[4].set_text('   25m')
    L.get_texts()[5].set_text('   50m')
    L.get_texts()[6].set_text('   75m')
    L.get_texts()[7].set_text('   100m')
    L.get_texts()[8].set_text('   125m+')


    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    return fig

def fertilityComparison(df):
    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    ax.set_facecolor(background)
    sns.scatterplot(data=df, x='Fert. Rate', y='Logged GDP per capita',hue=df['Regional indicator'] == 'Southeast Asia',palette=cmap, alpha=0.9,ec='black',linewidth=1.3,size=df["Med. Age"], legend=True, sizes=(5, 500))

    ax.set_xlabel("Fertility rate",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("GDP p/Capita [log]",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)

    start, end = ax.get_xlim()
        
    ax.text(start,12.7,'GDP, Fertility Rate, and Median Age',fontfamily='sansserif',fontsize=17,weight='bold',color='#323232')
    ax.text(start,12.3,'Bringing all the above together, we see that these features are all linked',fontfamily='monospace',fontweight='light',fontsize=12,color='gray')


    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Outside of ASEAN')
    L.get_texts()[2].set_text('ASEAN')
    L.get_texts()[3].set_text('Median Age')
    #L.get_texts()[4].set_text('   25m')


    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    return fig

def densityComparison(df):
    happiness_mean = df['Ladder score'].mean()

    df['lower_happy'] = df['Ladder score'].apply(lambda x: 0 if x < happiness_mean else 1)
    
    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    ax.set_facecolor(background)

    cmap = [low_c,high_c]

    df_plot = df[df['density_quantile'] <9 ]

    sns.scatterplot(data=df_plot, x="Density (P/Km²)", y="Ladder score", hue=df['lower_happy'],palette=cmap, size=df_plot["Population (2020)"]*1000, legend=True, sizes=(5, 2500),alpha=0.9,ec='black',linewidth=1.5)

    ax.set_xlabel("Population density (p/km²)",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Happiness Index Score",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)

    start, end = ax.get_xlim()
        
    ax.text(start,9.35,'Happiness, Population, and Population Density',fontfamily='sansserif',fontsize=17,weight='bold',color='#323232')
    ax.text(start,8.7,'There does not seem to be a relationshop between happiness\nand population density',fontfamily='monospace',fontweight='light',fontsize=12,color='gray')

    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Below Average Happiness')
    L.get_texts()[2].set_text('Above')
    L.get_texts()[3].set_text('Population')
    L.get_texts()[4].set_text('   25m')
    L.get_texts()[5].set_text('   50m')
    L.get_texts()[6].set_text('   75m')
    L.get_texts()[7].set_text('   100m')
    L.get_texts()[8].set_text('   125m+')

    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    return fig