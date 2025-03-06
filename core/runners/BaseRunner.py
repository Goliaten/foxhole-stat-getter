from typing import Any, Self


class BaseRunner:

    def setup(self): ...

    def run(self) -> Self:
        return self

    def get_data(self) -> Any: ...
