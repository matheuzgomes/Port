import seaborn as sns
import matplotlib.pyplot as plt
import random
i = 0
height = [5, 5, 3, 3, 15, 4, 3, 9, 35, 20, 34, 48, 48, 39, 14, 46, 39, 39, 43, 41, 35, 49, 27, 35, 5]
weight = [42, 11, 29, 12, 39, 34, 8, 41, 19, 28, 47, 23, 19, 32, 46, 13, 45, 4, 49, 8, 3, 46, 26, 44, 26]

sns.barplot(x=height, y=weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()


