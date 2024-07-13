import pandas as pd
import numpy as np
import statsmodels.api as sm

# Define the data
pre_experiment = {
    'event_count': [15,	11,	2,	4,	13],
    'total_users': [2	,1,	1,	1,	3],
    'event_count_per_user': [7.5,	11,	1,	4,	4.3],
    'experiment': ['pre'] * 5
}

post_experiment = {
    'event_count': [7,	26,	1,	16,	15],
    'total_users': [3,	2,	1,	2,	1],
    'event_count_per_user': [2.3,	13,	1,	8	,15],
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