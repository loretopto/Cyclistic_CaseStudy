import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# appending all the 4 quarters to a single list
def quarter_append(dataQ1,dataQ2,dataQ3,dataQ4):
    columns_name = list(dataQ1.columns)
    dataQ2.columns = columns_name
    dataQ3.columns = columns_name
    dataQ4.columns = columns_name

    total_data = pd.concat([dataQ1, dataQ2, dataQ3, dataQ4], ignore_index=True)

    return total_data


# checking data composition
def data_check(data):
    print(data.describe())
    print(data.shape)
    print(data.head(20))
    print(data.isna().any())
    print(data.nunique())
    print(data.dtypes)
    data['usertype'].value_counts()

    # corrmat = data.corr()
    # sns.heatmap(corrmat, vmax=0.9, square=False)
    # plt.show()


# cleaning data and removing wrong values and converting dates
def data_cleaning(data):

    data["birthyear"].mask(data["birthyear"] <= 1919, np.NaN, inplace=True)
    # print(data.birthyear.unique())

    data['start_time'] = pd.to_datetime(data['start_time'], format="%Y-%m-%d %H:%M:%S")
    data['end_time'] = pd.to_datetime(data['end_time'], format="%Y-%m-%d %H:%M:%S")
    data['month'] = pd.DatetimeIndex(data['start_time']).month

    return data


# check why some id have two names.
# Result: They refer to the same station but they are named differently
def check_if_uniqueID(data):
    data = data.drop(columns=['trip_id','start_time','end_time','bikeid','tripduration','usertype','gender','birthyear','to_station_id','to_station_name'])
    group = data.groupby(["from_station_id"])["from_station_name"].nunique().reset_index(name='count')
    true_groupcount = group[group['count']>1]

    list_unique = []
    for index, row in true_groupcount.iterrows():
        stationname = (data[data['from_station_id']==row['from_station_id']])
        uniquesstationname = stationname['from_station_name'].unique()
        print(uniquesstationname)
