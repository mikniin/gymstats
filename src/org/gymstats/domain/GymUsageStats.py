from sqlite3 import DatabaseError
import pandas


class GymUsageStats:
    """Domain object for GymUsageStats

    Container for the data derived from the GymStatisticsFile
    """
    def __init__(self, dataframe: pandas.DataFrame) -> None:
        self._dataframe = dataframe.copy()
        self._dataframe['time'] = pandas.to_datetime(self._dataframe['time'])
        self._dataframe = self._dataframe.set_index('time')
        self._device_colums = [column for column in self._dataframe.columns if column != 'time']
        self._dataframe['total'] = self.summarize_columns(self._device_colums)
        self._dataframe['hour'] = self._dataframe.index.hour
        self._dataframe['weekday'] = self._dataframe.index.weekday

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
