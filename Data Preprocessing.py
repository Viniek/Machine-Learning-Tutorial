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