# Machine Learning Stock Predictor

In this project we analyzed tweets over multiple years that are related to the company Tesla to try and predict their result. For more detailed information, see the 
"MachineLearningStockPredictorPaper.pdf" file.

## Code Overview

get_price_data.ipynb
Gets the TSLA stock price and S&P 500 stock price from yahoo finance and gets TSLA’s beta value from Zacks. Saves this data to csv files.

gather_tweets_snscrape.py
Gather all the tweets starting from 2013 to 2022 related to Tesla and Elon Musk and saves them to files based on the day they were gathered.

sentiment_on_jsonl.py
Reads each tweet file and cleans up the text in order to perform sentiment analysis. Loads tweet into csv file.

data_agregation.ipynb
Combines tweets and stock data into daily sample values and saves this data to csv files. Also does model training and analysis.

feature_selection_and_NN.ipynb
Our implementation of feature selection on the various datasets and the neural networks with hyperparameter selection. 

bing_project_code.ipynb
Using the dataset created to graph data visualizations and do linear regression, logistic regression, SVM, Simple Neural Network, and confusion matrices. 
