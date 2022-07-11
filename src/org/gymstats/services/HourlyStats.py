import pandas


class HourlyStats:
    """Aggregate all data by hourly usage"""
    def __init__(self, devices: dict, stats: pandas.DataFrame) -> None:
        """Constructor

        Parameters:
            devices: dict - The device mappings content
            stats: pandas.DataFrame - The pandas dataframe to manipulate
        """
        self._devices = devices
        self._stats = stats.copy()

    def aggregate(self) -> dict:
        """Aggregate the usage of gym devices hourly basis

        Convert stats, then group them by time with 1h interval and aggregate sums for the columns
        """
        stats = self._stats
        stats['time'] = pandas.to_datetime(stats['time'], utc=True)
        stats.set_index('time')
        stats = stats.groupby(pandas.Grouper(key='time', freq='1H')).sum()
        print('=== GymStats - Presentation of -- Exercise 1 values; hourly stats:')
        print(stats.head(10))
