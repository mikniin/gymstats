import logging

from org.gymstats.dao.DeviceMappingFile import DeviceMappingFile
from org.gymstats.dao.GymStatisticsFile import GymStatisticsFile
from org.gymstats.services.HourlyStats import HourlyStats


class GymStats:
    """Gym stats class

    Reads in the data and runs all the exercises
    """
    def __init__(self) -> None:
        self._device_mappings = DeviceMappingFile('device-mapping.csv')
        self._gym_statistics = GymStatisticsFile('hietaniemi-gym-data.csv')

    def _read_data(self):
        """Read in the required data for the exercises

        Read all the required files into the memory (bad idea, should make them streamable)"""
        # We *could* hardcode the file names inside the respective data files as well
        logging.debug('Reading all data')
        try:
            self._device_mappings.read_data()
            self._gym_statistics.read_data()
        except:
            logging.error('Failed to read data from files')
            raise

    def _aggregate_hourly_stats(self):
        """Run hourly stats out of the gym data

        Run aggregations using Hourly stats class and present 10 first rows of the aggregation
        with device beacons replaced by device names
        """
        stats_service = HourlyStats(self._device_mappings.mappings, self._gym_statistics.usage_stats)
        stats_service.aggregate()
        stats_service.present_data()

    def _present_data(self, title: str, data: dict):
        for key, value in data:
            print('')

    def run(self):
        """Run all the exercises"""
        self._read_data()

        self._aggregate_hourly_stats()
