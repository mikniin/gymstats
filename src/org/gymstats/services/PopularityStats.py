import pandas


class PopularityStats:
    """Inspect the popularity of the gym"""
    def __init__(self, devices: dict, stats: pandas.DataFrame) -> None:
        """Constructor, take in the device mappings and gym stats data"""
        self._devices = devices
        self._stats = stats.copy()

    def summarize_columns(self, dataframe: pandas.DataFrame, columns: list) -> int:
        """Calculate sum of given column values"""
        value = 0
        for column in columns:
            value += dataframe[column]
        return value

    def popular_device(self):
        """Determine which device is most used"""
        stats = self._stats.rename(columns=self._devices)
        columns = [column for column in stats.columns if column != 'time']
        usage = stats[columns].agg('sum')
        name = usage.idxmax()
        print(usage)
        print('Most popular device seems to be {name} with {highest} minutes of use'.format(
            name=name, highest=usage[name]))

    def popular_time(self):
        """Dig out the most popular time of day (by hour) of the gym

        Group and summarize all devices together by the hour of the day, we'd have 24 rows if
        data expands over whole day
        """
        stats = self._stats.copy()

        columns = [column for column in stats.columns if column != 'time']
        stats['time'] = pandas.to_datetime(stats['time'], utc=True)
        stats = stats.set_index('time')
        stats['hour'] = stats.index.hour
        stats['total'] = self.summarize_columns(stats, columns)
        stats = stats.groupby('hour').agg('sum')
        print(stats)
        print('Most popular hour of the day seems to be {}'.format(stats['total'].idxmax()))

    def weekend_popularity(self):
        """Calculate the most popular weekday

        Instead of adding hour to data, add a weekday as a string and present the most popular
        day
        """
        stats = self._stats.copy()

        columns = [column for column in stats.columns if column != 'time']
        stats['time'] = pandas.to_datetime(stats['time'], utc=True)
        stats = stats.set_index('time')
        stats['weekday'] = stats.index.weekday
        stats['total'] = self.summarize_columns(stats, columns)
        stats = stats.groupby('weekday').agg('sum')
        print(stats)
        print('Most popular weekday seems to be {}'.format(stats['total'].idxmax()))
