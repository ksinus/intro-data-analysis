import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from matplotlib.figure import Figure

import seaborn as sns

class YouTube2:
    def __init__(  # task0
            self,
            trends_df_path: str = "RUvideos_short.csv",
            categories_df_path: str = "RU_category_id.json"
    ):
        self.trends_df = pd.read_csv(trends_df_path)

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )

        self.categories_df['id'] = self.categories_df['id'].astype(int)
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df['trending_date'], format='%y.%d.%m')

    def task1(self) -> pd.DataFrame:
        self.trends_df = self.trends_df.merge(self.categories_df, left_on='category_id', right_on='id')
        return self.trends_df

    def task2(self) -> pd.DataFrame:
        return self.trends_df.pivot_table(
            values='views',
            index='name',
            columns='trending_date',
            aggfunc=np.sum)

    def task3(self) -> Figure:
        test = self.task2()
        test.replace(np.NaN, 0)
        ax = sns.heatmap(test / 10 ** 6, annot=True, fmt='.2g').set_title(
            'test name')
        return plt.gcf()


    def task4(self) -> pd.DataFrame:
        test = self.trends_df.pivot_table(
            values='views',
            index='name',
            columns='trending_date',
            aggfunc=np.sum,
            margins=True)
        test.rename(columns={'All':'Всего просмотров'}, inplace=True)
        return test
    def task5(self) -> Figure:
        test = self.task4()
        test.replace(np.NaN, 0)
        ax = sns.heatmap(test / 10 ** 6, annot=True, fmt='.2g', vmax=11).set_title(
            'test name')
        return plt.gcf()
