# Telco Churn Predictions

This is a repository for the Telco churn classification project.


Customer churn, also known as customer attrition, customer turnover, or customer defection, is the loss of clients or customers. In the telecommunication industry it is critical to retain customers because it is often more costly to acquire new ones. The goal of this project is to find identify those drivers which cause customer churn at Telco.


## initial hypothesis and quetions that came to thought

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
    - Acquired data using SQL from the telco_churn database
- Prepare

## instructions or an explanation of how someone else can reproduce this project and findings



## key findings, recommendations, and takeaways from your project.

