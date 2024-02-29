from typing import Callable


class CliCommand:
    def __init__(self, name: str, description: str, callback: Callable[[], None]):
        self.name = name
        self.description = description
        self.callback = callback
