from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

iris_conj = load_iris(as_frame=True)

X_train, X_test, y_train, y_test = train_test_split(
    iris_conj["data"],
    iris_conj["target"],
    random_state=0
)

dcorr = pd.plotting.scatter_matrix(
    X_train,
    c=y_train,
    figsize=(15, 15),
    hist_kwds={'bins': 20},
    s=60,
    alpha=0.8
)