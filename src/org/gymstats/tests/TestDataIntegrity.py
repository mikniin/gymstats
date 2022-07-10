import unittest
import csv

import pandas

from org.gymstats.dao.DataFile import DataFile
from org.gymstats.dao.GymStatisticsFile import GymStatisticsFile


class TestDataIntegrity(unittest.TestCase):
    """Data integrity test cases"""
    def setUp(self) -> None:
        """Setup the test case"""
        self.datafile = GymStatisticsFile('hietaniemi-gym-data.csv')
        self.datafile.read_data()

    """Test cases to test data integrity"""
    def test_data_size(self):
        """Test that gym data has more than 50000 lines"""
        datafile = DataFile('hietaniemi-gym-data.csv')
        count = 0
        with open(datafile.file_path) as gymdata:
            reader = csv.DictReader(gymdata)
            for _ in reader:
                count += 1
        self.assertTrue(count > 50000)

    def test_records_between(self):
        """Test that there are records between 2020-04-24 and 2021-05-11"""
        stats = pandas.DataFrame(self.datafile.usage_stats)
        stats['time'] = pandas.to_datetime(stats['time'])
        stats = stats[(stats['time'] >= '2020-04-24') & (stats['time'] <= '2021-05-11')]
        self.assertGreater(len(stats.values), 0)

    def test_all_columns_positive(self):
        """Test that all numerical columns are positive"""
        stats = pandas.DataFrame(self.datafile.usage_stats)
        for column in stats:
            if column == 'time':
                continue
            for value in stats[column]:
                self.assertGreater(value, -1)

if __name__ == '__main__':
    unittest.main()
