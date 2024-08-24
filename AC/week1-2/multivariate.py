import pandas
from statsmodels.multivariate.manova import MANOVA

df = pandas.read_csv("AC/AC.csv")

data= {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['week1_ec'], df['week2_ec']]).values,
    'total_users': pandas.concat([df['week1_tu'], df['week2_tu']]).values,
    'event_count_per_user': pandas.concat([df['week1_ecpu'], df['week2_ecpu']]).values
}

data_df = pandas.DataFrame(data)
data_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', data_df).mv_test()

print("Week 1 vs Week 2: Multivariate")
print(data_manova)

