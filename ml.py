##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    df = pd.read_csv('mauna_loa.csv')
    return df
   

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    years = df['decimal_date'][0] - df['decimal_date']
    plt.ylabel('CO2 Levels')
    plt.xlabel('Years since 1958')
    plt.title('Rising CO2 Levels since 1958 Mauna Loa Observatory')
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    return plt.plot(years,df.C02)
    