import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def split_telco_data(df):
    '''
    This function performs split on telco data, stratify churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test

def prep_telco_data(df):
    
    # convert total_charges to numeric
    df.total_charges = pd.to_numeric(df.total_charges, errors='coerce')

    # resets index column
    df.reset_index(inplace=True)

    # removes nulls
    df.dropna(how = 'any', inplace = True)

    # renames tenure column
    df = df.rename(columns = {'tenure':'tenure_mths'})
    
    # converts churn to 0/1
    df['churn'] = np.where(df.churn == 'Yes',1,0)

    # converts gender to 0/1
    df['gender'] = np.where(df.gender == 'Male',1,0)

    # replaces the payment types to 0/1
    df['payment_type'] = df.payment_type.replace({'Electronic check': 0,'Mailed check': 0, 'Bank transfer (automatic)': 1, 'Credit card (automatic)': 1})

    # converts remaining yes and no to 0/1
     
    df['online_security'] = df.online_security.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    
    df['online_backup'] = df.online_backup.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    
    df['device_protection'] = df.device_protection.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    
    df['tech_support'] = df.tech_support.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    
    df['contract_type'] = df.contract_type.replace({'Month-to-month':0, 'One year':1, 'Two year':2})
    
    df['internet_service_type'] = df.internet_service_type.replace({'None': 0, 'DSL': 1, 'Fiber optic': 1})
    
    df = df.drop('internet_service_type_id',axis=1)
    
    df = df.rename(columns = {'payment_type':'automatic_payment'})
    
    df['partner'] = df['partner'].replace({'No': 0, 'Yes': 1})
    
    df['dependents'] = df['dependents'].replace({'No': 0, 'Yes': 1})
    
    df['phone_service'] = df['phone_service'].replace({'No': 0, 'Yes': 1})
    
    df['paperless_billing'] = df['paperless_billing'].replace({'No': 0, 'Yes': 1})
    
    df['multiple_lines'] = df.multiple_lines.replace({'No phone service': 0, 'No': 1, 'Yes': 2})
    
    df['streaming_movies'] = df.streaming_movies.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    
    df['streaming_tv'] = df.streaming_tv.replace({'No internet service': 0, 'No': 0, 'Yes': 1})

    # Drop duplicate columns
    #df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'], inplace=True)
       
    # Drop null values stored as whitespace    
    #df['total_charges'] = df['total_charges'].str.strip()
    #df = df[df.total_charges != '']

    
    # Convert to correct datatype
    #df['total_charges'] = df.total_charges.astype(float)
    
    # Convert binary categorical variables to numeric
    #df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    #df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    #df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    #df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    #df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    #df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Get dummies for non-binary categorical variables
    dummy_df = pd.get_dummies(df.gender, drop_first=True)
    
    # Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

    # split the data
    # train, validate, test = split_telco_data(df)
    # #return train, validate, test


def percentage_stacked_plot(columns_to_plot, title, telco_df):
    
    '''
    Returns a 100% stacked plot of the response variable for independent variable of the list columns_to_plot.
    Parameters: columns_to_plot (list of string): Names of the variables to plot
    '''
    
    number_of_columns = 2
    number_of_rows = math.ceil(len(columns_to_plot)/2)

    # create a figure
    fig = plt.figure(figsize=(12, 5 * number_of_rows)) 
    fig.suptitle(title, fontsize=22,  y=.95)
 

    # loop to each column name to create a subplot
    for index, column in enumerate(columns_to_plot, 1):

        # create the subplot
        ax = fig.add_subplot(number_of_rows, number_of_columns, index)

        # calculate the percentage of observations of the response variable for each group of the independent variable
        # 100% stacked bar plot
        prop_by_independent = pd.crosstab(telco_df[column], telco_df['churn']).apply(lambda x: x/x.sum()*100, axis=1)

        prop_by_independent.plot(kind='bar', ax=ax, stacked=True,
                                 rot=0, color=['#94bad4','#ebb086'])

        # set the legend in the upper right corner
        ax.legend(loc="upper right", bbox_to_anchor=(0.62, 0.5, 0.5, 0.5),
                  title='Churn', fancybox=True)

        # eliminate the frame from the plot
        spine_names = ('top', 'right', 'bottom', 'left')
        for spine_name in spine_names:
            ax.spines[spine_name].set_visible(False)

    return percentage_stacked_plot

def draw_roc( actual, probs ):
    fpr, tpr, thresholds = metrics.roc_curve( actual, probs,
                                              drop_intermediate = False )
    auc_score = metrics.roc_auc_score( actual, probs )
    plt.figure(figsize=(5, 5))
    plt.plot( fpr, tpr, label='ROC curve (area = %0.2f)' % auc_score )
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate or [1 - True Negative Rate]')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic curve')
    plt.legend(loc="lower right")
    plt.show()

    return None
###

