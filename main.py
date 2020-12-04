import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv', sep=',')
NimblePrice = 0
NimbleWeigth = 0
NimbleCount = len(df[df.CARGO == 'Nimble'][['PRICE']])
for i in df[df.CARGO == 'Nimble'][['PRICE']].index:
    NimblePrice = NimblePrice + int(df.loc[[i], 'PRICE'])
    NimbleWeigth = NimbleWeigth + int(df.loc[[i], 'WEIGHT'])
JumboPrice = 0
JumboWeigth = 0
JumboCount = len(df[df.CARGO == 'Jumbo'][['PRICE']])
for i in df[df.CARGO == 'Jumbo'][['PRICE']].index:
    JumboPrice = JumboPrice + int(df.loc[[i], 'PRICE'])
    JumboWeigth = JumboWeigth + int(df.loc[[i], 'WEIGHT'])
MediumPrice = 0
MediumWeigth = 0
MediumCount = len(df[df.CARGO == 'Medium'][['PRICE']])
for i in df[df.CARGO == 'Medium'][['PRICE']].index:
    MediumPrice = MediumPrice + int(df.loc[[i], 'PRICE'])
    MediumWeigth = MediumWeigth + int(df.loc[[i], 'WEIGHT'])
index = ['Nimble','Jumbo', 'Medium']
valuesCount = [NimbleCount,JumboCount,MediumCount]
valuesWeight = [NimbleWeigth,JumboWeigth,MediumWeigth]
valuesPrice = [NimblePrice,JumboPrice,MediumPrice]
plt.title('Total Count')
plt.bar(index,valuesCount)
plt.show()
plt.title('Total Weigth')
plt.bar(index,valuesWeight)
plt.show()
plt.title('Total Price')
plt.bar(index,valuesPrice)
plt.show()

