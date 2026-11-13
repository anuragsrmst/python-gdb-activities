from abc import ABC, abstractmethod
import sqlite3

class ConnectionProvider(ABC):
    @abstractmethod
    def get_connection(self) -> sqlite3.Connection:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
