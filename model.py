from os import X_OK
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

def load_data(file_name):
    data = pd.read_csv(file_name)
    return data


def __duplicates__(data):
    # data = data.drop_duplicates(subset='id', keep='first')
    if data.duplicated().any():
        data = data.drop_duplicates()
    
    return data

def __info__(data):
    print(data.info())
    print('---------------------------------------------------------------------------------------------------------')
    print(data.describe())
    print('---------------------------------------------------------------------------------------------------------')
    print(data.head())
    print('---------------------------------------------------------------------------------------------------------')
    print(data.tail())
    print('---------------------------------------------------------------------------------------------------------')
    print(data.shape)
    print('---------------------------------------------------------------------------------------------------------')
    print(data.dtypes)
    print('---------------------------------------------------------------------------------------------------------')
    print(data.isnull().sum())
    print('---------------------------------------------------------------------------------------------------------')
    print(data.isnull().sum()/data.shape[0]*100)
    print('---------------------------------------------------------------------------------------------------------')
    print(data['owner'].value_counts())
    print('---------------------------------------------------------------------------------------------------------')
    print(data['fuel'].value_counts())
    

def __handlemissingValues__(data):
    data = data.dropna()
    return data


# Cleaning data

def __cleanData__(data):
    data = data.drop(['torque'], axis=1)
    data = data.drop(['name'], axis=1)
    data['age'] = 2021 - data['year']
    data = data.drop(['year'], axis=1)
    data['owner'] = data['owner'].replace({'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4, 'Test Drive Car': 5})
    data['mileage'] = data['mileage'].str.strip(' kmpl').str.strip(' km/kg')
    data['engine'] = data['engine'].str.strip(' CC')
    data['max_power'] = data['max_power'].str.strip(' bhp')
    data['transmission'] = data['transmission'].replace({'Manual': 1, 'Automatic': 2})
    data['fuel'] = data['fuel'].replace({'Petrol': 1, 'Diesel': 2, 'CNG': 3, 'LPG': 4})
    data['seller_type'] = data['seller_type'].replace({'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3})
    data['mileage'] = pd.to_numeric(data['mileage'])
    data['engine'] = pd.to_numeric(data['engine'])
    data['max_power'] = pd.to_numeric(data['max_power'])
    data['owner'] = pd.to_numeric(data['owner'])
    return data


def __plottest__(data):
    #data.hist(bins=50, figsize=(20, 15))
    data.plot(x='selling_price', y='age', kind='scatter')
    data.plot(x='selling_price', y='mileage', kind='scatter')
    data.plot(x='selling_price', y='engine', kind='scatter')
    data.plot(x='selling_price', y='max_power', kind='scatter')
    data.plot(x='selling_price', y='transmission', kind='scatter')
    data.plot(x='selling_price', y='owner', kind='scatter')
    data.plot(x='selling_price', y='fuel', kind='scatter')
    plt.show()

# Splotting data

def __splittingData__(data):

    train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
    return (train_set, test_set)

def datadropping(data): #Training data
    data = __splittingData__(data)[0].drop(['selling_price'], axis=1)
    return data

def datalabbelling(data):
    data_label = __splittingData__(data)[0]['selling_price'].copy()
    return data_label


#Start trainig model

def linearTraining(data):
    regressor = LinearRegression()
    regressor.fit(datadropping(data), datalabbelling(data))
    some_data = datadropping(data).iloc[:10]
    some_labels = datalabbelling(data).iloc[:10]
    print('Predictions:', regressor.predict(some_data))
    print('Labels:', list(some_labels))
    price_prediction = regressor.predict(datadropping(data))
    lmse = mean_squared_error(datalabbelling(data), price_prediction)
    rmse = np.sqrt(lmse)
    print('RMSE:', rmse)
    scores = cross_val_score(regressor, datadropping(data), datalabbelling(data), cv=10, scoring='neg_mean_squared_error')
    rmse_scores = np.sqrt(-scores)
    print('RMSE scores:', rmse_scores)
    print('Mean RMSE:', rmse_scores.mean())
    print('Standard deviation:', rmse_scores.std())

def treeTraining(data):
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(datadropping(data), datalabbelling(data))
    some_data = datadropping(data).iloc[:10]
    some_labels = datalabbelling(data).iloc[:10]
    print('Predictions:', regressor.predict(some_data))
    print('Labels:', list(some_labels))
    price_prediction = regressor.predict(datadropping(data))
    lmse = mean_squared_error(datalabbelling(data), price_prediction)
    rmse = np.sqrt(lmse)
    print('RMSE:', rmse)
    scores = cross_val_score(regressor, datadropping(data), datalabbelling(data), cv=10)
    tree_rmse_scores = np.sqrt(scores)
    print('RMSE scores:', tree_rmse_scores)
    print('Mean RMSE score:', tree_rmse_scores.mean())
    print('Standard deviation:', tree_rmse_scores.std())


def randomForestTraining(data):
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(datadropping(data), datalabbelling(data))
    some_data = datadropping(data).iloc[:10]
    some_labels = datalabbelling(data).iloc[:10]
    print('Predictions:', regressor.predict(some_data))
    print('Labels:', list(some_labels))
    price_prediction = regressor.predict(datadropping(data))
    lmse = mean_squared_error(datalabbelling(data), price_prediction)
    rmse = np.sqrt(lmse)
    print('RMSE:', rmse)
    scores = cross_val_score(regressor, datadropping(data), datalabbelling(data), cv=10)
    rf_rmse_scores = np.sqrt(scores)
    print('RMSE scores:', rf_rmse_scores)
    print('Mean RMSE score:', rf_rmse_scores.mean())
    print('Standard deviation:', rf_rmse_scores.std())



def modelTraining(data):
    reg = LinearRegression()
    tree = DecisionTreeRegressor()
    forest = RandomForestRegressor()
    reg.fit(datadropping(data), datalabbelling(data))
    price_prediction = reg.predict(datadropping(data))
    lmse = mean_squared_error(datalabbelling(data), price_prediction)
    rmse = np.sqrt(lmse)
    print('RMSE Linear Training:', rmse)
    print('---------------------------------------------------------------------------------------------------------')
    tree.fit(datadropping(data), datalabbelling(data))
    price_prediction2 = tree.predict(datadropping(data))
    lmse2 = mean_squared_error(datalabbelling(data), price_prediction2)
    rmse2 = np.sqrt(lmse2)
    print('RMSE Tree Training:', rmse2)
    print('---------------------------------------------------------------------------------------------------------')
    forest.fit(datadropping(data), datalabbelling(data))
    price_prediction3 = forest.predict(datadropping(data))
    lmse3 = mean_squared_error(datalabbelling(data), price_prediction3)
    rmse3 = np.sqrt(lmse3)
    print('RMSE Forest Training:', rmse3)
    print('---------------------------------------------------------------------------------------------------------')


def searchGrid(data):
    param_grid = [
        {'n_estimators': [10, 20, 30, 40, 50],'max_features': [2, 3, 4, 5, 6],
        'bootstrap': [False], 'n_estimators': [10, 20, 30, 40, 50, 60, 70, 80, 90], 'max_features': [2, 3, 4, 5, 6, 7, 8, 9, 10]},
    ]
    forest = RandomForestRegressor()
    grid_search = GridSearchCV(forest, param_grid, cv=10, scoring='neg_mean_squared_error', return_train_score=True)
    grid_search.fit(datadropping(data), datalabbelling(data))
    print(grid_search.best_params_)


def final_model(data):
    forest = RandomForestRegressor(n_estimators=100, max_features=5, bootstrap=False)
    test_set = __splittingData__(data)[1]
    X_test = test_set.drop(['selling_price'], axis=1)
    y_test = test_set['selling_price'].copy()
    forest.fit(X_test, y_test)
    some_data = X_test.iloc[:10]
    some_labels = y_test.iloc[:10]
    print('Predictions:', forest.predict(some_data))
    print('Labels:', list(some_labels))
    price_prediction = forest.predict(X_test)
    lmse = mean_squared_error(y_test, price_prediction)
    rmse = np.sqrt(lmse)
    print('RMSE:', rmse)

        