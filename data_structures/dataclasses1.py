from typing import Optional
from dataclasses import dataclass, field


# Repr doc: https://docs.python.org/3/reference/datamodel.html#object.__repr__
# dataclasses: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass

# This 2 are the same. The thing with __repr_ is that we can do some more
# calculations when building the repr string
@dataclass(repr=False)
class Configuration:
    """Stores configuration"""

    server_url: str
    proxy_url: Optional[str] = None

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return (
            f"{classname}("
            f"server_url={self.server_url!r}, "
            f"proxy_url={self.proxy_url!r})"
        )


a = Configuration("test.com")
print(a)
# Configuration(server_url='test.com', proxy_url=None)

@dataclass()
class Configuration2:
    """Stores configuration"""

    server_url: str
    proxy_url: Optional[str] = None

a = Configuration2("test.com")
print(a)
#
################################################################################
#                            ORDER
################################################################################

# order: If true (the default is False), __lt__(), __le__(), __gt__(), and __ge__()
# methods will be generated. These compare the class as if it were a tuple of its
# fields, in order. Both instances in the comparison must be of the identical type.
# If order is true and eq is false, a ValueError is raised.

# If the class already defines any of __lt__(), __le__(), __gt__(), or __ge__(),
# then TypeError is raised.

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

# >>> queen_of_hearts = PlayingCard('Q', '♡')
# >>> ace_of_spades = PlayingCard('A', '♠')
# >>> ace_of_spades > queen_of_hearts
# True
