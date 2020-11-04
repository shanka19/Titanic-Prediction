import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Pclass':1.0, 'Age':50.0, 'Members':4, 'Fare':50, 
                            'Female':1.0, 'Male': 0.0,'C':1.0,'Q':0.0, 'S':0.0})

print(r.json())