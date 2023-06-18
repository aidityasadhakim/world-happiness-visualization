import matplotlib.pyplot as plt
import seaborn as sns


def lifeExpectancyVisualization(df):
    background = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    ax.set_facecolor(background)
    sns.scatterplot(data=df, x='Healthy life expectancy', y='Ladder score',hue=df['Regional indicator'] == 'Western Europe',palette=cmap, alpha=0.9,ec='black',size=df["Logged GDP per capita"]*1000, legend=True, sizes=(5, 500))

    ax.set_xlabel("Life Expectancy",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Happiness Index Score",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)
        
    ax.text(45,9.2,'Happiness Score, Life Expectancy, and GDP per Capita',fontfamily='sansserif',fontsize=17,weight='bold',color='#323232')
    ax.text(45,8.5,'Dapat dilihat bahwa negara yang berada di Eropa memiliki tingkat kebahagiaan yang lebih tinggi \nNegara yang memiliki nilai GDP perkapita rendah memiliki tingkat kebahagiaan yang rendah',fontfamily='monospace',fontweight='light',fontsize=12,color='gray')


    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Outside of Europe')
    L.get_texts()[2].set_text('Europe')
    L.get_texts()[3].set_text('GDP p/Capita [log]')


    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    return fig