import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes


class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):  # task0
        self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
        return self.df.head(5)

    def task2(self) -> tp.List[str]:
        df_isna = self.df.isna()
        columns_list = self.df.columns.tolist()

        for column in columns_list:
            if (pd.Series(df_isna[column]).sum() == 0):
                columns_list.remove(column)

        return columns_list

    def task3(self) -> pd.DataFrame:
        self.df.dropna(inplace = True)
        return self.df

    def task4(self) -> pd.DataFrame:
        return self.df.describe()

    def task5(self) -> int:
        return (self.df['test_score'] == 100).sum()

    def task6(self) -> pd.DataFrame:
        rslt_df = self.df[self.df['test_score'] == 100]
        cnt = rslt_df['school'].value_counts().to_dict()
        
        rslt_df['cnt_100'] = rslt_df['school'].map(cnt)
        rslt_df = rslt_df.drop_duplicates()
        rslt_df = rslt_df.drop('test_score', 1)
        rslt_df = rslt_df.sort_values(by = ['cnt_100', 'school'], ascending = False)
        
        return rslt_df

    
    def task7(self) -> pd.DataFrame:
        tmp = self.df
        tmp = tmp.groupby(['school']).mean()
        tmp = tmp.sort_values(by=['test_score'], ascending=False)
        tmp = tmp.reset_index()
        return tmp.head(10)

    def task8(self) -> pd.DataFrame:
        tmp = self.df
        tmp = tmp.groupby(['school']).mean()
        tmp = tmp.sort_values(by=['test_score'], ascending=False)
        tmp = tmp.reset_index()
        return tmp.tail(10)

    def task9(self) -> Axes:
        schools = self.df
        schools['size'] = schools['number_of_students'].apply(lambda x: 'small'
        if x <= 1000 else 'big')

        big_schools, small_schools = [school for _, school in schools.groupby(schools['size'] == 'small')]
        plt.title('my plot')
        plt.hist(x = small_schools['test_score'], alpha = 0.5, bins = 10, label = "small_schools")
        plt.hist(x = big_schools['test_score'], alpha = 0.5, bins = 10, label = "big_schools")
        plt.legend()
        plt.gca().set(xlabel='x', ylabel='y')
        return plt.gca()
