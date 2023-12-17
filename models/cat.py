from dataclasses import dataclass


@dataclass(kw_only=True)
class Cat:
    id: str = ""
    name: str = ""
    age: int = None
    color: str = ""
