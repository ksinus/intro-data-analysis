from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp


class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
        self.df['trending_date'] = pd.to_datetime(
            self.df['trending_date'].apply(lambda x:
                                           x.split('.')[1] + "." +
                                           x.split('.')[2] + "." +
                                           x.split('.')[0]))
        return self.df

    def task2(self) -> pd.DataFrame:
        self.df = self.df.loc[:, ['trending_date',
                                  'category_id',
                                  'views',
                                  'likes',
                                  'dislikes',
                                  'comment_count']]
        self.df['trending_date'] = self.df['trending_date'].apply(lambda x: x.day)
        return self.df

    def task3(self) -> Figure:
        ax = sns.boxplot(x="trending_date", y="views",
                         data=self.df, palette="Set3").set_title('box plot')
        
        return plt.gcf()

    def task4(self) -> Figure:
        ax = sns.boxplot(x="trending_date", y="views",
                 data=self.df, palette="Set3", showfliers=False).set_title('box plot')
        
        return plt.gcf()

    def task5(self) -> Figure:
        ax = sns.jointplot(data=self.df, x="views", y="likes", hue="trending_date")
        plt.suptitle('test title')
        plt.xlabel('views')
        plt.ylabel('likws')
        return plt.gcf()

    def task6(self) -> Figure:
        q1 =  self.df['views'].quantile(0.25)
        q3 =  self.df['views'].quantile(0.75)
        self.df = self.df[(self.df['views'] > q1) & (self.df['views'] < q3)]

        q1 =  self.df['likes'].quantile(0.25)
        q3 =  self.df['likes'].quantile(0.75)
        self.df = self.df[(self.df['likes'] > q1) & (self.df['likes'] < q3)]

        ax = sns.jointplot(data=self.df, x="views", y="likes")
        plt.suptitle('test title')
        plt.xlabel('views')
        plt.ylabel('likes')
        return plt.gcf()
