from dataclasses import dataclass


@dataclass(kw_only=True)
class Dog:
    id: str = ""
    name: str = ""
    age: int = None
    color: str = ""
