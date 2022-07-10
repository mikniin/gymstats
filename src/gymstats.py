#!/usr/bin/env python3
"""Gymstats main file - bootstrap the tool

Load any starting points and handle any environment and or command line configs
"""
from org.gymstats.services.GymStats import GymStats

if __name__ == '__main__':
    app = GymStats()
    app.run()
