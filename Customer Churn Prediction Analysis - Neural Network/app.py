import pickle
from flask import Flask,jsonify,request
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__) #__name__ = nama file nya (app.py)

CHURN_CLASSES = [0,1]
LABEL = ['Not Churn','Churn']
columns = ['tenure',
 'MonthlyCharges',
 'TotalCharges',
 'OnlineSecurity',
 'Contract',
 'PaymentMethod']

with open("fe_preprocessing.pkl","rb") as f:
    fe_preprocessing = pickle.load(f)

model = load_model('neuralmodel_m1.h5')


@app.route("/")
def homepage():
    return "<h1> Backend Pemodelan Churn Pelanggan </h1>"

@app.route("/churn",methods=['GET','POST'])
def churn_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [
            data['tenure'],
            data['MonthlyCharges'],
            data['TotalCharges'],
            data['OnlineSecurity'],
            data['Contract'],
            data['PaymentMethod']
        ]
        new_data = pd.DataFrame([new_data],columns=columns)

        new_data_preprocessed = fe_preprocessing.transform(new_data)

        res = model.predict(new_data_preprocessed)
        res = np.where(res>=0.5, 1, 0)
        res = res.flatten()[0]
        response = {
            'code' : 200,
            'status' : 'OK',
            'result' : {
                'prediction' : str(res),
                'classes': LABEL[res]
            }
        }
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model churn"

# app.run(debug=True)