import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

background_color = "#fbfbfb"
low_c = '#dd4124'
high_c = '#009473'
mid_c = '#ffff00'


def changesLine(df2):
    import matplotlib.dates as mdates

    fig = plt.figure(figsize=(10, 4), dpi=150,facecolor=background_color)
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0, hspace=0)
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.set_facecolor(background_color)
    for s in ["right", "top"]:
        ax0.spines[s].set_visible(False)
        
    ax0.set_xlabel("Year",fontfamily='monospace',loc='left',color='gray')
    ax0.set_ylabel("Happiness Index Score",fontfamily='monospace',loc='top',color='gray')
    ax0.tick_params(axis = 'both', which = 'major', labelsize = 10)
        


    ax0.tick_params(axis='both', which='both', left=False, bottom=False,labelbottom=True) 

    #low
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Zimbabwe')], x='year', y='Life Ladder',color='lightgray')
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Rwanda')], x='year', y='Life Ladder',color='lightgray')
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Afghanistan')], x='year', y='Life Ladder',color=low_c)

    #high
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Denmark')], x='year', y='Life Ladder',color='lightgray')
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Switzerland')], x='year', y='Life Ladder',color='lightgray')
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Finland')], x='year', y='Life Ladder',color=high_c)

    #Indonesia
    sns.lineplot(ax=ax0,data=df2[(df2['Country']=='Indonesia')], x='year', y='Life Ladder',color=mid_c)


    Xstart, Xend = ax0.get_xlim()
    Ystart, Yend = ax0.get_ylim()
    ax0.plot(2019,df2[(df2['Country']=='Afghanistan')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=low_c, markeredgewidth=1.5)
    ax0.plot(2020,df2[(df2['Country']=='Zimbabwe')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=low_c, markeredgewidth=1.5)
    ax0.plot(2019,df2[(df2['Country']=='Rwanda')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=low_c, markeredgewidth=1.5)

    ax0.plot(2019,df2[(df2['Country']=='Indonesia')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=mid_c, markeredgewidth=1.5)

    ax0.plot(2020,df2[(df2['Country']=='Finland')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=high_c,markeredgewidth=1.5)
    ax0.plot(2020,df2[(df2['Country']=='Denmark')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=high_c, markeredgewidth=1.5)
    ax0.plot(2020,df2[(df2['Country']=='Switzerland')]['Life Ladder'].reset_index().iloc[-1,-1], 'ko', markersize=10, fillstyle='full',color=high_c, markeredgewidth=1.5)


    ax0.text(2020.2,df2[(df2['Country']=='Finland')]['Life Ladder'].reset_index().iloc[-1,-1],'Finland',color=high_c,fontfamily='monospace',fontsize=8, rotation=0)
    ax0.text(2020.2,df2[(df2['Country']=='Denmark')]['Life Ladder'].reset_index().iloc[-1,-1],'Denmark',color=high_c,fontfamily='monospace',fontsize=8, rotation=0)
    ax0.text(2020.2,df2[(df2['Country']=='Switzerland')]['Life Ladder'].reset_index().iloc[-1,-1]-0.35,'Switzerland',color=high_c,fontfamily='monospace',fontsize=8, rotation=0)

    ax0.text(2020.2,df2[(df2['Country']=='Indonesia')]['Life Ladder'].reset_index().iloc[-1,-1]-0.35,'Indonesia',color='black',fontfamily='monospace',fontsize=8, rotation=0)

    ax0.text(2019.2,df2[(df2['Country']=='Afghanistan')]['Life Ladder'].reset_index().iloc[-1,-1],'Afghanistan',color=low_c,fontfamily='monospace',fontsize=8, rotation=0)
    ax0.text(2020.2,df2[(df2['Country']=='Zimbabwe')]['Life Ladder'].reset_index().iloc[-1,-1],'Zimbabwe',color=low_c,fontfamily='monospace',fontsize=8, rotation=0)
    ax0.text(2019.2,df2[(df2['Country']=='Rwanda')]['Life Ladder'].reset_index().iloc[-1,-1],'Rwanda',color=low_c,fontfamily='monospace',fontsize=8, rotation=0)



    ax0.yaxis.set_ticks(np.arange(0, 10, 1))
    ax0.set_xlim(left = 2008, right = 2020.5)
    plt.xticks(fontname = "monospace")
    plt.yticks(fontname = "monospace")

    Xstart, Xend = ax0.get_xlim()
    Ystart, Yend = ax0.get_ylim()

    ax0.text(Xstart, Yend+(Yend*0.2), 'Changes over time', fontsize=17, fontweight='bold', fontfamily='sansserif',color='#323232')

    return fig