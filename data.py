import pandas as pd

class data:
    def __init__(self, dataframe):
        self.df = dataframe

    def search(self, start_time, end_time, vehicle_type):
        """
        Return a data class object satisfy the three conditions:
            1. df.start_time<start_time,
            2. df.finish_time<endtime,
            3. df.vehicle_type=vehicle_type

        Parameters
        ----------
        self: data
            data class object
        start_time: str
            the vehicle must enter highway after the start_time
        end_time: str
            the vehicle must exit highway before the end_time
        vehicle_type: int
            integer indicating the type of vehicle

        Returns
        -------
        Data: data
            Data class containing the filtered data
        """
        filtered_df = self.df[(self.df['DerectionTime_O'] >= start_time) & (self.df['DerectionTime_D'] <= end_time) & (
                    self.df['VehicleType'] == vehicle_type)].copy()
        return data(filtered_df)

    def show_n(self, n_row):
        """
        Sample n rows from the current dataframe

        Parameters
        ----------
        self: data
            data class object
        n_row: int
            number of row to sample from the dataframe

        Returns
        -------
        Data: data
            Data class containing the sampled data
        """
        sampled_df = self.df.sample(n_row)
        return data(sampled_df)

    def sort(self, entry_number, ascending=True):
        """
        Sort the data frame by column number and by selected order

        Parameters
        ----------
        self: data
            data class object
        ascending: bool
            if True sort in asending order,else sort in descending order
        entry_number: int
            sort the data frame according to the column number
        Returns
        -------
        data
            data class containing the sorted data
        """
        column_name = self.df.columns[entry_number]
        sorted_df = self.df.sort_values(column_name, axis=0, ascending=ascending).copy()
        return data(sorted_df)

    def get_count(self):
        """
        Get the number of observations in data.df

        Parameters
        ----------
        self: data
            data class object

        Returns
        -------
        n_row: int
            number of rows in data.df
        """
        n_row = self.df.shape[0]
        return n_row

    def get_mean_trip_length(self):
        """
        Get the mean trip_length in data.df

        Parameters
        ----------
        self: data
            data class object

        Returns
        -------
        mean_trip_length: int
            mean trip length in km
        """
        mean_trip_length = round(self.df['TripLength'].mean(), 2)
        return mean_trip_length


colnames = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D', 'TripLength','TripEnd', 'TripInformation']
traffic_df = pd.read_csv("TDCS_M06A_20190830_080000.csv",names=colnames)
traffic_data = data(traffic_df)
# start_time = str('2019-08-30 08:00:00')
# end_time = str('2019-08-30 15:08:02')
# vehicle_type = 31

import interface_controller as ic

start_time, end_time, vehicle_type=ic.get_content_search()
n_row,ascending=ic.get_content_sort()
filtered_data = traffic_data.search(start_time, end_time, vehicle_type)
sorted_data = filtered_data.sort(1, ascending)
sample_data = sorted_data.show_n(n_row)
sample_data.get_count()
sample_data.get_mean_trip_length()


