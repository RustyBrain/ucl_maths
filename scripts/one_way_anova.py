import numpy as np


def one_way_anova(df, block_column, condition, calc_p=True):
    sum_squared_between_var = 0
    sum_squared_within_var = 0
    blocks = df[block_column].unique()
    block_dict = {}

    for block in blocks:
        block_dict[block] = df[df[block_column] == block][condition]

    for i, block in enumerate(blocks):
        sum_squared_between_var += block_dict[block].shape[0] * np.sum((block_dict[block].mean() - df[condition].mean())**2)
        sum_squared_within_var += np.sum((block_dict[block] - block_dict[block].mean())**2)
        index = i

    mean_sum_between_var = sum_squared_between_var / index
    mean_sum_within_var = sum_squared_within_var / (len(df) - (index + 1))
    f = mean_sum_between_var / mean_sum_within_var
    if calc_p:
        pass
    return f, p

