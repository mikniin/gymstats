import pandas

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
        self._usage_stats = None

    @property
    def usage_stats(self) -> pandas.DataFrame:
        """Get the usage stats in memory"""
        return self._usage_stats

    def read_data(self) -> pandas.DataFrame:
        """Read the contents of the gym usage stats file

        Read the data from gym usage stats file, expecting the contents to be small
        and file to be set

        TODO: Domain object for each of the rows?
        """
        if self.file_path is None:
            raise ValueError('Please give a valid file path')

        with open(self.file_path, newline='') as device_file:
            self._usage_stats = pandas.read_csv(device_file, sep=',')

        return self._usage_stats
