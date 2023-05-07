# MA3615-Credited-Research-Project-I
It is a credited group project about analysing banks financial health. By Prajwaldeep Kamble, Mulugu Vishwanath and Lokesh Surana under Dr. Sammen Naqvi IIT-Hyderabad.

In this Project we tried to analysis Indian Banks Financial performace. With respect to the India's Stock index Nifty-50. using various Statistical and Machine Learning techniques. 

## Data Collection (scrape1.py and scrape2.py)
These two files are used for data collection. We have used money control website for the data collection. 

## Data Cleaning (data_clean.py)
1. We have removed the columns which are not required for our analysis.
2. We have removed the rows whth NaN values.
3. We normailzed some features as mentioned in the report.
4. collected the data data about Nifty-50 index and merged it with the bank data, using the yfinance library.
5. merged all the data into one csv file [file name: final_data (1).csv ].

## Data Analysis (main.py and main_pca.py)
1. We have used the main.py file for the analysis of the data without the orignal features.
2. We have used the main_pca.py file for the analysis of the data with only the 11-principle componants. we chose 11-principle componants because it explains 95% of the variance in the data.
### In both main.py and main_pca.py we have used the following techniques for the analysis.
1. Discriminant Analysis: Linear Discriminant Analysis (LDA) and Quadratic Discriminant Analysis (QDA)
2. Logistic Regression
3. Support Vector Machine (SVM)
4. Random Forest
5. Decision Tree
6. XGBoost
7. AdaBoost
8. CatBoost
9. Regularized XGBoost 

