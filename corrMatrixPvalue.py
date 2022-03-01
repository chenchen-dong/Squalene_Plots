import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def corr_sig(df=None):
    p_matrix = np.zeros(shape=(df.shape[1],df.shape[1]))
    for col in df.columns:
        for col2 in df.drop(col,axis=1).columns:
            _ , p = stats.pearsonr(df[col],df[col2])
            p_matrix[df.columns.to_list().index(col),df.columns.to_list().index(col2)] = p
    return p_matrix

df = pd.read_csv('/Users/dongchen/Downloads/plant_corr.csv')

p_values = corr_sig(df)
#np.savetxt("/Users/dongchen/Documents/Chen_work/SaltStress_pValue.csv",p_values,delimiter=",")
df_mask = np.invert(np.tril(p_values<0.05))
f, ax = plt.subplots(figsize=(11, 15))

#triuMax = np.triu(df.corr())
#corrMax = sns.heatmap(df.corr(),annot = True, vmin=-1, vmax=1, center= 0, fmt = '.2g', cmap= 'coolwarm', mask = df_mask)
corrMax = sns.heatmap(df.corr(),
                      mask = df_mask,
                      square = True,
                      linewidths = .5,
                      cmap = 'coolwarm',
                      cbar_kws = {'shrink': .4,
                                'ticks' : [-1, -.5, 0, 0.5, 1]},
                      vmin = -1,
                      vmax = 1,
                      annot = True,
                      annot_kws = {'size': 12})
corrMax.get_figure().savefig('plant_corr.png', bbox_inches='tight')

