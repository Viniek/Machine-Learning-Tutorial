'''Data preprocessing is the process of evaluating, filtering, manipulating, 
and encoding data so that a machine learning algorithm can understand it and use the resulting output. 
-The major goal of data preprocessing is to eliminate data issues such as :
  -missing values, 
  -improve data quality and 
  -make the data useful for machine learning purposes.

  Importance of Data Preprocessing 

  As the adage goes, “If garbage goes in, garbage comes out.” 
  -Your data project will only be as successful as the input 
  data you feed into your machine learning algorithms.

         1.It Improves Data Quality

Data preprocessing is the fast track to improving data quality since many of its steps mirror activities
 you’ll find in any data quality management process, such as data cleansing, data profiling,
data integration, and more.

         2.It Handles Missing Data

-There are several reasons why a data collection may be missing values (particular fields of data). 
-Data practitioners must determine if it’s best to reject records with missing values, ignore them,
 or fill them in with an estimated value.

        3.It Normalizes and Scales Data

-Dependent and independent variables change on separate scales, or one changes linearly while another
 changes exponentially.
 -Normalizing and scaling help to modify data in a way that allows computers to extract a meaningful 
 link between these variables.
 -Salary, for example, might be a multiple-figure digit, whereas age is expressed in double digits. 
 
        4.It Eliminates Duplicate Records

  -When two records appear to repeat, an algorithm must identify whether the same metric was captured
   twice or whether the data reflects separate occurrences.
   -Techniques for finding, deleting, or connecting duplicates help to address such data quality issues
    automatically.

        5.It Handles Outliers

  -Data practitioners sometimes need to merge many data sources to construct a new machine learning model. 
  example:
   -Principal component analysis is an important technique for lowering the number of dimensions in the 
   training data set and producing a more efficient representation.

 Data Preprocessing Steps in Machine Learning.

                1. Acquire the Dataset
 -Naturally, data collection is the first step in any machine learning project and the first among the data
  preprocessing steps. 
  For example, the marketing team might have access to a CRM system, but that system may operate in isolation
   from the web analytics solution. Combining all data streams into consolidated storage will be challenging.

               2. Import Libraries
-A library is a collection of functions that an algorithm can call and utilize.
-You can streamline data preprocessing procedures using tools and frameworks that make the process easier to
 organize and execute.

               3. Import Datasets
  -This is the most critical machine learning preprocessing step.
  -It involves  loading the data that will be utilized in the machine learning algorithm. 
  -Warehouses are commonly used to access data through business intelligence interfaces in 
  order to observe metrics that we know we need to monitor.   

               4. Check for Missing Values       
  -Evaluate the data and look for missing values.
   Missing values can break actual data trends and potentially result in additional data loss
    when entire rows and columns are deleted due to a few missing cells in the dataset.
               5.Encode the Data
-Non-numerical data is incomprehensible to machine learning modules. To avoid issues later on, the data should be arranged numerically. 
               6. Scaling
               7. Split Dataset Into Training, Evaluation and Validation Sets
 -This is the final step among the data preprocessing steps. 
 - The training set is the data you’ll use to train your machine learning model.
  The evaluation set will assess the data and the model, while the validation set will validate it.             

         Data Preprocessing  Techniques
1.Data Transformation
-It changes data from one format to another.
-Example => the KNN model uses distance measurements to 
determine which neighbors are closest to a particular record.

2.Feature Engineering
-The feature engineering strategy is used to produce better features
 for your dataset, which will improve the model’s performance

 3.Imbalanced Data
 -One of the most prevalent issues you may encounter while working with 
 real-world data categorization is that the classes are unbalanced 
 (one contains more samples than the other), resulting in a significant
  bias for the model.


Techniques you can use to solve this problem:
-Oversampling – 
Oversampling is the technique of augmenting your dataset with generated data from the minority class. The Synthetic Minority Oversampling Technique (SMOTE) is the most commonly used method for doing this; 
it selects a random sample from the minority class.