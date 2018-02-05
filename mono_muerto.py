# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 18:59:20 2018

@author: Andres
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
specie = pd.read_csv('http://gdfa.ugr.es/docencia/ecoinformatica/mano_de_muerto.csv')
specie.describe()
print (specie)
specie['continent'].value_counts()
specie['depth'].plot(style='o')
specie.groupby('yearcollected')['id'].count().plot(style='x')
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df= df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')
plt.savefig('graf.png')
