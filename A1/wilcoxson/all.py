import numpy as np
from scipy.stats import wilcoxon

# Pre experiment data
pre_event_count = np.array([3, 1, 3, 5, 6, 3,	3,	15,	1,	9, 3,	1,	5,	1,	4.5])
pre_total_user = np.array([2,	1,	3,	2,	5, 1	,1,	3,	1	,2, 2	,1,	1,	1,	3])
pre_event_count_per_user = np.array([1.5,	1,	1,	2.5,	1.2, 7.5,	11,	1,	4,	4.3])

# Post experiment data
post_event_count = np.array([7, 8, 6, 5, 2, 12,	26,	19,	22,	5, 7,	26,	1,	16,	15])
post_total_user = np.array([5,	5,	6,	3,	2, 3	,6,	6,	3,	2, 3,	2,	1,	2,	1])
post_event_count_per_user = np.array([1.4,	1.6,	1,	1.67,	1, 2.3,	13,	1,	8	,15])

# Perform Wilcoxon signed-rank test
def perform_wilcoxon_test(pre_data, post_data, variable_name):
    stat, p_value = wilcoxon(pre_data, post_data)
    print(f"{variable_name}: Wilcoxon test statistic = {stat}, p-value = {p_value}")
    if p_value < 0.05:
        print(f"Result: {variable_name} shows a statistically significant difference after the experiment.\n")
    else:
        print(f"Result: {variable_name} does not show a statistically significant difference after the experiment.\n")

print("Overall")
perform_wilcoxon_test(pre_event_count, post_event_count, 'Event Count: ')
perform_wilcoxon_test(pre_total_user, post_total_user , 'Total User: ')
perform_wilcoxon_test(pre_event_count_per_user, post_event_count_per_user, 'Event Count per User')