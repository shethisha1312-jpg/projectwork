Global Happiness report analysis (2015)

Project Overview
This project analyzes the World Happiness Report 2015 dataset to explore happiness scores across countries and understand how selected factors relate to happiness.
The program summarizes the data, identifies the 10 happiest countries, compares GDP per capita with happiness scores, and visualizes correlations between happiness and other factors.

Dataset
=>Filename : 2015.csv
=>World Happiness Report dataset available on Kaggle

Tools and Libraries
=>Python 
=>Pandas
=>Numpy
=>Matplotlib
=>Seaborn

Project Features
1) Load and Preview Data
   Load 2015.csv with pandas and display the first few rows.
2) Explore Dataset
   Display the dataset shape and checks missing-value counts in each column.
3) Happiness Score countries
   Uses NumPy to calculate the mean, maximum, median, and standard deviation of happiness scores
4) Top 10 happiness countries
   sorts countries by Happiness Score , display the top 10 , and plots them in a bar chart
5) Explore Happiness Factors
   Calculate the mean , maximum ,and minimum for GDP per capita, family/social support, healthy life expectancy, and freedom. A scatter plot compares GDP per capita with       happiness score
6) Correlation Heatmap
   Creates a heatmap showing correlations between happiness score, GDP per capita, family, life expectancy, freedom, and generosity. The YlGn color map is used

Expected Output
Dataset preview,Dataset shape and missing-value counts,Happiness score statistics,Top 10 happiest countries and a bar chart,Summary statistics for selected happiness factors,GDP-versus-happiness scatter plot,Correlation heatmap,Name of the highest-scoring country in the dataset

Conclusion 
This project demonstrates basic data analysis with Pandas and NumPy, and visualization with Matplotlib and Seaborn. It explores how happiness scores vary across countries and how selected economic and social indicators correlate with happiness. Correlation does not prove causation.

