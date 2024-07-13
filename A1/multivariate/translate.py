import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# Sample data
data = {
    'promotion': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': [3,	3,	15,	1,	9, 12,	26,	19,	22,	5],
    'total_users': [1	,1,	3,	1	,2, 3	,6,	6,	3,	2],
    'event_count_per_user': [3,	1,	5,	1,	4.5, 4,	4.3,	3.17,	7.3,	2.5]
}

df = pd.DataFrame(data)

# Fit the multivariate regression model
manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ promotion', data=df)
result = manova.mv_test()

print(result)
