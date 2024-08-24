import pandas
from statsmodels.multivariate.manova import MANOVA

df = pandas.read_csv("AC/AC.csv")

data= {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['week3_ec'], df['week5_ec']]).values,
    'total_users': pandas.concat([df['week3_tu'], df['week5_tu']]).values,
    'event_count_per_user': pandas.concat([df['week3_ecpu'], df['week5_ecpu']]).values
}

data_df = pandas.DataFrame(data)
data_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', data_df).mv_test()

print("Week3 vs Week5: Multivariate")
print(data_manova)

