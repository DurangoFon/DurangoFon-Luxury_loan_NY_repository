# DurangoFon-Luxury_loan_NY_repository

## requirements 
The requirements are inside the file requirements.txt, and can be install with: 
```bash
    pip install -r requirements.txt
```
## Data 
The data will be downloaded by the script called (data_addition.py) that will run inside the notebook
## 1. Summary
This project contain varios process of identification and imputation data of a data set publish in kaggle, this data were study and compare multiple time for offer the best solution with the essencial information detected. 

## 2. Procedure 
The procedure will be explain in the follow steps:
### 2.1 Data Load
 - The data is download from kaggle
 - Inserted in the folder call "Data"
 - Loaded into the notebook using Pandas

### 2.1 Exploration and imputation
The first impression marked this dataset without missing data, but the land and gross characteristics were storage as object, this atributes can be used in the model, for this reason was necessary change the data type as integer leaving with more of 50% spaces missing, resulting in a imputation process.

 - With no posible grafics the focus was identify posible problems
 - After identify that the data type were an object it was transform as integer
 - This porcedure leave a large amount of missing data that is necessary impute 
 - After some study, the data missing were change with the value 0, due the relation that is not always present and can be a deeper focus for next approximations

### 2.3 Monovariable analysis
 - After been charged the data is analysis by variables
 - With pandas describe module is posible observe the limits and behaviour of those characteristics
 - All characteristic describe were necessary observe in grafics this behaviour like, linear or normal relation.

### 2.4 Multivariable analysis 
 - Knowing the behaviours of variables individualy, the result of identify relation between this is identify by a correlation matrix expose as a heatmap.
 - With this conclusions the plannification of machine learning models can be add 
 - After see and collect which atributes can be define or predict by others were separate and passe for the prediction process

### 2.5 Machine learning models 
 - Important data were separate, the reason is eliminate the maximun noise posible. 
 - The models build were linear regressions with multiple variables.
 - The final result are expose inside the notebook blocks were it is build
