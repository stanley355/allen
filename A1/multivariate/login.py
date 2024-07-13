import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# Sample data
data = {
    'promotion': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': [3, 1, 3, 5, 6, 7, 8, 6, 5, 2],
    'total_users': [2,	1,	3,	2,	5, 5,	5,	6,	3,	2],
    'event_count_per_user': [1.5,	1,	1,	2.5,	1.2, 1.4,	1.6,	1,	1.67,	1]
}

df = pd.DataFrame(data)

# Fit the multivariate regression model
manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ promotion', data=df)
result = manova.mv_test()

print(result)
