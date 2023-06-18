import matplotlib.pyplot as plt
import seaborn as sns


def lifeExpectancyVisualization(df):
    df.reset_index(inplace=True)
    background = "#fbfbfb"
    low_c = '#dd4124'
    high_c = '#009473'

    fig, ax = plt.subplots(1,1, figsize=(10, 5),dpi=150)
    fig.patch.set_facecolor(background) # figure background color

    cmap = [low_c,high_c]

    ax.set_facecolor(background)
    sns.scatterplot(data=df, x='Healthy life expectancy', y='Ladder score',hue=df['Country'] == 'Indonesia',palette=cmap, alpha=0.9,ec='black',size=df["Logged GDP per capita"]*1000, legend=True, sizes=(5, 1000))

    ax.set_xlabel("Life Expectancy",fontfamily='monospace',loc='left',color='gray')
    ax.set_ylabel("Happiness Index Score",fontfamily='monospace',loc='top',color='gray')
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

    for s in ["top","right","left"]:
        ax.spines[s].set_visible(False)

    for i, txt in enumerate(df['Country']):
        ax.annotate(txt, (df['Healthy life expectancy'][i]+0.5, df['Ladder score'][i]),fontfamily='monospace')

    L = ax.legend(frameon=False,loc="upper center", bbox_to_anchor=(1.25, 0.8), ncol= 1)
    plt.setp(L.texts, family='monospace')
    L.get_frame().set_facecolor('none')
    L.get_texts()[1].set_text('Outside of Indonesia')
    L.get_texts()[2].set_text('Indonesia')
    L.get_texts()[3].set_text('GDP p/Capita [log]')

    ax.tick_params(axis='both', which='both',left=False, bottom=False,labelbottom=True) 

    return fig