#author PGKSUNILKUMAR
import os
import numpy as np
import pandas as pd
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, metrics
data = pd.read_csv('1.csv',names=['A1', 'A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21'])
data.head()
 
data.info()
data['class'],class_names = pd.factorize(data['class'])
print(class_names)
print(data['class'].unique())

# Index([u'unacc', u'acc', u'vgood', u'good'], dtype='object')
# data['buying'],_ = pd.factorize(data['buying'])
# data['maint'],_ = pd.factorize(data['maint'])
# data['doors'],_ = pd.factorize(data['doors'])
# data['persons'],_ = pd.factorize(data['persons'])
# data['lug_boot'],_ = pd.factorize(data['lug_boot'])
# data['safety'],_ = pd.factorize(data['safety'])
# data.head()
 
 
 
 