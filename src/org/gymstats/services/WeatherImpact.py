from os import stat
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
        print('Weather data shape:', self._weather.shape)
        print('Gym stats usage shape:', self._stats.shape)
        print('Merged data shape', self._merged.shape)

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
        """Analyze if temperature somehow affects usage minutes

        Group and aggregate by temperature, dig out mean of temperature and highest and lowest use
        """
        temp_key = 'Temperature (degC)'
        rain_key = 'Precipitation (mm)'

        stats = self._merged.copy()
        stats = stats[['Total', temp_key, rain_key]] \
            .groupby(pandas.cut(stats[temp_key], 15, precision=0)) \
                .agg({'Total': ['sum', 'count', 'mean']})

        print('Stats; temperature by total use')
        stats = stats.sort_values(by=[('Total', 'sum')], ascending=False)
        print(stats.head(5))
        print(stats.tail(5))

        print('Stats; use by highest and lowest temperature')
        stats = stats.sort_values(by=temp_key, ascending=False)
        print(stats.head(5))
        print(stats.tail(5))

    def precipitation_impact(self):
        pass
