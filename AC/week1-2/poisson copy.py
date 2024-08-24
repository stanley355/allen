import pandas
import statsmodels.formula.api as smf

df = pandas.read_csv("AB/translate/AB_pre_post - translate.csv")

df = pandas.read_csv("AC/AC.csv")

data= {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['week1_ec'], df['week2_ec']]).values,
    'total_users': pandas.concat([df['week1_tu'], df['week2_tu']]).values,
    'event_count_per_user': pandas.concat([df['week1_ecpu'], df['week2_ecpu']]).values
}

data_df = pandas.DataFrame(data)
ec_sum = smf.poisson("event_count ~ experiment", data_df).fit().summary()
tu_sum = smf.poisson("total_users ~ experiment", data_df).fit().summary()
ecpu_sum = smf.poisson("event_count_per_user ~ experiment", data_df).fit().summary()

print("WEEK 1 VS WEEK 2")
print("EVENT COUNT:")
print(ec_sum)
print("TOTAL USERS:")
print(tu_sum)
print("EVENT COUNT PER USERS:")
print(ecpu_sum)
