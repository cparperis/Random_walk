#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 07:55:15 2022

@author: Christopher
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("darkgrid", {"axes.facecolor": ".96"})

data=pd.read_csv('example_MSD.csv')

sns.lineplot(x='Lag time', y='All',  data=data, color='blue', linewidth=2)

sns.lineplot(x='Lag time', y='0',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='1',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='2',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='3',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='4',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='5',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='6',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='7',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='8',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='9',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='10',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='11',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='13',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='14',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='15',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='16',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='17',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='18',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='19',  data=data, color='black', alpha=0.2)
sns.lineplot(x='Lag time', y='20',  data=data, color='black', alpha=0.2)

plt.ylabel('MSD$_{(μm^2)}$', fontsize=16)
plt.xlabel(r'$\tau$'+'$_{(seconds)}$', fontsize=16)