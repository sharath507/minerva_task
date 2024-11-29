# import required libraries
from fastapi import FastAPI
import joblib
import numpy as np
import json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
# load the model
model = joblib.load('D:\minerva_task\my_model.joblib')



app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'student_performance_prediction'}

@app.post('/predict')
def predict(data: dict):
    """
    give the 3 dimnsional data in json format

    s=subject
    {
               "student": [
                    {
                        "Year 1": {"s1": 85, "s2": 92,"s3": 85, "s4": 92,"s5": 85, "s6": 92}
                    },
                    {
                        "Year 2": {"s1": 85, "s2": 92,"s3": 85, "s4": 92,"s5": 85, "s6": 92}
                    },
                    {
                        "Year 3": {"s1": 85, "s2": 92,"s3": 85, "s4": 92,"s5": 85, "s6": 92}
                    }
                    {
                        "Year 4": {"s1": 85, "s2": 92,"s3": 85, "s4": 92,"s5": 85, "s6": 92}
                    },
                    {
                        "Year 5": {"s1": 85, "s2": 92,"s3": 85, "s4": 92,"s5": 85, "s6": 92}
                    },
                    {
                        "Year 6": {"s1": 85, "s2": 92,"s3": 85, "s4": 92,"s5": 85, "s6": 92}
                    }
                ]
    }
    """        
#function to convert the json data to array to load the data to model
    def json_to_array(json_file):

        
        # data = json.loads(json_file)("use this line to convert the json to python dictinory")

        data = json_file

        # Extract the "student" data
        student_data = data["student"]

        # Initialize an empty list to store the 3D data
        array_3d = []

        # Iterate through each year and collect subject values
        for year in student_data:
            for key, subjects in year.items():
                array_3d.append(list(subjects.values()))  # Append subject scores as a list

        # Convert to NumPy array
        array_3d = np.array(array_3d)

        # Reshape to 3D ( 1 student, 6 years , 6 subject)
        array_3d = array_3d.reshape(1,6, 6)

        return array_3d

    features = json_to_array(data)
    prediction = model.predict(features)
    p=prediction
    
    return {f" future_score: {{'s1': {int(p[0][0])}, 's2': {int(p[0][1])}, 's3': {int(p[0][2])}, 's4': {int(p[0][3])}, 's5': {int(p[0][4])}, 's6': {int(p[0][5])}}}"}
