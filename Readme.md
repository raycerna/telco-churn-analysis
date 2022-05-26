# Telco Churn Predictions

This is a repository for the Telco churn classification project.


Customer churn, also known as customer attrition, customer turnover, or customer defection, is the loss of clients or customers. In the telecommunication industry it is critical to retain customers because it is often more costly to acquire new ones. The goal of this project is to find identify those drivers which cause customer churn at Telco.


## quetions and initial hypothesis that came to thought

`Does tech support affect different rates of churn?`
#### 𝐻0  : tech support does not affect churn
#### 𝐻𝑎  : tech support does affect a customer churning

`Does device protection affect different rates of churn?`
#### 𝐻0  : device protection does not affect churn
#### 𝐻𝑎  : device protection does affect a customer churning

`Does online security affect different rates of churn?`
#### 𝐻0  : having online security does not affect churn
#### 𝐻𝑎  : online security does affect a customer churning

### Having additional services prevents a customer from churning

## Additional hypotheses
`Is there a relationship monthly charges and when (tenure) a customer will churn?`
#### 𝐻0 : There is no linear correlation between monthly charges and whether a customer will churn.
#### 𝐻𝑎 : There is a linear relationship between monthly charges and whether a customer will churn.


## Data dictionary from Raw Data

| Feature                   | Definition                               | Data Type       |
|---------------------------|------------------------------------------|-----------------|
|contract_type_id           |numerical value for contract_type         | int64           |
|internet_service_type_id   |numerical value for internet_service_type | int64           |              
|customer_id                |account # for customer                    | object          |
|gender                     |male or female                            | object          |
|senior_citizen             |senior citizen or not                     | int64           |
|partner                    |parnter or not                            | object          |
|dependents                 |dependents or not                         | object          |
|tenure                     |duration with company in months           | int64           |
|phone_service              |phone service or not                      | object          |
|multiple_lines             |more than one line or not                 | object          |
|online_security            |online security or not                    | object          |
|online_backup              |online backup or not                      | object          |
|device_protection          |device protection or not                  | object          |
|tech_support               |tech support or not                       | object          |
|streaming_tv               |streaming tv or not                       | object          |
|streaming_movies           |streaming movies or not                   | object          |
|paperless_billing          |paperless bills or not                    | object          |
|monthly_charges            | in USD                                   | float64         |
|total_charges              | in USD                                   | object          |
|churn                      | loss of customer or not                  | object          |
|internet_service_type      | DSL, Fiber optic, or none                | object          |
|contract_type              | Two-year, One-year, Month-to-month       | object          |
|payment_type               | different types of payment methods       | object          |



## project planning 
- Acquire
    - Acquired data using SQL from the telco_churn database.
        - Note: Functions to acquire data are built into the acquire.py file.
    - Loaded and inspected dataset

- Prepare
    - After inspecting dataset it was observed that it contained both numerical and non-numerical columns, timeframe, missing values, and duplicates.
    - Coverted/replaced features where definitions were Yes or No and changed to 1 for Yes and 0 for No.
    - Features that had more than 2 object definitios were replaced with 0, 1, and 2.
    - Grouped payment types by automatic and manual.
    - Drop null values and replaced with 0 in total and monthly charges.
    - Created a stacked bar plot function to return visuals from features in question.
    - Created a ROC Curve to plot performance of top performing model
    - Built function that performs split on telco data, stratify churn. Returns train, validate, and test dataframes.

- Explore
    - Performed univariate analysis on individual predictors of churn.
    - Performed bivariate and multivariate exploration on several features to find easy recommendations to improve and prevent churn.
        -Online security, tech support, and device protection were all related.
    - Further explored features that I questioned in my initial hypothesis.
    - Visualized features of churn by using countplots and stackedplots and kdeplots.

- Model
    - Train, validated, and tested the predictors/independent features.
    - Determined my baseline prediciton at 73%.
    - Trained on three different classification models.
        - Logistic Regression
        - Random Forest
        - K-Nearest Neighbors
    - Validated on two since they were nearly identical.
        - KNN and Random Forest
    - Chose Random Forest for Test model after highest accuracy on validate.

## instructions on how to reproduce this project and findings

- Copy the acquire.py, prepare.py, and telco_analysis.ipynb
- Run telco_analysis.ipynb then further explore or reprepare data to your liking.

## key findings, recommendations, and takeaways from project

- It is evident that contract type is the highest indicator for customers to churn. My suggestion would be to offer a discount for subscribing to a one-year thus showing the customer they would save money in the long run.
- There is currently no option to bundle packages for internet service to include online_security, device_protection, and tech_support. It was evident that if a customer did not have one of these they were more likely to churn. My suggestion would be to bundle all these together at a discounted rate.
- Our best performing model obtained an accuracy of 76% ~3% higher than baseline.

*** NOTE: With more time we can determine the amount of revenue we can increase with my recommendations.