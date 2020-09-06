""" This Program creates a regression model to predict the housing prices in Boston """

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model

data = pd.read_csv("boston_house_data.txt", sep=",")
print(data.head())

data = data[["CRIM", "ZN", "INDUS","CHAS", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]]

print(data.head())
predict = 'TAX'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)

"""print model accuracy"""

print(acc)

""" output regession model """

print("Co: \n", linear.coef_)
print("Intercept \n", linear.intercept_)


""" print prediction and actual value in $10,000s"""

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], y_test[x])
