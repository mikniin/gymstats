import pandas


class GymUsageStats:
    """Domain object for GymUsageStats

    Container for the data derived from the GymStatisticsFile
    """
    def __init__(self, dataframe: pandas.DataFrame) -> None:
        self._dataframe = dataframe.copy(deep=True)
        self._dataframe['time'] = pandas.to_datetime(self._dataframe['time'], utc=True)
        self._dataframe = self._dataframe.set_index('time')
        self._device_colums = [column for column in self._dataframe.columns if column != 'time']
        self._dataframe['Total'] = self.summarize_columns(self._device_colums)
        self._dataframe['Year'] = self._dataframe.index.year
        self._dataframe['Month'] = self._dataframe.index.month
        self._dataframe['Day'] = self._dataframe.index.day
        self._dataframe['Hour'] = self._dataframe.index.time
        self._dataframe['Timezone'] = 'UTC'
        self._dataframe['Weekday'] = self._dataframe.index.weekday

    def print_hour(self, index):
        hours = []
        for i in range(index.hour.size):
            hours.append('{0}:{1}'.format(index.hour.loc[i], index.minute.loc[i]))
        return hours

    def summarize_columns(self, columns: list) -> int:
        """Calculate sum of given column values"""
        value = 0
        for column in columns:
            value += self._dataframe[column]
        return value

    @property
    def dataframe(self) -> pandas.DataFrame:
        """Get the pandas dataframe"""
        return self._dataframe

    @property
    def device_columns(self) -> list:
        """Get all the available device columns (except time)"""
        return self._device_colums
