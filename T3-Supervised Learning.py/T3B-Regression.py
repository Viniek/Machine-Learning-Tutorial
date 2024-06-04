# Linear regression is a type of supervised machine learning algorithm that computes the linear 
# relationship between the dependent variable and one or more independent features by fitting a linear 
# equation to observed data.
# -When there is only one independent feature, it is known as Simple Linear Regression, and
#  when there are more than one feature, it is known as Multiple Linear Regression.
#  -Similarly, when there is only one dependent variable, it is considered Univariate Linear Regression, 
#  while when there are more than one dependent variables, it is known as Multivariate Regression.

#            Types of Linear Regression
#   1. Simple Linear Regression 

#   -This is the simplest form of linear regression, and it involves only one independent variable and 
#   one dependent variable. The equation for simple linear regression is:   
#   y=β0 +β1 X+ε 
#   where:
# Y is the dependent variable
# X is the independent variable
# β0 is the intercept
# β1 is the slope
# ε  is the error term. (For a good model it will be negligible

# Example of Simple Linear Regression:
# -Here we are taking a dataset that has two variables: salary (dependent variable) and experience 
# (Independent variable). 

#   The goals of this problem is:
# -We want to find out if there is any correlation between these two variables
# -We will find the best fit line for the dataset.
# -How the dependent variable is changing by changing the independent variable.
# -In this section, we will create a Simple Linear Regression model to find out the best fitting line 
# for representing the relationship between these two variables.
# Step-1: Data Pre-processing
# ​
#  STEP1:We will import the three important libraries, which will help us for loading the dataset,
#   plotting the graphs, and creating the Simple Linear Regression model.
import numpy as nm
import matplotlib.pyplot as matp
import pandas as pd

#    STEP2: We will load the dataset into our code:
data_set=pd.read_csv("Salary_Data.csv")

# By executing the above line of code (ctrl+ENTER), we can read the dataset on our Spyder IDE
#  screen by clicking on the variable explorer option.
# ​NoteBetter: In Spyder IDE, the folder containing the code file must be saved as a working directory, 
# and the dataset or csv file should be in the same folder.
  
# STEP3:We will extract the dependent and independent variables from the given dataset.
#  The independent variable is years of experience, and the dependent variable is salary.

x=data_set.iloc[:,:-1].values
y=data_set.iloc[:,1].values
# In the above lines of code, for x variable, we have taken -1 value since we want to
#  remove the last column from the dataset. For y variable, we have taken 1 value as a parameter,
#  since we want to extract the second column and indexing starts from the zero.
# By executing the above line of code, we will get the output for X and Y variable as:

 