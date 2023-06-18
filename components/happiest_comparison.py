import matplotlib.pyplot as plt

def happiestComparisonVisualization(df):
    low_c = '#dd4124'
    high_c = '#009473'

    fig = plt.figure(figsize=(22,10),dpi=150)
    gs = fig.add_gridspec(1, 2)
    gs.update(wspace=0.05, hspace=0.27)
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])


    background_color = "#fafafa"
    fig.patch.set_facecolor(background_color) # figure background color
    ax0.set_facecolor(background_color) 
    ax1.set_facecolor(background_color) 


    # Plots 
    # Happiest
    data = df.groupby('Country')['Ladder score'].mean().sort_values(ascending=False)[:10]


    color_map = ['#e7e9e7' for _ in range(10)]
    color_map[0] = color_map[1] = color_map[2] =  high_c # color highlight

    #base
    ax0.barh(data.index, 10, 
        edgecolor='darkgray',color='lightgray',alpha=0.1)
    # actual
    ax0.barh(data.index, data, 
        edgecolor='darkgray',color=color_map)


    #annotations
    #for i in data.index:
    #   ax.annotate(f"{round(data[i],3)}", 
    #                 xy=(data[i] + 0.5,i), #i like to change this to roughly 5% of the highest cat
    #                va = 'center', ha='right',fontweight='light', fontfamily='serif',fontsize=12)
    for i in range(0,10):
        ax0.annotate(list(data.index)[i], 
                    xy=(data[i]-(data[i]*0.01), i), 
                    va = 'center', ha='right',fontweight='light', fontfamily='monospace',fontsize=15, color='gray',rotation=0)
    # diff color text
    for i in range(0,3):
        ax0.annotate(list(data.index)[i], 
                    xy=(data[i]-(data[i]*0.01), i), 
                    va = 'center', ha='right',fontweight='light', fontfamily='monospace',fontsize=15, color='white',rotation=0)
        
    # Unhappiest

    data = df.groupby('Country')['Ladder score'].mean().sort_values(ascending=True)[:10]

    color_map = ['#e7e9e7' for _ in range(10)]
    color_map[0] = color_map[1] = color_map[2] =  low_c # color highlight

    #base
    ax1.barh(data.index[::-1], 10, 
        edgecolor='darkgray',color='lightgray',alpha=0.1)
    # actual
    ax1.barh(data.index, data, 
        edgecolor='darkgray',color=color_map)


    #annotations
    #for i in data.index:
    #   ax.annotate(f"{round(data[i],3)}", 
    #                 xy=(data[i] + 0.5,i), #i like to change this to roughly 5% of the highest cat
    #                va = 'center', ha='right',fontweight='light', fontfamily='serif',fontsize=12)
    for i in range(7,10):
        ax1.annotate(list(data.index)[::-1][i], 
                    xy=(data[::-1][i]-(data[::-1][i]*0.01), i), 
                    va = 'center', ha='left',fontweight='light', fontfamily='monospace',fontsize=15, color='white',rotation=0)
    # diff color text
    for i in range(0,7):
        ax1.annotate(list(data.index)[::-1][i], 
                    xy=(data[::-1][i]-(data[::-1][i]*0.01), i), 
                    va = 'center', ha='left',fontweight='light', fontfamily='monospace',fontsize=15, color='gray',rotation=0)

        


    # Remove border from plot

    for s in ['top', 'bottom', 'right']:
        ax0.spines[s].set_visible(False)
        
    for s in ['top', 'bottom', 'right','left']:    
        ax1.spines[s].set_visible(False)
        


        
    ax0.set_xlim(0,10)
    ax1.set_xlim(10,0)
        
    # ax labels off

    ax0.axes.get_xaxis().set_ticks([])
    ax0.axes.get_yaxis().set_ticks([])
    ax1.axes.get_xaxis().set_ticks([])
    ax1.axes.get_yaxis().set_ticks([])

    ax0.text(0,10.8,'The Happiest & Unhappiest Countries in the World: Side-by-side',fontfamily='sans-serif',fontsize=20,fontweight='bold',color='#323232')
    ax0.text(0,10.3,'Pada visualisasi kedepan, kita akan menginvestigasi apa yang menjadi faktor dari tingkat kebahagiaan negara ini',fontfamily='monospace',fontsize=15,fontweight='light',color='gray')

    # rect
    from matplotlib.patches import Rectangle
    X, Y = 0, 6.5


    ax1.add_patch(Rectangle((X, Y), 10, 3,alpha=0.2, edgecolor='gray',facecolor='gray'))

    fig.text(0.53,0.72,
            
    '''
    Apa yang membuat negara
    ini menjadi negara yang
    tampil di urutan terakhir

    ''',color='black',fontfamily='monospace',fontsize=12)
    
    return fig