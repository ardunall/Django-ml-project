
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd


def make_prediction():

    # Load dataset
    df = pd.read_csv("data_model/diabetes_data.csv")

    X = df[["age", "sex", "bmi", "bp", "tc",
            "ldl", "hdl", "tch", "ltg", "glucose"]]
    Y = df['Result']

    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1)

    model = linear_model.LinearRegression()
    
    model.fit(x_train, y_train)

    test = model.predict(x_test)  

    print(r2_score(y_test, test))

  
  #  Pickle model
    pd.to_pickle(model, "data_model/mo3del.pickle")

    # Unpickle model
    model = pd.read_pickle("data_model/mo3del.pickle")