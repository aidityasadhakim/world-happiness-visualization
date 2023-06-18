import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def corruptionComparison(df):
    background = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    ax.set_facecolor(background)
    sns.scatterplot(data=df, x='Freedom to make life choices', y='Perceptions of corruption',hue=df['Regional indicator'] == 'Western Europe',palette=cmap, alpha=0.9,ec='black',size=df["Ladder score"], legend=True, sizes=(5, 600))

    ax.set_xlabel("Freedom",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Corruption",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)

    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Outside of Europe')
    L.get_texts()[2].set_text('Europe')
    L.get_texts()[3].set_text('Happiness Score')

    start, end = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(0, end+0.2, 0.2))



    ax.text(0.31,1.155,'Happiness Score, Freedom, and Corruption',fontfamily='sansserif',fontsize=17,weight='bold',color='#323232')
    ax.text(0.31,1.1,'Lower corruption, higher freedom, higher happiness?',fontfamily='monospace',fontweight='light',fontsize=12,color='gray')


    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    ax.text(0.4,0.1,
    '''
    Seperti yang terlihat, kebebasan
    dan korupsi berbanding terbalik.
    
    Dapat dilihat juga, ketika korupsi
    menurun, kebebebasan meningkat begitu
    juga dengan kebahagiaanya
    ''',fontfamily='monospace',fontsize=10,color='gray')

    return fig