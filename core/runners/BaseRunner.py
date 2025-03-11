from typing import Any, Self


class BaseRunner:

    def setup(self): ...

    def run(self) -> Self:
        raise NotImplementedError

    def get_data(self) -> Any: ...
