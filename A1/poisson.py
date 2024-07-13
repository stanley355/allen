import pandas as pd
import numpy as np
import statsmodels.api as sm

# Define the data
pre_experiment = {
    'login': [3, 1, 3, 5, 6],
    'translate': [3, 3, 15, 1, 9],
    'checkbot': [15, 58, 2, 4, 13],
    'experiment': ['pre'] * 5
}

post_experiment = {
    'login': [7, 8, 6, 5, 0],
    'translate': [12, 26, 19, 22, 0],
    'checkbot': [7, 26, 1, 16, 0],
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
responses = ['login', 'translate', 'checkbot']

# Function to fit Poisson regression and print summary
def fit_poisson_model(response):
    model = sm.GLM(data[response], sm.add_constant(data['experiment']), family=sm.families.Poisson()).fit()
    print(f"\nPoisson Regression Results for {response.capitalize()}:")
    print(model.summary())

for response in responses:
    fit_poisson_model(response)