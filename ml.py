##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    mauna_loa_df = pd.read_csv('mauna_loa.csv')
    return mauna_loa_df
   

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    
    
