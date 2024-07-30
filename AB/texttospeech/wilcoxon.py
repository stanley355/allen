import pandas
from scipy.stats import wilcoxon

df = pandas.read_csv("AB/students/AB_pre_post - students.csv")

translate_cols = df[['ec_pre_translate', 'ec_post_translate', 'tu_pre_translate', 'tu_post_translate', 'ecpe_pre_translate', 'ecpe_post_translate']]
checkbot_cols = df[['ec_pre_checkbot', 'ec_post_checkbot', 'tu_pre_checkbot', 'tu_post_checkbot', 'ecpe_pre_checkbot', 'ecpe_post_checkbot']]

print("Translate:")
print("Event count", wilcoxon(translate_cols['ec_pre_translate'], translate_cols['ec_post_translate']))
print("Total users", wilcoxon(translate_cols['tu_pre_translate'], translate_cols['tu_post_translate']))
print("Event count per user", wilcoxon(translate_cols['ecpe_pre_translate'], translate_cols['ecpe_post_translate']))
print("\n")
print("Checkbot:")
print("Event count", wilcoxon(checkbot_cols['ec_pre_checkbot'], checkbot_cols['ec_post_checkbot']))
print("Total users", wilcoxon(checkbot_cols['tu_pre_checkbot'], checkbot_cols['tu_post_checkbot']))
print("Event count per user", wilcoxon(checkbot_cols['ecpe_pre_checkbot'], checkbot_cols['ecpe_post_checkbot']))