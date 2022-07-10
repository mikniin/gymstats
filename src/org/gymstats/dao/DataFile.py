import os

from abc import abstractmethod
from pathlib import Path


class DataFile:
    """Base class for resolving a file path into data dir for a given file name"""
    def __init__(self, file_name: str) -> None:
        """Constructor

        Parameters:
            file_name: str - The local file name we want to open from data dir
        """
        self._basedir = os.path.dirname(__file__)
        self._file_name = file_name
        self._file_path = None
        self._resolve_path()

    def _resolve_path(self) -> None:
        """Resolve a full path for given data file"""
        if self._file_name is not None:
            self._file_path = Path(self._basedir, '../data', self._file_name)

    @property
    def basedir(self) -> str:
        """Getter for basedir"""
        return self._basedir

    @property
    def file_name(self) -> str:
        """Getter for filename in use"""
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str) -> None:
        """Setter for filename to use

        Constructs full path immediately after this has been set
        """
        self._resolve_path()
    
    @property
    def file_path(self) -> Path:
        """Returns the currently resolved file path"""
        return self._file_path

    @abstractmethod
    def read_data(self) -> dict:
        """Read data from the datafile"""
        raise NotImplementedError('read_data() has not been implemented')
