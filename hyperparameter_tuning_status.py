#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_training_trials():

    # hard-coded my result in  a list of (depth, nround, score) format
    res = [
        (15, 39, 0.87657),
        (16, 36, 0.87681),
        (16, 37, 0.87674),
        (16, 38, 0.87695),
        (16, 39, 0.87685),
        (17, 34, 0.87647),
        (17, 35, 0.87662),
        (17, 36, 0.87693),
        (17, 37, 0.87683),
        (18, 33, 0.87690),
        (18, 34, 0.87698),
        (18, 35, 0.87690),
        (25, 33, 0.87543),
        (25, 35, 0.87568),
        (28, 35, 0.87478),
        (30, 33, 0.87457)
    ]

    hp_tuning = pd.DataFrame(res, columns=['depth', 'nround', 'score'])
    hp_tuning_pivot = hp_tuning.pivot('depth', 'nround', 'score')

    return hp_tuning_pivot


if __name__ == '__main__':

    df = get_training_trials()
    sns.heatmap(df, annot=True, fmt="f")
    plt.title('XGBoost hyperparameter tuning')
    plt.show()

