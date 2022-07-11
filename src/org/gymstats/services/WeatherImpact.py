import pandas


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
        self._stats = stats.copy()
        self._weather = weather.copy()

    def temperature_impact(self):
        pass

    def precipitation_impact(self):
        pass
