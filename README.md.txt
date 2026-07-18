# Iris Flower Classification System

## Project Description

The Iris Flower Classification System is a machine learning application that predicts the species of an Iris flower based on its physical measurements. The system uses a trained Random Forest Classifier and provides real-time predictions through a user-friendly Streamlit web interface.

## Problem Being Solved

Identifying flower species manually can be challenging and time-consuming, especially for individuals without botanical expertise. This project automates the classification process by using machine learning to accurately predict flower species from measurable flower characteristics.

## Technologies Used

* Python
* Scikit-Learn
* Joblib
* Streamlit
* NumPy

## How the AI System Works

1. The Iris dataset is loaded and prepared for training.
2. A Random Forest Classifier is trained using flower measurements as input features.
3. The trained model is serialized and saved using Joblib.
4. The Streamlit application loads the saved model.
5. Users enter:

   * Sepal Length
   * Sepal Width
   * Petal Length
   * Petal Width
6. The model processes the input values and predicts the flower species:

   * Setosa
   * Versicolor
   * Virginica

## Model Information

* Model Type: Random Forest Classifier
* Machine Learning Task: Classification
* Dataset: Iris Dataset

## Deployment

The application is deployed using Streamlit Community Cloud and can be accessed through a web browser.

## Live Application

https://iris-flower-classification-system-2gurjujqpitgtduyguyuhy.streamlit.app/

## GitHub Repository

https://github.com/Ojeyinka-Mary/iris-flower-classification-system

## API Endpoints

Not applicable. This project uses a Streamlit web interface for user interaction instead of an API.

## Instructions for Running Locally

### Clone the Repository

```bash
git clone https://github.com/Ojeyinka-Mary/iris-flower-classification-system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

### Using the Application

1. Open the application in your browser.
2. Enter the flower measurements.
3. Click the Predict button.
4. View the predicted Iris flower species.

## Project Outcome

The deployed AI application successfully accepts user input, processes the data using a trained machine learning model, and provides real-time flower species predictions through an interactive web interface.
