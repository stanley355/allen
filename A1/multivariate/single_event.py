import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# Sample data
data = {
    'promotion': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'login': [1000, 1200, 1100, 1300, 1050, 1250],
    'translate': [5000, 6000, 5500, 6500, 5250, 6250],
    'checkbot': [5, 5, 5, 5, 5, 5]
}

df = pd.DataFrame(data)

# Fit the multivariate regression model
manova = MANOVA.from_formula('login + translate + checkbot ~ promotion', data=df)
result = manova.mv_test()

print(result)