import seaborn as sns
from matplotlib import pyplot as plt

sns.get_dataset_names()
print(sns.get_dataset_names())

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")

print(tips)

# spread = sns.scatterplot(x="tip", y="total_bill", data=tips, hue="day", size="size", palette="YlGnBu")

# spread2 = sns.histplot(tips['tip'], kde=True, bins=15)

# spread3 = sns.distplot(tips['tip'], kde=True, bins=15)

spread4 = sns.barplot(x='sex', y='tip', data=tips, palette="YlGnBu")

plt.show()