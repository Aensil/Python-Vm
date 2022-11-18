a: int = 5
b: str = "Hello"
c: bool = True

from typing import Dict, List, Tuple

p: List[int] = [1, 2, 3, 4, 5]    
u: Dict[str, int] = {
    'one':1,
    'two':2,
    'three':3
    }
Countries: List[Dict[str, str]] = [
    {
        'name': 'Arg',
        'pib' : '10',
    },
    {
        'name': 'Mex',
        'pib' : '15',
    }
]

n: Tuple[int, float, int]= (1,1.0,2)
CoordinatesType = List[Dict[str, Tuple[int, int]]]
Coordinates: CoordinatesType = [
    {
        'Coord1':(1,2),
        'Coord2':(5,5)
    },
    {
        'Coord1':(2,1),
        'Coord2':(5,6)   
    },
]


def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


def run():
    print(is_palindrome("ana"))


if __name__ == '__main__':
    run()
