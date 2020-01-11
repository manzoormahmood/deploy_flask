
# coding: utf-8

# # House Prices using Backward Elimination
# 
# Just started with machine learning. I have used backward Elimination to check the usefulness of dependent variables.

# In[1]:


#importing all the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

get_ipython().run_line_magic('matplotlib', 'inline')


dataset = pd.read_csv('kc_house_data.csv')
dataset.head()


# In[2]:


#checking if any value is missing
print(dataset.isnull().any())


# In[3]:


#checking for categorical data
dataset = dataset.drop(['id','date','sqft_lot','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15'], axis = 1)
print(dataset.dtypes)
dataset.head()


# In[4]:


#separating independent and dependent variable
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values#price
#splitting dataset into training and testing dataset
#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# In[5]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model_house.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model_house.pkl','rb'))
print(model.predict([[ 4, 4,2000,2]]))

# Predicting the Test set results
#y_pred = regressor.predict(X_test)

