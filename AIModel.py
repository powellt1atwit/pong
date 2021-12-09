import pandas as pd
import numpy as np 

data = pd.read_csv("pong_data_train.csv")
data = data.dropna()
print(data)

#Split train and test data
x = data.iloc[:, 0:4]
y = data.iloc[:, 5]
print(x)
print(y)

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(xtrain, ytrain)
y_model = model.predict(xtest)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, x, y, cv=5)
print(np.mean(np.abs(scores)))

from joblib import dump
dump(model, 'mymodel.joblib') #save