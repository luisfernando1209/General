import pickle
from flask import Flask,jsonify,request
import pandas as pd

app = Flask(__name__) #__name__ = nama file nya (app.py)

CHURN_CLASSES = [0,1]
LABEL = ['Not Churn','Churn']
columns = ['Account length',
 'International plan',
 'Total day minutes',
 'Total day calls',
 'Total eve minutes',
 'Total night minutes',
 'Total night calls',
 'Total intl minutes',
 'Total intl calls',
 'Customer service calls']

with open("model_gridpipeline.pkl","rb") as f:
    model_pipeline = pickle.load(f)

@app.route("/")
def homepage():
    return "<h1> Backend Pemodelan Churn Pelanggan </h1>"

@app.route("/churn",methods=['GET','POST'])
def churn_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [
            data['Account length'],
            data['International plan'],
            data['Total day minutes'],
            data['Total day calls'],
            data['Total eve minutes'],
            data['Total night minutes'],
            data['Total night calls'],
            data['Total intl minutes'],
            data['Total intl calls'],
            data['Customer service calls'],
        ]
        new_data = pd.DataFrame([new_data],columns=columns)
        res = model_pipeline.predict(new_data)
        response = {
            'code' : 200,
            'status' : 'OK',
            'result' : {
                'prediction' : str(res[0]),
                'classes': LABEL[res[0]]
            }
        }
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model churn"

    
# app.run(debug=True)
