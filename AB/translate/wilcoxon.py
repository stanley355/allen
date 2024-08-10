import pandas
from scipy.stats import wilcoxon

df = pandas.read_csv("AB/translate/AB_pre_post - translate.csv")

translate_cols = df[['ec_pre_translate', 'ec_post_translate', 'tu_pre_translate', 'tu_post_translate', 'ecpe_pre_translate', 'ecpe_post_translate']]

print("Translate:")
print("Event count", wilcoxon(translate_cols['ec_pre_translate'], translate_cols['ec_post_translate']))
print("Total users", wilcoxon(translate_cols['tu_pre_translate'], translate_cols['tu_post_translate']))
print("Event count per user", wilcoxon(translate_cols['ecpe_pre_translate'], translate_cols['ecpe_post_translate']))