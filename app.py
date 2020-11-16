import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
with open('model.pkl','rb') as f:
    model = pickle.load(f)
with open('scaler.pkl','rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = scaler_transform(np.array(int_features).reshape(1,-1))
    prediction = model.predict(final_features)
    output = prediction[0]
    
    return render_template('index.html',prediction_text='Survived or Not Survived {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)