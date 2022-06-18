from abc import ABC, abstractmethod

class UriInterface(ABC):
    @abstractmethod
    def get_postgres_uri():
        pass