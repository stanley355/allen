import pandas
from scipy.stats import wilcoxon

df = pandas.read_csv("AA/files/AA_pre_post - All.csv")

translate_cols = df[['ec_pre_translate', 'ec_post_translate', 'tu_pre_translate', 'tu_post_translate', 'ecpe_pre_translate', 'ecpe_post_translate']]
# post_translate = df['post_translate']
# translate_wilcoxson = wilcoxon(pre_translate[0], pre_translate[0])

print(translate_cols)
# print(translate_wilcoxson)