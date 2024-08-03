import pandas
from statsmodels.multivariate.manova import MANOVA

df = pandas.read_csv("AB/texttospeech/AB_pre_post - Text to Speech.csv")

home_tts_data= {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_tts_home'], df['ec_tts']]).values,
    'total_users': pandas.concat([df['tu_tts_home'], df['tu_tts']]).values,
    'event_count_per_user': pandas.concat([df['ecpu_tts_home'], df['ecpu_tts']]).values
}

home_df = pandas.DataFrame(home_tts_data)
home_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', home_df)
home_result = home_manova.mv_test()

students_data = {
    'experiment': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    'event_count': pandas.concat([df['ec_tts_students'], df['ec_tts']]).values,
    'total_users': pandas.concat([df['tu_tts_students'], df['tu_tts']]).values,
    'event_count_per_user': pandas.concat([df['ecpu_tts_students'], df['ecpu_tts']]).values
}

students_df = pandas.DataFrame(students_data)
student_manova = MANOVA.from_formula('total_users + event_count + event_count_per_user ~ experiment', students_df)
student_reulst = student_manova.mv_test()

print("HOME VS TTS")
print(home_result)
print('\n')
print("STUDENTS VS TTS")
print(student_reulst)

