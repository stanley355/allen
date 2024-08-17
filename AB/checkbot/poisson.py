import pandas
import statsmodels.formula.api as smf

df = pandas.read_csv("AB/checkbot/AB_pre_post - checkbot.csv")

checkbot_data = {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_pre_checkbot'], df['ec_post_checkbot']]).values,
    'total_users': pandas.concat([df['tu_pre_checkbot'], df['tu_post_checkbot']]).values,
    'event_count_per_user': pandas.concat([df['ecpe_pre_checkbot'], df['ecpe_post_checkbot']]).values
}

checkbot_df = pandas.DataFrame(checkbot_data)

ec_checkbot_model = smf.poisson("event_count ~ experiment", checkbot_df).fit()
tu_checkbot_model = smf.poisson("total_users ~ experiment", checkbot_df).fit()
ecpe_checkbot_model = smf.poisson("event_count_per_user ~ experiment", checkbot_df).fit()

print("Checkbot")
print("EVENT COUNT:")
print(ec_checkbot_model.summary())
print("EVENT COUNT:")
print(tu_checkbot_model.summary())
print("EVENT COUNT PER USERS:")
print(ecpe_checkbot_model.summary())