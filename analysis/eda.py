import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/hr_data.csv")

print(df.corr())

sns.heatmap(df.corr(), annot=True)
plt.show()
