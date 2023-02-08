import seaborn as sns
from matplotlib import pyplot as plt

sns.get_dataset_names()
print(sns.get_dataset_names())

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")

print(tips)

spread = sns.scatterplot(x="tip", y="total_bill", data=tips)
plt.show()