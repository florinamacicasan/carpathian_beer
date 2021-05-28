from abc import ABC, abstractmethod


class PunkAPIBaseSession(ABC):
    @abstractmethod
    def get(self):
        ...
