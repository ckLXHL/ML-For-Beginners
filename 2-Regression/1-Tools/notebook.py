from sklearn import linear_model, model_selection, datasets
import numpy as np
import matplotlib.pyplot as plt

X, y = datasets.load_diabetes(return_X_y=True)
print(X.shape)
print(X[0])
plt.plot()