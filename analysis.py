import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def correlmat(data):
    corrmat = data.corr()
    sns.heatmap(corrmat, vmax=0.9, square=False)
    plt.show()

def groupingby(data):
    groupby_month = data.groupby(['month'])['month'].count()
    print("Month group: \n", groupby_month)

    groupby_day = data.groupby(['day'])['day'].count()
    print("Day group: \n", groupby_day)

    groupby_weekday = data.groupby(['weekday'])['weekday'].count()
    print("Weekday group: \n", groupby_weekday)

    groupby_hour = data.groupby(['hour'])['hour'].count()
    print("Hour group: \n", groupby_hour)


    groupby_gender = data.groupby(['gender'])['gender'].count()
    print("gender group: \n", groupby_gender)

    groupby_usertype = data.groupby(['usertype'])['usertype'].count()
    print("usertype group: \n", groupby_usertype)

    groupby_multi = data.groupby(['hour','gender'])['hour'].count()
    print("Multi group: \n", groupby_multi)
