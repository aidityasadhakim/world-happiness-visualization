import matplotlib.pyplot as plt


def headerVisualization():
    low_c = '#dd4124'
    high_c = '#009473'
    plt.rcParams["font.family"] = "monospace"

    fig = plt.figure(figsize=(6,3),dpi=150)
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0.2, hspace=0.4)
    ax0 = fig.add_subplot(gs[0, 0])

    background_color = "#fafafa"
    fig.patch.set_facecolor(background_color) # figure background color
    ax0.set_facecolor(background_color) 

    ax0.text(1.167,0.85,"2021 World Happiness Index",color='#323232',fontsize=22, fontweight='bold', fontfamily='sanserif',ha='center')
    ax0.text(1.13,-0.35,"stand-out facts",color='lightgray',fontsize=22, fontweight='bold', fontfamily='monospace',ha='center')

    ax0.text(0,0.4,"Finland",color=high_c,fontsize=20, fontweight='bold', fontfamily='monospace',ha='center')
    ax0.text(0,0.1,"Happiest",color='gray',fontsize=10, fontfamily='monospace',ha='center')

    ax0.text(0.77,0.4,"9 of top 10",color=high_c,fontsize=20, fontweight='bold', fontfamily='monospace',ha='center')
    ax0.text(0.75,0.1,"in Europe",color='gray',fontsize=10, fontfamily='monospace',ha='center')

    ax0.text(1.5,0.4,"7 of bottom 10",color=low_c,fontsize=20, fontweight='bold', fontfamily='monospace',ha='center')
    ax0.text(1.5,0.1,"in Africa",color='gray',fontsize=10, fontfamily='monospace',ha='center')

    ax0.text(2.25,0.4,"Afghanistan",color=low_c,fontsize=20, fontweight='bold', fontfamily='monospace',ha='center')
    ax0.text(2.25,0.1,"Unhappiest",color='gray',fontsize=10, fontfamily='monospace',ha='center')

    ax0.set_yticklabels('')
    ax0.set_xticklabels('')
    ax0.tick_params(axis='both',length=0)

    for s in ['top','right','left','bottom']:
        ax0.spines[s].set_visible(False)
        
    import matplotlib.lines as lines
    l1 = lines.Line2D([0.15, 1.95], [0.67, 0.67], transform=fig.transFigure, figure=fig,color = 'gray', linestyle='-',linewidth = 1.1, alpha = .5)
    fig.lines.extend([l1])
    l2 = lines.Line2D([0.15, 1.95], [0.07, 0.07], transform=fig.transFigure, figure=fig,color = 'gray', linestyle='-',linewidth = 1.1, alpha = .5)
    fig.lines.extend([l2])
    
    return fig
