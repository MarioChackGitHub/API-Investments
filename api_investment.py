from unittest import result
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score
import flask
import pickle

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/train', methods=['GET'])
def train():
    df = pd.read_csv("data/Advertising.csv")
    X = df[["TV" , "radio", "newspaper"]].values
    y= df[["sales"]]
    model = LinearRegression()
    model.fit(X, y)
    filename = 'model_pickle.pkl'
    pickle.dump(model, open(filename,'wb'))
    return "Modelo entrenado"


@app.route('/predict', methods=['POST'])
def predict():
    d_values = flask.request.json
    dict_values = dict(d_values)
    print(d_values)
    values_ordered = [dict_values['TV'], dict_values['radio'], dict_values['newspaper']]
    preprocessed_values = np.array(values_ordered).reshape(1,-1)

    filename = 'model_pickle.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(preprocessed_values)[0][0]
    print(result)
    return flask.jsonify({'Prediction': round(result,2)})


app.run()