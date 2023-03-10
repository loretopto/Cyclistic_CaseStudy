# %% Import relevant modules

# Third party modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# import tensorflow as tf
# tf.get_logger().setLevel('INFO')
import seaborn as sns
import argparse
import logging
import pprint
from datetime import datetime
from colorlog import ColoredFormatter

# import internal modules
import config
import preprocessing
import analysis

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Cyclistic Case Study")
    parser.add_argument('--analysis', dest='analysis', action='store_true')
    parser.set_defaults(analysis=False)
    args = parser.parse_args()

    pp = pprint.PrettyPrinter()
    LOG_LEVEL = logging.DEBUG #if args.debug else logging.CRITICAL
    logging.root.setLevel(LOG_LEVEL)
    formatter = ColoredFormatter(config.LOGFORMAT)
    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)
    logger = logging.getLogger('Cyclistic Log')
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(stream)

    # dataQ1=pd.read_csv("2019/Divvy_Trips_2019_Q1.csv", thousands=',')
    # dataQ2=pd.read_csv("2019/Divvy_Trips_2019_Q2.csv", thousands=',')
    # dataQ3=pd.read_csv("2019/Divvy_Trips_2019_Q3.csv", thousands=',')
    # dataQ4=pd.read_csv("2019/Divvy_Trips_2019_Q4.csv", thousands=',')
    # combined_data = preprocessing.quarter_append(dataQ1,dataQ2,dataQ3,dataQ4)
    # data = preprocessing.data_cleaning(combined_data)
    # preprocessing.check_if_uniqueID(data)
    # data.to_csv('processed_data.csv', index=False)

    data = pd.read_csv("processed_data.csv")
    # preprocessing.data_check(data)


    # analysis.correlmat(data)
    analysis.groupingby(data)
