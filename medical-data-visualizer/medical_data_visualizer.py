import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
BMI = df['weight'] / (df['height']/100)**2
df['overweight'] = BMI.apply(lambda x: 1 if x > 25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = None, 
                     value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                     var_name = None,
                     value_name = 'value',
                     ignore_index = False)



    # 6
    df_cat = df_cat.join(df['cardio']).groupby('cardio').value_counts().rename('total').reset_index().sort_values(by = ['cardio', 'variable'])
    

    # 7



    # 8
    g = sns.catplot(df_cat, 
                       x = df_cat['variable'], 
                       y = df_cat['total'],
                       hue = df_cat['value'], 
                       kind = 'bar', 
                       col = 'cardio'
            )
    
    fig = g.fig



    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    cond_pressure = (df['ap_lo'] <= df['ap_hi'])
    cond_height = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    cond_weight = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    
    df_heat = df.loc[cond_pressure & cond_height & cond_weight]

    # 12
    corr = np.corrcoef(df_heat, rowvar = False)

    # 13
    mask = np.triu(corr, 0)



    # 14
    fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize=(11,9))
    (ax1, ax2) = ax
    ax1.axes.set_position([0.125, 0.115, 0.625, 0.765])
    ax2.axes.set_position([0.78, 0.3, 0.015, 0.4])



    # 15
    sns.heatmap(corr, 
            vmax = 0.3,
            center = 0,
            annot = True,
            fmt = '.1f',
            linewidth = 0.5,
            cmap = None,
            cbar = True,
            cbar_ax = ax2,
            xticklabels = df_heat.columns, 
            yticklabels = df_heat.columns,
            mask = mask,
            ax = ax1)




    # 16
    fig.savefig('heatmap.png')
    return fig
