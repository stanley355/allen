import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# Sample data
data = {
    'promotion': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'total_users': [1000, 1200, 1100, 1300, 1050, 1250],
    'event_count': [5000, 6000, 5500, 6500, 5250, 6250],
    'event_count_per_user': [5, 5, 5, 5, 5, 5]
}

df = pd.DataFrame(data)

# Fit the multivariate regression model
manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ promotion', data=df)
result = manova.mv_test()

print(result)
