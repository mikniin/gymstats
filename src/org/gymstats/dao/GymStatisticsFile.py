import csv

from org.gymstats.dao.DataFile import DataFile


class GymStatisticsFile(DataFile):
    """Read the gym statistics into memory

    Read data from the gym statistics csv
    TODO: Avoid reading whole file at once
    """
    def __init__(self, file_name: str) -> None:
        """Init and """
        DataFile.__init__(self, file_name)
        # time: {beacon1: count, beacon2: count, beacon3: count}
        self._usage_stats = {}

    @property
    def usage_stats(self) -> dict:
        """Get the usage stats in memory"""
        return self._usage_stats

    def read_data(self) -> dict:
        """Read the contents of the gym usage stats file

        Read the data from gym usage stats file, expecting the contents to be small
        and file to be set

        TODO: Domain object for each of the rows?
        """
        if self.file_path is None:
            raise ValueError('Please give a valid file path')

        with open(self.file_path, newline='') as device_file:
            reader = csv.DictReader(device_file)
            for row in reader:
                self._usage_stats[row['time']] = {key:row[key] for key in row if key != 'time'}

        return self._usage_stats
