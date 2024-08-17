import pandas
from statsmodels.multivariate.manova import MANOVA

df = pandas.read_csv("AB/checkbot/AB_pre_post - checkbot.csv")

checkbot_data = {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_pre_checkbot'], df['ec_post_checkbot']]).values,
    'total_users': pandas.concat([df['tu_pre_checkbot'], df['tu_post_checkbot']]).values,
    'event_count_per_user': pandas.concat([df['ecpe_pre_checkbot'], df['ecpe_post_checkbot']]).values
}

checkbot_df = pandas.DataFrame(checkbot_data)
checkbot_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', checkbot_df)
checkbot_result = checkbot_manova.mv_test()

print("Checkbot")
print(checkbot_result)

