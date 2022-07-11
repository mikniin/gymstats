import pandas

from org.gymstats.dao.DataFile import DataFile


class WeatherFile(DataFile):
    """Read kaisaniemi weather stats into memory

    Reads kaisaniemi weather information from csv and returns it as pandas DataFrame
    """
    def __init__(self, file_name: str) -> None:
        DataFile.__init__(self, file_name)
        self._weather_data = None

    @property
    def weather_data(self) -> pandas.DataFrame:
        return self._weather_data

    def read_data(self) -> dict:
        """Read the data into memory with pandas"""
        with open(self.file_path) as device_file:
            self._weather_data = pandas.read_csv(device_file, sep=',', parse_dates=True)

        return self._weather_data
