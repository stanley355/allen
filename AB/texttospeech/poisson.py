import pandas
import statsmodels.formula.api as smf

df = pandas.read_csv("AB/texttospeech/AB_pre_post - Text to Speech.csv")

home_tts_data= {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_tts_home'], df['ec_tts']]).values,
    'total_users': pandas.concat([df['tu_tts_home'], df['tu_tts']]).values,
    'event_count_per_user': pandas.concat([df['ecpu_tts_home'], df['ecpu_tts']]).values
}

home_df = pandas.DataFrame(home_tts_data)
ec_home = smf.poisson("event_count ~ experiment", home_df).fit()
tu_home = smf.poisson("total_users ~ experiment", home_df).fit()
ecpu_home = smf.poisson("event_count_per_user ~ experiment", home_df).fit()

print("HOME VS TTS")
print("EVENT COUNT:")
print(ec_home.summary())
print("TOTAL_USERS:")
print(tu_home.summary())
print("EVENT COUNT PER USERS:")
print(ecpu_home.summary())


students_data = {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_tts_students'], df['ec_tts']]).values,
    'total_users': pandas.concat([df['tu_tts_students'], df['tu_tts']]).values,
    'event_count_per_user': pandas.concat([df['ecpu_tts_students'], df['ecpu_tts']]).values
}

students_df = pandas.DataFrame(students_data)
ec_students = smf.poisson("event_count ~ experiment", students_df).fit()
tu_students= smf.poisson("total_users ~ experiment", students_df).fit()
ecpu_students = smf.poisson("event_count_per_user ~ experiment", students_df).fit()

print("\n\n")
print("STUDENTS VS TTS")
print("EVENT COUNT:")
print(ec_students.summary())
print("TOTAL_USERS:")
print(tu_students.summary())
print("EVENT COUNT PER USERS:")
print(ecpu_students.summary())