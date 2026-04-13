import seaborn as sns
import matplotlib.pyplot as plt

iris_nuevo = sns.load_dataset("iris")

# Pairplot
sns.pairplot(iris_nuevo, hue="species")

# Petalos
sns.lmplot(
    x="petal_width",
    y="petal_length",
    data=iris_nuevo,
    fit_reg=False,
    hue="species"
)

plt.title("Diagrama pétalos")

# Sépalos
sns.lmplot(
    x="sepal_width",
    y="sepal_length",
    data=iris_nuevo,
    fit_reg=False,
    hue="species"
)

plt.title("Diagrama sépalos")

plt.show()