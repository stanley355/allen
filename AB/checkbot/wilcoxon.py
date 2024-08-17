import pandas
from scipy.stats import wilcoxon

df = pandas.read_csv("AB/checkbot/AB_pre_post - checkbot.csv")

checkbot_cols = df[['ec_pre_checkbot', 'ec_post_checkbot', 'tu_pre_checkbot', 'tu_post_checkbot', 'ecpe_pre_checkbot', 'ecpe_post_checkbot']]

print("Checkbot:")
print("Event count", wilcoxon(checkbot_cols['ec_pre_checkbot'], checkbot_cols['ec_post_checkbot']))
print("Total users", wilcoxon(checkbot_cols['tu_pre_checkbot'], checkbot_cols['tu_post_checkbot']))
print("Event count per user", wilcoxon(checkbot_cols['ecpe_pre_checkbot'], checkbot_cols['ecpe_post_checkbot']))