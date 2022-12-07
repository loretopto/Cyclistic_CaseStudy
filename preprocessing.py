import numpy as np
import pandas as pd

usertype_boolean = {"Subscriber": 0, "Customer": 1}
gender_boolean = {"Female": 0, "Male": 1}

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
    print("This is a description of your data:")
    print(data.describe())

    print("This is the shape of your data:")
    print(data.shape)

    print("This are the first values of your data:")
    print(data.head(20))

    print("This tells if a columns missises values:")
    print(data.isna().any())

    print("This tells how many unique values a column has:")
    print(data.nunique())

    print("This are the datatypes of your data:")
    print(data.dtypes)


# cleaning data and removing wrong values and converting dates
def data_cleaning(data):

    data["birthyear"].mask(data["birthyear"] <= 1919, np.NaN, inplace=True)
    # print(data.birthyear.unique())

    data['start_time'] = pd.to_datetime(data['start_time'], format="%Y-%m-%d %H:%M:%S")
    data['end_time'] = pd.to_datetime(data['end_time'], format="%Y-%m-%d %H:%M:%S")
    data['month'] = pd.DatetimeIndex(data['start_time']).month
    data['day'] = pd.DatetimeIndex(data['start_time']).day
    data['weekday'] = pd.DatetimeIndex(data['start_time']).weekday
    data['hour'] = pd.DatetimeIndex(data['start_time']).hour

    data['tripduration'] = pd.to_numeric(data['tripduration'], errors='coerce')

    data = data.drop(columns=['from_station_name', 'to_station_name', 'start_time', 'end_time'])

    data.replace({"gender": gender_boolean, "usertype": usertype_boolean}, inplace=True)

    return data


# check why some id have two names.
# Result: They refer to the same station but they are named differently
def check_if_uniqueID(data):
    # data = data.drop(columns=['trip_id','start_time','end_time','bikeid','tripduration','usertype','gender','birthyear','to_station_id','to_station_name'])
    # group = data.groupby(["from_station_id"])["from_station_name"].nunique().reset_index(name='count')
    # true_groupcount = group[group['count']>1]
    #
    # list_unique = []
    # for index, row in true_groupcount.iterrows():
    #     stationname = (data[data['from_station_id']==row['from_station_id']])
    #     uniquesstationname = stationname['from_station_name'].unique()
    #     print(uniquesstationname)

    data = data.drop(columns=['trip_id','start_time','end_time','bikeid','tripduration','usertype','gender','birthyear','from_station_id','from_station_name'])
    group = data.groupby(["to_station_id"])["to_station_name"].nunique().reset_index(name='count')
    true_groupcount = group[group['count']>1]

    list_unique = []
    for index, row in true_groupcount.iterrows():
        stationname = (data[data['to_station_id']==row['to_station_id']])
        uniquesstationname = stationname['to_station_name'].unique()
        print(uniquesstationname)
