import numpy as np
from scipy.stats import wilcoxon

# Pre experiment data
pre_login = np.array([3, 1, 3, 5, 6])
pre_translate = np.array([3, 3, 15, 1, 9])
pre_checkbot = np.array([15, 11, 2, 4, 13])

# Post experiment data
post_login = np.array([7, 8, 6, 5, 0])
post_translate = np.array([12, 26, 19, 22, 0])
post_checkbot = np.array([7, 26, 1, 16, 0])

# Perform Wilcoxon signed-rank test
def perform_wilcoxon_test(pre_data, post_data, variable_name):
    stat, p_value = wilcoxon(pre_data, post_data)
    print(f"{variable_name}: Wilcoxon test statistic = {stat}, p-value = {p_value}")
    if p_value < 0.05:
        print(f"Result: {variable_name} shows a statistically significant difference after the experiment.\n")
    else:
        print(f"Result: {variable_name} does not show a statistically significant difference after the experiment.\n")

perform_wilcoxon_test(pre_login, post_login, 'Login')
perform_wilcoxon_test(pre_translate, post_translate, 'Translate')
perform_wilcoxon_test(pre_checkbot, post_checkbot, 'Checkbot')