# Continuous Flow Process in a Factory

## Project Description

This project aims to predict the output measurements of a continuous flow manufacturing process using machine learning. The manufacturing line is separated into two stages:

1. **Stage 1**: Involves three machines operating in parallel. The products processed by these machines are combined at a conveyor, and measurements are taken at 15 locations.
2. **Stage 2**: The combined output from Stage 1 is fed into two machines operating in series. Measurements are again taken at 15 locations after processing through the second stage.

## Objectives

- **Primary Goal**: Predict the measurements at 15 locations after the first stage using ambient conditions, machine parameters, and combination zone parameters.
- **Secondary Goal**: Predict the measurements at 15 locations after the second stage using ambient conditions, machine parameters from the second stage, and the outputs from the first stage.

## Models

Three models are developed to achieve the project objectives:
1. **Model A**: Predicts Stage 1 outputs.
2. **Model B**: Predicts Stage 2 outputs using ambient conditions and machine parameters from the second stage.
3. **Model C**: Predicts Stage 2 outputs using ambient conditions, outputs from Stage 1, and machine parameters from the second stage.

## Implementation

<!-- - **Data Preprocessing**: Involves handling missing values, removing setpoints and columns with high zero values, and feature selection using backward elimination.
- **Machine Learning Algorithms**: Utilizes Decision Trees, Polynomial Support Vector Machines (SVM), and K-Nearest Neighbors (KNN) for predictions.
- **Evaluation**: Prediction accuracy is measured for each model and algorithm, focusing on minimizing mean squared error (MSE). -->

## MLOps Integration

<!-- The project integrates continuous integration and continuous deployment (CI/CD) practices using GitHub Actions and Azure, ensuring efficient model deployment and monitoring. -->