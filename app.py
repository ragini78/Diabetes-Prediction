# Importing the liberaries
import pickle
import numpy as np
from flask import Flask , request , render_template

#Global Variable
app = Flask(__name__)
loadModel = pickle.load(open('diabetes.pkl','rb'))

#User defined functions
@app.route("/",methods = ['GET'])
def Home():
    return render_template('index.html')

@app.route('/prediction',methods = ['POST'])
def predict():
    name = request.form['name']
    age = int(request.form['age'])
    bmi = int(request.form['BMI'])
    glucose = int(request.form['Glucose'])

    prediction = loadModel.predict([[glucose,bmi,age]])

    if prediction == [0]:
        prediction = 'Not Diabetic'
    else :
        prediction = 'Diabetic'

    return render_template('index.html',diagnosis_output = prediction) 

# Main Function

if __name__ == "__main__":
    app.run(debug = True)