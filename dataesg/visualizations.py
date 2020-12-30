from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

style.use('fivethirtyeight')

def barchart(df, x, metric,
             stacked  = True,
             title    = 'Bar Chart',
             legend   = True,
            ):

    if x=='Fiscal_Year':
        group_name = 'Fiscal_Year'
        type_name = 'Ticker'
    else: 
        group_name = x
        type_name = 'Fiscal_Year'

    df.sort_values(by=group_name,inplace=True)
    group_labels = df[group_name].unique().tolist()
    group_count = len(df[group_name].unique().tolist())
    type_labels = df[type_name].unique().tolist()
    type_count = len(df[type_name].unique().tolist())
    index = np.arange(group_count)

    size = .5
    _width = .7 if stacked else .8/type_count
    x_ticks_loc = index if stacked else index + _width*(type_count-1)*.5
    figsize_x = 2.5*(group_count+(type_count*(not stacked)))*size
    figsize_y = 12 * size
    color_palette = ['#1D455F','#00AEB7','#FFBD2E','#6F2C83','#00AEB7','#D9D9D9','#373F51','#F0C808','lightgreen','orangered','teal','yellowgreen']*10
    _, ax = plt.subplots(figsize=(figsize_x,figsize_y))
    bar_space = .00
    if not stacked:
        for (i, _type) in enumerate(type_labels):
            values =  []
            for label in group_labels:
                d = df[df[group_name]==label]
                for _,x in d.iterrows():
                    if x[type_name] == _type:
                        value = x[metric]
                        break 
                    else:
                        value = 0 
                values.append(value)
        
            ax.bar(index + (_width * i) + (bar_space * i),
               values,
               width = _width,
               color = color_palette[i],
               label = _type)

    bottom_temp = [0] * group_count
    if stacked:
        for (i, _type) in enumerate(type_labels):
            values =  []
            for label in group_labels:
                d = df[df[group_name]==label]
                for _,x in d.iterrows():
                    if x[type_name] == _type:
                        value = x[metric]
                        break 
                    else:
                        value = 0 
                values.append(value)
            ax.bar(index,
                values,
                width = _width,
                color = color_palette[i],
                label = _type,
                bottom = bottom_temp
                    )  
            values_temp = df[metric][df[type_name] == _type].values.tolist()
            bottom_temp = [values[i]+bottom_temp[i] for i in range(group_count)]
            for i,x in enumerate(bottom_temp):
                if str(x) == 'nan':
                    bottom_temp[i] = 0

    ax.grid(color='black', linestyle=':', linewidth=1.5*size, alpha = .3)
    ax.xaxis.grid(False)
    yloc = plt.MaxNLocator(10)
    ax.yaxis.set_major_locator(yloc)
    ax.set_axisbelow(True)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_edgecolor('#2B2D42')
    plt.xticks(x_ticks_loc, group_labels)
    ax.set_ylabel(metric)
    ttl = ax.set_title(title, color = '#2B2D42', fontsize = 18*size*1.6)
    for item in ([ax.xaxis.label, ax.yaxis.label] + #ax.title, 
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(22*size)
        item.set_fontname('Helvetica')
    if legend:
        lg = ax.legend(ncol = type_count, loc = 'upper center', bbox_to_anchor=(0.5, -.03), frameon = False, fontsize = 22*size)
        plt.setp(lg.get_texts(), color='#2B2D42')
    plt.show()


def piechart(df,metric,title='Pie Chart',exploded=None):
    df = df[['Fiscal_Year',metric]]
    df.dropna(axis=0,inplace=True)
    x = df[metric]
    labels = df['Fiscal_Year']
    colors = ['#00AEB7','#FFBD2E','#6F2C83','#1D455F','beige','lightgreen','orangered','teal','yellowgreen','salmon']
    patches=  plt.pie(x,
                     labels=labels,
                     colors=colors,
                     startangle=90,
                     shadow= True,
                     explode=[0.05]*len(x),
                     autopct='%1.1f%%'
                     )
    plt.title(title)
    plt.show()


def graph(df, x, metric,
             title = 'Graph',
             legend = True,
            ):

    group_name = x
    type_name = 'Ticker'
    size = 0.5
    df.sort_values(by=group_name,inplace=True)
    group_labels = df[group_name].unique().tolist()
    group_count = len(df[group_name].unique().tolist())
    type_labels = df[type_name].unique().tolist()
    type_count = len(df[type_name].unique().tolist())
    index = np.arange(group_count)
    x_ticks_loc = index

    figsize_x = 1.5*group_count
    figsize_y = 12 * size

    colors = ['#1D455F','#00AEB7','#FFBD2E','#6F2C83','#00AEB7','#D9D9D9','#373F51','#F0C808','lightgreen','orangered','teal','yellowgreen']*10
    _, ax = plt.subplots(figsize=(figsize_x,figsize_y))
    bar_space = .00
    for (i, _type) in enumerate(type_labels):
        values =  []
        for label in group_labels:
            d = df[df[group_name]==label]
            for _,x in d.iterrows():
                if x[type_name] == _type:
                    value = x[metric]
                    break 
                else:
                    value = None
            values.append(value)
        ax.plot(index, values,color=colors[i],label=_type,marker='o')


    ax.grid(color='black', linestyle=':', linewidth=1.5*size, alpha = .3)
    ax.xaxis.grid(False)
    yloc = plt.MaxNLocator(10)
    ax.yaxis.set_major_locator(yloc)
    ax.set_axisbelow(True)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_edgecolor('#2B2D42')
    plt.xticks(x_ticks_loc, group_labels)
    ax.set_ylabel(metric)
    ttl = ax.set_title(title,color = '#2B2D42', fontsize = 18*size*1.6)
    for item in ([ax.xaxis.label, ax.yaxis.label] + #ax.title, 
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(22*size)
        item.set_fontname('Helvetica')
    if legend:
        lg = ax.legend(ncol = type_count, loc = 'upper center', bbox_to_anchor=(0.5, -.03), frameon = False, fontsize = 22*size)
        plt.setp(lg.get_texts(), color='#2B2D42')
    plt.show()