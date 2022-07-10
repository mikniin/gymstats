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
        self._stats = pandas.DataFrame(stats)
        self._aggregated = None

    def _convert_data(self):
        """Convert, sort and define columns

        Convert our presented dataframe into something that is a bit more user
        friendly.

        Convert
        """
        # self._stats.rename(columns=self._devices, inplace=True)
        self._stats['time'] = pandas.to_datetime(self._stats['time'])
        self._stats.sort_values(by=['time'], ascending=True, inplace=True)

    def aggregate(self) -> dict:
        """Aggregate the usage of gym devices hourly basis

        Convert stats, then group them by time with 1h interval and aggregate sums for the columns
        """
        self._convert_data()
        self._aggregated = self._stats.groupby(pandas.Grouper(key='time', freq='1H')).sum()

    def present_data(self) -> None:
        print('=== GymStats - Presentation of -- Exercise 1 values; hourly stats:')
        print(self._aggregated.head(10))
