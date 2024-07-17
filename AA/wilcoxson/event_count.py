import pandas

df = pandas.read_csv("AA/files/AA_pre_post - event_count.csv")

translate_data = df[['pre_translate', 'post_translate']]
print(translate_data)