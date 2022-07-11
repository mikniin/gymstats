import logging
import unittest

from org.gymstats.dao.DeviceMappingFile import DeviceMappingFile
from org.gymstats.dao.GymStatisticsFile import GymStatisticsFile
from org.gymstats.dao.WeatherFile import WeatherFile
from org.gymstats.domain.GymUsageStats import GymUsageStats
from org.gymstats.services.HourlyStats import HourlyStats
from org.gymstats.services.PopularityStats import PopularityStats
from org.gymstats.services.WeatherImpact import WeatherImpact
from org.gymstats.tests.TestDataIntegrity import TestDataIntegrity


class GymStats:
    """Gym stats class

    Reads in the data and runs all the exercises
    """
    def __init__(self) -> None:
        self._device_mappings = DeviceMappingFile('device-mapping.csv')
        self._gym_statistics = GymStatisticsFile('hietaniemi-gym-data.csv')
        self._weather_stats = WeatherFile('kaisaniemi-weather-data.csv')

    def read_data(self):
        """Read in the required data for the exercises

        Read all the required files into the memory (bad idea, should make them streamable)"""
        # We *could* hardcode the file names inside the respective data files as well
        logging.debug('Reading all data')
        try:
            self._device_mappings.read_data()
            self._gym_statistics.read_data()
            self._weather_stats.read_data()
        except:
            logging.error('Failed to read data from files')
            raise

    def aggregate_hourly_stats(self):
        """Run hourly stats out of the gym data

        Run aggregations using Hourly stats class and present 10 first rows of the aggregation
        with device beacons replaced by device names
        """
        print('=== GymStats - Running hourly aggregation exercise')
        stats_service = HourlyStats(self._device_mappings.mappings, self._gym_statistics.usage_stats)
        stats_service.aggregate()
        print('=== GymStats - Hourly aggregation exercise over')

    def run_data_integrity_tests(self):
        """Run data integrity tests

        Runs tests using an included test class
        """
        print('=== GymStats - Running data integrity test exercise')
        suite = unittest.TestSuite()
        suite.addTest(TestDataIntegrity('test_data_size'))
        suite.addTest(TestDataIntegrity('test_records_between'))
        suite.addTest(TestDataIntegrity('test_all_columns_positive'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        print('=== GymStats - Data integrity test exercise over')

    def run_popularity_analysis(self):
        """Analyse the popularity of the gym

        Determine which device was the most popular device based on used minutes (value 2 is 0-2mins though)
        Check if time of day has an impact to the popularity of the gym
        Check if gym is more popular during weekends than not
        """
        print('=== GymStats - Running popularity stats exercise')
        popularity_service = PopularityStats(self._device_mappings.mappings, self._gym_statistics.usage_stats)
        popularity_service.popular_device()
        popularity_service.popular_time()
        popularity_service.weekend_popularity()
        print('=== GymStats - Popularity stats exercise over')

    def run_enrich_data(self):
        """Enrich the gym data with certain elements

        Create a domain object out of the gym statistics and enrich it certain data
        """
        print('=== Enrich data exercise')
        print(GymUsageStats(self._gym_statistics.usage_stats).dataframe)
        print('=== Enrich data exercise over')

    def run_weather_impact(self):
        """Analyze weather impact on use of gym

        Does the temperature impact the gym popularity
        Does precipitation impact the gym popularity
        """
        print('=== GymStats - Analyzing weather impact')
        weather_impact = WeatherImpact(
            self._device_mappings.mappings,
            self._gym_statistics.usage_stats,
            self._weather_stats.weather_data
        )
        weather_impact.temperature_impact()
        weather_impact.precipitation_impact()
        print('=== GymStats - Weather impact analyzis complete')

    def run(self):
        """Run all the exercises"""
        self.read_data()

        self.aggregate_hourly_stats()
        self.run_data_integrity_tests()
        self.run_popularity_analysis()
        self.run_enrich_data()
        self.run_weather_impact()
