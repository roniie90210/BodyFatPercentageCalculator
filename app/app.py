from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
    if request.method=='GET':
        return render_template('index.html')
    else:
        print('yes')
        
        model = pickle.load(open("../models/model.pkl", 'rb'))
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        neck = float(request.form['neck'])
        chest = float(request.form['chest'])
        abdomen = float(request.form['abdomen'])
        hip = float(request.form['hip'])
        thigh = float(request.form['thigh'])
        knee = float(request.form['knee'])
        ankle = float(request.form['ankle'])
        biceps = float(request.form['biceps'])
        forearm = float(request.form['forearm'])
        wrist = float(request.form['wrist'])
        density = float(request.form['density'])

        data=np.array([[density,age,weight,height,neck,chest,abdomen,hip,thigh,knee,ankle,biceps,forearm,wrist]])
        my_prediction = model.predict(data)
        #final_prediction = my_prediction[0]

        return render_template('index.html', prediction=my_prediction)

if __name__=='__main__':
    app.run(debug=True)