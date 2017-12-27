# Predictive Analytics on Cross-Domain Datasets using Ensemblers

The main goal of dissertation was to evaluate the performances of traditional machine learning algorithms, ensembler models and artificial neural network models by creating solutions for predictive problems and developing applications belonging to datasets from different domains.  
The initial hypothesis was ensembler models with feature engineering will work better in comparison to artificial neural networks and to prove this hypothesis not one, but five datasets belonging to different domains were used so that the hypothesis can be verified in general.  
The application created were:  
• Personalized Medicine for Cancer Research – A multivariate classification problem solved using LightGBM with feature extraction using Natural Language Processing, Support Vector Machine, and Sequential Neural Network.  
• Instagram Like Prediction – A multivariate regression problem solved by comparing algorithms such as AdaBoost, Lasso regression and Convolution Neural Network.  
• Stock Prediction – Solved using three different approaches which included using the stock values from major world markets, using sentiment scores related to a company and implementing Markovian Chain Monte Carlo model.  
• Fake Profile Detection – A bivariate classification problem whose data was retrieved in the form of Facebook profiles and solved using Random Forest and Sequential Neural Network.  
• Intrusion Detection System – Using the infamous KDD 1999 Cup dataset, an approach was created for the multivariate classification problem which outperformed the winning entry of the competition and rectified the problem in the dataset.  

The environment.yml file contains the virtual env to run all the code apart from Fake profiles - Facebook.  
It's .yml file is different and is supplied within the folder.  
To create the environment run:  

#### conda env create -f environment.yml