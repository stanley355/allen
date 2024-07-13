import pandas as pd
import numpy as np
import statsmodels.api as sm

# Define the data
pre_experiment = {
    'event_count': [3,	3,	15,	1,	9],
    'total_users': [1	,1,	3,	1	,2],
    'event_count_per_user': [3,	1,	5,	1,	4.5],
    'experiment': ['pre'] * 5
}

post_experiment = {
    'event_count': [12,	26,	19,	22,	5],
    'total_users': [3	,6,	6,	3,	2],
    'event_count_per_user': [4,	4.3,	3.17,	7.3,	2.5],
    'experiment': ['post'] * 5
}

# Convert the dictionaries to dataframes
pre_df = pd.DataFrame(pre_experiment)
post_df = pd.DataFrame(post_experiment)

# Combine the dataframes
data = pd.concat([pre_df, post_df], ignore_index=True)

# Encode the experiment variable as numerical values
data['experiment'] = data['experiment'].map({'pre': 0, 'post': 1})

# Variables to model
responses = ['event_count', 'total_users', 'event_count_per_user']

# Function to fit Poisson regression and print summary
def fit_poisson_model(response):
    model = sm.GLM(data[response], sm.add_constant(data['experiment']), family=sm.families.Poisson()).fit()
    print(f"\nPoisson Regression Results for {response.capitalize()}:")
    print(model.summary())

for response in responses:
    fit_poisson_model(response)