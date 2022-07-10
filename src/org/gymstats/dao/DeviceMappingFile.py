import csv
from numbers import Number

from org.gymstats.dao.DataFile import DataFile


class DeviceMappingFile(DataFile):
    """Reads in device mappings from a csv file into memory

    CSV format we expect is:
    beacon,device name,device number
    TODO: Possibly return a Domain object, that represents our data, possibly the option to
          just simply iterate through file back and forth
    """
    def __init__(self, file_name: str) -> None:
        """Constructor, give file name as an optional argument"""
        DataFile.__init__(self, file_name)
        # beacon: name
        self._mappings = {}

    @property
    def mappings(self) -> dict:
        """Get the mappings in memory"""
        return self._mappings

    def read_data(self) -> dict:
        """Read the contents of the device mappings file

        Read the data from device mappings file, expecting the contents to be small
        and file to be set

        FIXME: Domain object for each of the rows?
        """
        if self.file_path is None:
            raise ValueError('Please give a valid file path')

        with open(self.file_path, newline='') as device_file:
            reader = csv.DictReader(device_file)
            for row in reader:
                self._mappings[row['beacon']] = row['device name']

        return self._mappings
