import pandas
from scipy.stats import wilcoxon

df = pandas.read_csv("AC/AC.csv")

week_cols = df[['week1_ec', 'week1_tu', 'week1_ecpu', 'week2_ec', 'week2_tu', 'week2)ecpu']]

print("Week 1 vs Week 2:")
print("Event count: ", wilcoxon(week_cols['week1_ec'], week_cols['week2_ec']))
print("Total users: ", wilcoxon(week_cols['week1_tu'], week_cols['week2_tu']))
print("Event count per user: ", wilcoxon(week_cols['week1_ecpu'], week_cols['week2_ecpu']))