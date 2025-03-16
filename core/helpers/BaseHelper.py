from typing import Optional, Self


class BaseHelper:
    _instance: Optional[Self] = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(BaseHelper, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    @classmethod
    def get(cls) -> Self:
        """Get the singleton instance of the Logger."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def initialize(self) -> None:
        pass
