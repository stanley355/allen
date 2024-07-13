import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# Sample data
data = {
    'Promotion': [0, 1, 0, 1, 0, 1],
    'Total_Users': [1000, 1200, 1100, 1300, 1050, 1250],
    'Event_Count': [5000, 6000, 5500, 6500, 5250, 6250],
    'Event_Count_per_User': [5, 5, 5, 5, 5, 5]
}

df = pd.DataFrame(data)

# Fit the multivariate regression model
manova = MANOVA.from_formula('Total_Users + Event_Count + Event_Count_per_User ~ Promotion', data=df)
result = manova.mv_test()

print(result)
