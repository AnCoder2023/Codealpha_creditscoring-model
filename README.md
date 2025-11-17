Credit Scoring Model – Internship Project

This project builds a Decision Tree–based Credit Scoring Model to classify whether a customer has Good Credit or Bad Credit.
The project includes data preprocessing, model training, evaluation, visualization, and model export.

Project Structure:
credit-scoring-model/
│
├── data/                # dataset folder (empty for now)
├── models/              # saved trained models
│     └── credit_model.pkl
├── notebooks/
│     └── credit_model.ipynb   # your Jupyter notebook
├── report.txt           # model accuracy + confusion matrix
├── requirements.txt     # python dependencies
└── README.md            # project documentation

Project Workflow:

Loaded a sample dataset generated inside the notebook
Preprocessed and cleaned the data
Trained a Decision Tree Classifier

Evaluated using:

Accuracy Score
Confusion Matrix
Visualized the decision tree
Exported model as credit_model.pkl
Generated a text-based project report

Model Used:

Decision Tree Classifier (Gini Index)
Implemented using scikit-learn

 Evaluation Metrics:

Accuracy Score
Confusion Matrix
Tree Visualization
All outputs are visible inside the Jupyter Notebook and saved in report.txt.

Saved Model:

The trained model is exported to:
models/credit_model.pkl
This file can be loaded later for deployment.

Tools & Libraries:

Python 3
Jupyter Notebook
pandas
numpy
scikit-learn
matplotlib
seaborn

All dependencies are listed in requirements.txt.

 Developed By:

Ananya Gaur
Credit Scoring Model – Internship Submission




TASK 2 — Iris Flower Classification

Colab Notebook:
https://colab.research.google.com/drive/1xYbzBYV5yvijkO18b2V0yJLzs9fl8YiX?authuser=0#scrollTo=wUdpvtpY60JU

Model File:

models/iris_model.pkl

Notebook File:

notebooks/task2_iris_classification.ipynb

Description:
This task focuses on building a machine learning classification model using the classic Iris dataset.
Steps completed:

Loaded Iris dataset using Scikit-learn

Performed train–test split (80% train / 20% test)

Trained Random Forest Classifier

Evaluated model using accuracy and classification report

Saved the trained model as iris_model.pkl

Result:
Successfully achieved high accuracy on test data.
