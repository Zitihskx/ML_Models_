# -*- coding: utf-8 -*-
"""Non linear reg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xX1PCdN3VQS47o4A7pe9vtPZqOsJvKog
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

!wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv

df = pd.read_csv('FuelConsumption.csv')
df.head()

ned = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
ned.head()

plt.scatter(ned.ENGINESIZE, ned.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

msk = np.random.rand(len(df)) < 0.8
train = ned[msk]
test = ned[~msk]

train.describe()
test.describe()

from sklearn.preprocessing import PolynomialFeatures
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)

train_x_poly

from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit(train_x_poly,train_y)

print('Coefficients: ', clf.coef_)
print('Intercepts: ',clf.intercept_)

plt.scatter(train.ENGINESIZE,train.CO2EMISSIONS,color='green')
xx = np.arange(0,10.0,0.1)
yy = clf.intercept_ + clf.coef_[0][1]*xx + clf.coef_[0][2]*np.power(xx,2)
plt.plot(xx,yy,'-r')
plt.xlabel('ENginesize')
plt.ylabel('Co2emission')



from sklearn.metrics import r2_score

test_x_poly = poly.fit_transform(test_x)
test_y_poly = clf.predict(test_x_poly)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_poly - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_poly - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_poly , test_y) )

poly1 = PolynomialFeatures(degree=3)
train_xxx_poly = poly1.fit_transform(train_x)
clf.fit(train_xxx_poly,train_y)


print("Coefficient: ", clf.coef_)
print("intercept: ", clf.intercept_)

plt.scatter(train.ENGINESIZE,train.CO2EMISSIONS,color='green')
xx = np.arange(0,10.0,0.1)
yy = clf.intercept_ + clf.coef_[0][1]*xx + clf.coef_[0][2]*np.power(xx,2)+clf.coef_[0][3]*np.power(xx,3)
plt.plot(xx,yy,'-r')
plt.xlabel('ENginesize')
plt.ylabel('Co2emission')

from sklearn.metrics import r2_score

test_x_poly = poly1.fit_transform(test_x)
test_y_poly = clf.predict(test_x_poly)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_poly - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_poly - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_poly , test_y) )