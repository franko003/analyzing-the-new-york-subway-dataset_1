import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'male':
            predictions[passenger_id] = 0
        else:
            predictions[passenger_id] = 1
        
    return predictions


import numpy
import pandas
import statsmodels.api as sm

def complex_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        else:
            if passenger['Pclass'] == 1 and passenger['Age'] < 18:
                predictions[passenger_id] = 1
            else:
                predictions[passenger_id] = 0

    return predictions

import numpy
import pandas
import statsmodels.api as sm

def custom_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' and passenger['Pclass'] < 3:
            predictions[passenger_id] = 1
        else:
            if passenger['Sex'] == 'female' and passenger['Age'] < 6:
                predictions[passenger_id] = 1
            else:
                if passenger['Sex'] == 'female' and passenger['SibSp'] > 1:
                    predictions[passenger_id] = 0
                else:
                    if passenger['Sex'] == 'female' and passenger['Embarked'] == 'Q':
                        predictions[passenger_id] = 1
                    else:
                        predictions[passenger_id] = 0

    return predictions
