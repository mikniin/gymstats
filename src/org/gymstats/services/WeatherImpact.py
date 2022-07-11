import pandas

from org.gymstats.domain.GymUsageStats import GymUsageStats


class WeatherImpact:
    """Analyzes the weather impact on gym popularity

    Does the temperature impact the gym popularity
    Does precipitation impact the gym popularity
    """
    def __init__(self, devices: dict, stats: pandas.DataFrame, weather: pandas.DataFrame) -> None:
        """Contructor

        Parameters:
            devices: dict - The device mappings from beacon to name
            stats: pandas.DataFrame - Gym usage statistics
            weather: pandas.DataFrame - Weather stats in Kaisaniemi
        """
        self._devices = devices
        self._weather = weather.copy()
        self._stats = stats.copy()
        self.format_weather()
        self.group_stats_hourly()
        # merge our data, inner method... so only common rows are present
        self._merged = pandas.merge(self._stats, self._weather, on=['Year', 'Month', 'Day', 'Hour', 'Timezone'])

    def format_weather(self):
        """Format weather hours to match stats hours"""
        self._weather['time'] = pandas.to_datetime(self._weather['Hour'], utc=True)
        self._weather = self._weather.set_index('time')
        self._weather['Hour'] = self._weather.index.time
        self._weather = self._weather.reset_index()
        self._weather = self._weather.drop(['time'], axis='columns')

    def group_stats_hourly(self):
        """Group by hourly use and enrich the gym stats"""
        self._stats['time'] = pandas.to_datetime(self._stats['time'], utc=True)
        self._stats = self._stats.groupby(pandas.Grouper(key='time', freq='1H')).sum()
        self._stats = self._stats.reset_index()
        # Enrich the data... *after* we've grouped data hourly
        self._usage = GymUsageStats(self._stats)
        self._stats = self._usage.dataframe.copy()
        self._stats = self._stats.reset_index()

    def temperature_impact(self):
        print(self._merged)
        pass

    def precipitation_impact(self):
        pass
