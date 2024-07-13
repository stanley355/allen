import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# Sample data
data = {
    'promotion': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': [15,	11,	2,	4,	13, 7,	26,	1,	16,	15],
    'total_users': [2	,1,	1,	1,	3, 3	,6,	6,	3,	2],
    'event_count_per_user': [7.5,	11,	1,	4,	4.3,  2.3,	13,	1,	8	,15]
}

df = pd.DataFrame(data)

# Fit the multivariate regression model
manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ promotion', data=df)
result = manova.mv_test()

print(result)
