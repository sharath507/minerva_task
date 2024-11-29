Student Performance Prediction
Project Explanation
This project focuses on predicting student performance using a neural network model based on LSTM (Long Short-Term Memory). The model is designed to analyze historical academic performance across multiple subjects and years and predict future scores. The model processes 3-dimensional data representing students, academic years, and subjects and outputs 2-dimensional data indicating predicted scores for each subject.

Key Features:
Input Data: 3-dimensional JSON format (students × years × subjects).
Output Data: Predicted future scores for each subject.
Dataset: Randomly generated 3-dimensional data used for training.
Model Format: The trained model is saved in .joblib format for efficient reuse.
Libraries Used: The model is implemented using TensorFlow and other supporting Python libraries.
Model Selection
The LSTM neural network was chosen for this project due to its ability to effectively handle sequential data and maintain temporal relationships. The architecture includes:

Input Layer: Processes the 3-dimensional input data.
LSTM Layer: Captures temporal patterns in the dataset.
Dense Layer: Outputs the future scores.
The model is trained on a dataset generated using random number generators, simulating the student's academic performance. The data preparation, training, and evaluation were performed using TensorFlow's high-level APIs.

Steps to Run the Application
1. Clone the Repository
Clone the project repository to your local machine:


2. Build and Run the Docker Container
Ensure you have Docker installed. Build and run the container using the following commands:

docker build -t student-performance-app .
docker run -p 8000:8000 student-performance-app

3. Access the API
Open your browser and navigate to:

http://localhost:8000/docs
This will open the Swagger UI, where you can test the API.

4. Use the /predict Endpoint
In the /docs interface:

Locate the POST /predict endpoint.
Insert the JSON data in the following format:

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
                },
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
Click "Execute" to send the POST request.
The API will respond with the predicted future scores in JSON format.
Example Output:

{
    "future_score": {
        "s1": 88,
        "s2": 90,
        "s3": 87,
        "s4": 89,
        "s5": 85,
        "s6": 91
    }
}
