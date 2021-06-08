from abc import ABC, abstractmethod


class BaseSession(ABC):
    @abstractmethod
    def get(self):
        ...
