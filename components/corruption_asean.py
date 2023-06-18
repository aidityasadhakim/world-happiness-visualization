import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def corruptionComparison(df):
    df.reset_index(inplace=True)
    background = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    ax.set_facecolor(background)
    sns.scatterplot(data=df, x='Freedom to make life choices', y='Perceptions of corruption',hue=df['Country'] == 'Indonesia',palette=cmap, alpha=0.9,ec='black',size=df["Ladder score"], legend=True, sizes=(5, 1000))

    ax.set_xlabel("Freedom",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Corruption",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)

    for i, txt in enumerate(df['Country']):
        ax.annotate(txt, (df['Healthy life expectancy'][i]+0.5, df['Ladder score'][i]),fontfamily='monospace')

    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace', fontsize = 20)
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Outside of Indonesia')
    L.get_texts()[2].set_text('Indonesia')
    L.get_texts()[3].set_text('Happiness Score')

    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 
    return fig
