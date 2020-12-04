import pandas as pd
from numpy import sqrt
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
companies = df.groupby('CARGO').sum()

companies['Unnamed: 0'] = df.groupby("CARGO")["CARGO"].count()

print(companies)

ax = companies.plot(kind='bar', subplots=True,
legend=False, title=['flights count', 'Total shipped', 'Total revenue'], layout=(1,3), figsize=(16,9))

plt.show()
