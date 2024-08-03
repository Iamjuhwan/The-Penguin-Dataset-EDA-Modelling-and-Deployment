# The Penguin Dataset: EDA, Modelling, and Deployment

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Model Details](#model-details)

## Introduction
This project focuses on exploratory data analysis (EDA), modelling, and deploying a machine learning model using the Penguin dataset. The goal is to predict the species of penguins based on their physical characteristics.

## Dataset
The dataset contains various features of penguins such as bill length, bill depth, flipper length, and body mass. It is used to classify penguins into three species: Adelie, Gentoo, and Chinstrap.

## Project Structure
The-Penguin-Dataset-EDA-Modelling-and-Deployment/
│
├── data/
│ └── penguins.csv # Original dataset
│
├── models/
│ └── logistic.pkl # Trained logistic regression model
│
├── notebooks/
│ └── Penguin.ipynb # Jupyter notebook for EDA and model training
│
├── scripts/
│ └── penguins.py # Python script for deployment
│
├── requirements.txt # Dependencies
└── README.md # This file

## Usage
EDA and Model Training
1) Open the Jupyter Notebook Penguin.ipynb in the notebooks/ directory.
2) Follow the instructions for exploratory data analysis and train the machine learning model.

## Model Details
The logistic regression model was trained using the following features:

Bill length
Bill depth
Flipper length
Body mass
The model was evaluated using accuracy, precision, recall, and F1-score metrics.

## Results
The model achieves amazing accuracy on the test dataset. Detailed results and evaluation metrics can be found in the Penguin.ipynb notebook.
