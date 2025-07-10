# https://youtu.be/bluclMxiUkA
"""
Multiple Linear Regression uses several explanatory variables to predict the outcome of a response variable.
There are a lot of variables and multiple linear regression is designed to create a model 
based on all these variables. 

#Dataset link:
https://cdn.scribbr.com/wp-content/uploads//2020/02/heart.data_.zip?_ga=2.217642335.893016210.1598387608-409916526.1598387608

#Heart disease
The effect that the independent variables biking and smoking 
have on the dependent variable heart disease 

the percentage of people biking to work each day, the percentage of people smoking, 
and the percentage of people with heart disease in an imaginary sample of 500 towns.


"""

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('files_for_training_model/heart.data_/heart.data.csv')
print(df.head())

df = df.drop("Unnamed: 0", axis=1)

sns.lmplot(x='biking', y='heart.disease', data=df)  
sns.lmplot(x='smoking', y='heart.disease', data=df)  


x_df = df.drop('heart.disease', axis=1)
y_df = df['heart.disease']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

from sklearn import linear_model

model = linear_model.LinearRegression()

model.fit(X_train, y_train) 
print(model.score(X_train, y_train))  

prediction_test = model.predict(X_test)    
print(y_test, prediction_test)
print("Mean sq. errror between y_test and predicted =", np.mean(prediction_test-y_test)**2)

import pickle
pickle.dump(model, open('models/model.pkl','wb'))

model = pickle.load(open('models/model.pkl','rb'))
print(model.predict([[20.1, 56.3]]))
