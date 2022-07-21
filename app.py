# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:52:45 2022

@author: Aniket
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('lungcap_bmi_alg.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_Lungcap.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        BMI = float(request.form['BMI'])
        Age=float(request.form['Age'])
        Height=float(request.form['Height'])
        Smoke=request.form['Smoke']
        if(Smoke=='yes'):
            Smoke=1
        else:
            Smoke=0
        Gender=request.form['Gender']
        if(Gender=='male'):
            Gender=1
        else:
            Gender=0	
        Caesarean=request.form['Caesarean']
        if(Caesarean=='yes'):
            Caesarean=1
        else:
            Caesarean=0
            
        prediction=model.predict([[Age,Height,Smoke,Gender,Caesarean,BMI]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index_Lungcap.html',prediction_texts="zero")
        else:
            return render_template('index_Lungcap.html',prediction_text="Lungcap is {}".format(output))
    else:
        return render_template('index_Lungcap.html')

if __name__=="__main__":
    app.run(debug=True)
