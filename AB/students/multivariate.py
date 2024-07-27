import pandas
from statsmodels.multivariate.manova import MANOVA

df = pandas.read_csv("AB/homepage/AB_pre_post - students.csv")

translate_data = {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_pre_translate'], df['ec_post_translate']]).values,
    'total_users': pandas.concat([df['tu_pre_translate'], df['tu_post_translate']]).values,
    'event_count_per_user': pandas.concat([df['ecpe_pre_translate'], df['ecpe_post_translate']]).values
}

translate_df = pandas.DataFrame(translate_data)
translate_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', translate_df)
translate_result = translate_manova.mv_test()

checkbot_data = {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_pre_checkbot'], df['ec_post_checkbot']]).values,
    'total_users': pandas.concat([df['tu_pre_checkbot'], df['tu_post_checkbot']]).values,
    'event_count_per_user': pandas.concat([df['ecpe_pre_checkbot'], df['ecpe_post_checkbot']]).values
}

checkbot_df = pandas.DataFrame(checkbot_data)
checkbot_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', checkbot_df)
checkbot_result = checkbot_manova.mv_test()

print("Translate")
print(translate_result)
print('\n')
print("Checkbot")
print(checkbot_result)

