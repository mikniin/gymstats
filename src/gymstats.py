#!/usr/bin/env python3
"""Gymstats main file - bootstrap the tool

Load any starting points and handle any environment and or command line configs
"""
from org.gymstats.dao.DeviceMappingFile import DeviceMappingFile
from org.gymstats.dao.GymStatisticsFile import GymStatisticsFile


def main():
    # We *could* hardcode the file names inside the respective data files as well
    devices = DeviceMappingFile('device-mapping.csv')
    gym_statistics = GymStatisticsFile('hietaniemi-gym-data.csv')
    print(devices.read_data())
    print(gym_statistics.read_data())

if __name__ == '__main__':
    main()
