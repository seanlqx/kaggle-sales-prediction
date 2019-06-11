# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:22:34 2019

@author: sean_lqx
"""

import os 
print(os.listdir("./data"))

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from matplotlib import pylab as plt
import matplotlib.dates as mdates
plt.rcParams['figure.figsize'] = (15.0, 8.0)
import seaborn as sns

# for kaggle competition, always look at sample_submission.csv first, so you know what you want to get
# then train.csv and test.csv
sub = pd.read_csv('./data/sample_submission.csv.gz')
sub.head()

train = pd.read_csv('./data/sales_train.csv.gz')
print ('number of shops: ', train['shop_id'].max())
print ('number of items: ', train['item_id'].max())
num_month = train['date_block_num'].max()
print ('number of month: ', num_month)
print ('size of train: ', train.shape)
train.head()

test = pd.read_csv('./data/test.csv.gz')
test.head()

items = pd.read_csv('./data/items.csv')
print ('number of categories: ', items['item_category_id'].max()) # the maximun number of category id
items.head()
























