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

data=pd.read_csv('example_MSD2.csv')

sns.lineplot(x='Lag time', y='All',  data=data, color='blue', linewidth=3.5)

sns.lineplot(x='Lag time', y='particle',  data=data, color='black', alpha=0.2)
