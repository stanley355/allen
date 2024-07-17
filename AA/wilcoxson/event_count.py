import pandas
import scipy.stats as stats

df = pandas.read_csv("AA/files/AA_pre_post - event_count.csv")

pre_translate = df['pre_translate']
post_translate = df['post_translate']
translate_wilcoxson = stats.wilcoxson(pre_translate, post_translate)
print(translate_wilcoxson)