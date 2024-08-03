import pandas
from scipy.stats import wilcoxon

df = pandas.read_csv("AB/texttospeech/AB_pre_post - Text to Speech.csv")


home_tts_cols = df[['ec_tts_home', 'ec_tts', 'tu_tts_home', 'tu_tts', 'ecpu_tts_home', 'ecpu_tts']]
students_tts_cols = df[['ec_tts_students', 'ec_tts', 'tu_tts_students', 'tu_tts', 'ecpu_tts_students', 'ecpu_tts']]

print("Home vs Tts:")
print("Event count", wilcoxon(home_tts_cols['ec_tts_home'], home_tts_cols['ec_tts']))
print("Total users", wilcoxon(home_tts_cols['tu_tts_home'], home_tts_cols['tu_tts']))
print("Event count per user", wilcoxon(home_tts_cols['ecpu_tts_home'], home_tts_cols['ecpu_tts']))
print("\n")
print("Students vs Tts:")
print("Event count", wilcoxon(students_tts_cols['ec_tts_students'], students_tts_cols['ec_tts']))
print("Total users", wilcoxon(students_tts_cols['tu_tts_students'], students_tts_cols['tu_tts']))
print("Event count per user", wilcoxon(students_tts_cols['ecpu_tts_students'], students_tts_cols['ecpu_tts']))