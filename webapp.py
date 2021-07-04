# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:29:25 2021

@author: aspdiscovery
"""

from flask import Flask,request
import joblib

encoder=joblib.load(r"Bank-encoder.pkl")
model=joblib.load(r"Bank-model.pkl")

app=Flask(__name__)

@app.route('/',methods=['POST'])

def abc():
    data=request.get_json(force=True)
    print(data)
    data=data['key']
    data=encoder.transform(data)
    print(data)
    output=model.predict(data)
    return str(output)

