# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\Jan\student mark prediction\Desktop.pkl")


df = pd.DataFrame()

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    global df
    
    input_features = [float(x) for x in request.form.values()]
    features_value = np.array(input_features)
    
    #validate input hours
    if input_features[0] <0 or input_features[0] >24:
        return render_template('index.html', prediction_text='Please enter valid hours between 1 to 24 if you live on the Earth')
        

    output = round(model.predict(features_value.reshape(1,-1))[0], 2)

    # input and predicted value store in df then save in csv file
    df= pd.concat([df,pd.DataFrame({'Study Hours':input_features,'Predicted Output':[output]})],ignore_index=True)
    print(df)   
    df.to_csv('smp_data_from_app.csv')

    return render_template('index.html', prediction_text='You will get [{}%] marks, when you do study [{}] hours per day '.format(output, int(features_value[0])))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000 ,debug=True)

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)
