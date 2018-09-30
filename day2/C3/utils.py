
from sklearn import datasets
import pandas as pd
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np


def get_boston_data(): 
    raw = datasets.load_boston()
    df = pd.DataFrame(raw['data'],columns=raw['feature_names'])
    df['target'] = raw['target']
    
    return df



def get_linreg_interactive(input_data):
    df = input_data.copy()
    m = widgets.FloatSlider(description='m',min=0,max=5,step=0.25)
    c = widgets.FloatSlider(description='c',min=-2,max=2,step=0.25)
    e = widgets.FloatText(description='error')

    def f(m , c ):
        fig = plt.figure(figsize=(10,6))
        x = np.linspace(-10, 10, num=100)
        err = np.sum((df['y']-(m*df['X']+c))**2)
        e.value = err 
        plt.plot(x, m * x + c)
        plt.scatter(df['X'],df['y'],c='r')
        plt.ylim(0, 4)
        plt.xlim(0,1)
        plt.show()

    out = widgets.VBox([widgets.VBox([m, c,e]), widgets.interactive_output(f, {'m': m, 'c': c})])

    return out

