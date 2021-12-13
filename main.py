from re import search

from sklearn import linear_model
import model 

data = model.load_data('car details v3.csv')
data = model.__duplicates__(data)
data = model.__handlemissingValues__(data)
data = model.__cleanData__(data)
final_model = model.modelTraining(data)


if __name__ == '__main__':
    final_model