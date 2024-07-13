import numpy as np
from scipy.stats import wilcoxon

# Pre experiment data
pre_event_count = np.array([3,	3,	15,	1,	9])
pre_total_user = np.array([1	,1,	3,	1	,2])
pre_event_count_per_user = np.array([3,	1,	5,	1,	4.5])

# Post experiment data
post_event_count = np.array([12,	26,	19,	22,	5])
post_total_user = np.array([3	,6,	6,	3,	2])
post_event_count_per_user = np.array([4,	4.3,	3.17,	7.3,	2.5])

# Perform Wilcoxon signed-rank test
def perform_wilcoxon_test(pre_data, post_data, variable_name):
    stat, p_value = wilcoxon(pre_data, post_data)
    print(f"{variable_name}: Wilcoxon test statistic = {stat}, p-value = {p_value}")
    if p_value < 0.05:
        print(f"Result: {variable_name} shows a statistically significant difference after the experiment.\n")
    else:
        print(f"Result: {variable_name} does not show a statistically significant difference after the experiment.\n")

print("Translate")
perform_wilcoxon_test(pre_event_count, post_event_count, 'Event Count: ')
perform_wilcoxon_test(pre_total_user, post_total_user , 'Total User: ')
perform_wilcoxon_test(pre_event_count_per_user, post_event_count_per_user, 'Event Count per User')