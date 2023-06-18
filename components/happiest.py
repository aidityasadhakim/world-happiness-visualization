import matplotlib.pyplot as plt

def happiestVisualization(top_bottom):
    low_c = '#dd4124'
    high_c = '#009473'
    plt.rcParams["font.family"] = "monospace"

    fig = plt.figure(figsize=(15,15),dpi=150)
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0.05, hspace=0.27)
    ax0 = fig.add_subplot(gs[0, 0])


    background_color = "#fafafa"
    fig.patch.set_facecolor(background_color) # figure background color
    ax0.set_facecolor(background_color) 

    # Plots 
    # Happiest
    data = top_bottom

    color_map = ['#e7e9e7' for _ in range(20)]
    color_map[0] = color_map[1] = color_map[2] =  low_c # color highlight
    color_map[17] = color_map[18] = color_map[19] =  high_c 
    #base
    ax0.barh(data.index, 10, 
        edgecolor='darkgray',color='lightgray',alpha=0.1)
    # actual
    ax0.barh(data.index, data, 
        edgecolor='darkgray',color=color_map)

    for i in range(0,20):
        ax0.annotate(list(data.index)[i], 
                    xy=(data[i]-(data[i]*0.01), i), 
                    va = 'center', ha='right',fontweight='light', fontfamily='monospace',fontsize=15, color='gray',rotation=0)
    # diff color text
    for i in range(0,3):
        ax0.annotate(list(data.index)[i], 
                    xy=(data[i]-(data[i]*0.01), i), 
                    va = 'center', ha='right',fontweight='light', fontfamily='monospace',fontsize=15, color='white',rotation=0)

    for i in range(17,20):
        ax0.annotate(list(data.index)[i], 
                    xy=(data[i]-(data[i]*0.01), i), 
                    va = 'center', ha='right',fontweight='light', fontfamily='monospace',fontsize=15, color='white',rotation=0)

    ax0.axes.get_xaxis().set_ticks([])
    ax0.axes.get_yaxis().set_ticks([])

    for s in ['top', 'bottom', 'right']:
        ax0.spines[s].set_visible(False)
        
    ax0.text(0,22.5,'The Happiest & Unhappiest Countries in the World',fontfamily='sans-serif',fontsize=20,fontweight='bold',color='#323232')
    ax0.text(0,21.3,'Pada visualisasi kedepan, kita akan menginvestigasi apa \nyang menjadi faktor dari tingkat kebahagiaan negara ini',fontfamily='monospace',fontsize=15,fontweight='light',color='gray')

    ax0.annotate('7 dari 10 terbawah \nterdapat di Benua Africa', xy=(4, 4.5), xytext=(6, 4.5), xycoords='data', 
                fontsize=15, ha='center', va='center',fontfamily='monospace',
                bbox=dict(boxstyle='round', fc=low_c),
                arrowprops=dict(arrowstyle='-[, widthB=12.3, lengthB=0.3', lw=1, color='gray'), color='white')
    
    return fig
