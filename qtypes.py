from typing import Union
from datetime import datetime

class qstr(str):
    def __new__(cls, value: str) -> 'qstr':
        # Create a new instance of Qstr
        return super().__new__(cls, value)
    
    def __repr__(self) -> str:
        return f'qstr({super().__repr__()})'


class qbool(bool):
    def __new__(cls, value: Union[str, bool, int]) -> 'qbool':
        # Create a new instance of Qbool
        if isinstance(value, str):
            value = value.lower()
            if value in ["true", "True", "TRUE", "y", "yes", "Yes", "YES", "1"]:
                value = True
            if value in ["false","False", "FALSE", "n", "no", "No", "NO", "0"]:
                value = False
        return super().__new__(cls, value)
    
    def __repr__(self) -> str:
        return f'qbool({super().__repr__()})'

class qamount(float):
    def __new__(cls, value: Union[str, float]) -> 'qamount':
        return super().__new__(cls, float(value))

    def __repr__(self) -> str:
        return f'qamount({super().__repr__()})'


class qdate(datetime):
    @classmethod
    def from_string(cls, date_str: str, format: str = '%Y-%m-%d') -> 'qdate':
        return cls.strptime(date_str, format)

    def __repr__(self) -> str:
        return f'Qdate({super().__repr__()})'
    

class qid(int):
    def __new__(cls, value: Union[str, int]) -> 'Qid':
        return super().__new__(cls, int(value))

    def __repr__(self) -> str:
        return f'qid({super().__repr__()})'


class qstrlist(list):
    def __init__(self, *args: Union[str, qstr]) -> None:
        super().__init__(qstr(arg) for arg in args)

    def __repr__(self) -> str:
        return f'Qstrlist({super().__repr__()})'

    def append(self, value: str) -> None:
        super().append(qstr(value))

    def extend(self, values: list[str]) -> None:
        super().extend(qstrlist(values))
    
    def insert(self, index: int, value: str) -> None:
        super().insert(index, qstr(value))
    
    def remove(self, value: str) -> None:
        super().remove(qstr(value))
    
    def pop(self, index: int = -1) -> str:
        return qstr(super().pop(index))
    
    def index(self, value: str) -> int:
        return super().index(qstr(value))
    
    def count(self, value: str) -> int:
        return super().count(qstr(value))
    
    def clear(self) -> None:
        super().clear()
    
    def sort(self) -> None:
        super().sort()
    
    def reverse(self) -> None:
        super().reverse()
    
    def copy(self) -> 'qstrlist':
        return super().copy()

class qbase:
    def __repr__(self) -> str:
        return 'qbase()'  # Can be extended as needed


def qtype(value: str) -> str:
    if value in ["true", "True", "TRUE", "y", "yes", "Yes", "YES", "1"]:
        return qbool
    elif value in ["false","False", "FALSE", "n", "no", "No", "NO", "0"]:
        return qbool
    try:
        float(value)
        return qamount
    except ValueError:
        pass
    try:
        datetime.strptime(value, '%Y-%m-%d')
        return qdate
    except ValueError:
        pass
    try:
        int(value)
        return qid
    except ValueError:
        pass
    if value[0] == '"' and value[-1] == '"':
        return qstr
    if value[0] == '[' and value[-1] == ']':
        return qstrlist
    if value[0] == '{' and value[-1] == '}':
        return qstrlist
    
    return qbase

    
    
    elif isinstance(value, list):
        return qstrlist
    
    return qbase


