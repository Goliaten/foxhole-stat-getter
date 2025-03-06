class StatGetterException(Exception):
    """Base class for exceptions in the stat getter."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
