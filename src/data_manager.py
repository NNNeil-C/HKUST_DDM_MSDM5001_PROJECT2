# -*- coding: utf-8 -*-
# @Time    : 3/12/2021 10:30 pm
# @Author  : ZIFENG NEIL CHEN
# @FileName: data_manager.py
# @Software: PyCharm
# @Github    ：https://github.com/NNNeil-C/
import pandas as pd
from data import Data


class DataManager:
    def __init__(self, file_path):
        self.data = []
        self.column_names = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D', 'TripLength',
                    'TripEnd', 'TripInformation']
        traffic_df = pd.read_csv(file_path, names=self.column_names)
        traffic_data = Data(traffic_df)
        self.data.append(traffic_data)

    def sort(self, column_index, ascending=True):
        return self.data[0].sort(column_index, ascending)

    def search(self, start_time, end_time, vehicle_type):
        return self.data[0].search(start_time, end_time, vehicle_type)