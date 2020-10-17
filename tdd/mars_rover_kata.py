"""
REF: https://kata-log.rocks/mars-rover-kata

Your Task
You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

Requirements
You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
The rover receives a character array of commands.
Implement commands that move the rover forward/backward (f,b).
Implement commands that turn the rover left/right (l,r).
Implement wrapping at edges. But be careful, planets are spheres. Connect the x edge to the other x edge, so (1,1) for x-1 to (5,1), but connect vertical edges towards themselves in inverted coordinates, so (1,1) for y-1 connects to (5,1).
Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.
Rules
Hardcore TDD. No Excuses!
Change roles (driver, navigator) after each TDD cycle.
No red phases while refactoring.
Be careful about edge cases and exceptions. We can not afford to lose a mars rover, just because the developers overlooked a null pointer.
"""
import dataclasses
import enum
from abc import ABCMeta, abstractmethod

import pytest


class Orientation(enum.Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    WEST = "WEST"
    SOUTH = "SOUTH"


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)


class Rover:
    INVALID_COMMAND = "Invalid command. Valid commands are f,b,r,l"

    def __init__(self, position: Point, orientation: Orientation):
        self.position = position
        self.orientation = orientation

    def process(self, commands: str):
        for command in commands:
            self._process_command(command)

    def _process_command(self, command):
        command_processor = CommandProcessor.for_rover(self)
        if command == "f":
            command_processor.forward()
        elif command == "b":
            command_processor.backward()
        elif command == "r":
            command_processor.right()
        elif command == "l":
            command_processor.left()
        else:
            raise ValueError(Rover.INVALID_COMMAND)

    def move_north(self):
        self.position = self.position + Point(0, 1)

    def move_south(self):
        self.position = self.position - Point(0, 1)

    def move_east(self):
        self.position = self.position + Point(1, 0)

    def move_west(self):
        self.position = self.position - Point(1, 0)

    def turn_north(self):
        self.orientation = Orientation.NORTH

    def turn_south(self):
        self.orientation = Orientation.SOUTH

    def turn_east(self):
        self.orientation = Orientation.EAST

    def turn_west(self):
        self.orientation = Orientation.WEST

    def is_at(self, position: Point, orientation: Orientation):
        return self.position == position and self.orientation == orientation

    def is_oriented(self, orientation: Orientation):
        return self.orientation == orientation


class CommandProcessor(metaclass=ABCMeta):
    @classmethod
    def for_rover(cls, rover: Rover):
        subclass = next(subclass for subclass in cls.__subclasses__() if subclass.can_handle(rover))
        return subclass(rover)

    @classmethod
    @abstractmethod
    def can_handle(cls, rover: Rover) -> bool:
        pass

    def __init__(self, rover: Rover):
        self.rover = rover

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def backward(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def left(self):
        pass


class RoverAtNorth(CommandProcessor):
    @classmethod
    def can_handle(cls, rover: Rover) -> bool:
        return rover.is_oriented(Orientation.NORTH)

    def forward(self):
        self.rover.move_north()

    def backward(self):
        self.rover.move_south()

    def right(self):
        self.rover.turn_east()

    def left(self):
        self.rover.turn_west()


class RoverAtEast(CommandProcessor):
    @classmethod
    def can_handle(cls, rover: Rover) -> bool:
        return rover.is_oriented(Orientation.EAST)

    def forward(self):
        self.rover.move_east()

    def backward(self):
        self.rover.move_west()

    def right(self):
        self.rover.turn_south()

    def left(self):
        self.rover.turn_north()


class RoverAtWest(CommandProcessor):
    @classmethod
    def can_handle(cls, rover: Rover) -> bool:
        return rover.is_oriented(Orientation.WEST)

    def forward(self):
        self.rover.move_west()

    def backward(self):
        self.rover.move_east()

    def right(self):
        self.rover.turn_north()

    def left(self):
        self.rover.turn_south()


class RoverAtSouth(CommandProcessor):
    @classmethod
    def can_handle(cls, rover: Rover) -> bool:
        return rover.is_oriented(Orientation.SOUTH)

    def forward(self):
        self.rover.move_south()

    def backward(self):
        self.rover.move_north()

    def right(self):
        self.rover.turn_west()

    def left(self):
        self.rover.turn_east()


def test1():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("")
    assert rover.is_at(Point(0, 0), Orientation.NORTH)


def test2():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("f")
    assert not rover.is_at(Point(0, 0), Orientation.NORTH)
    assert rover.is_at(Point(0, 1), Orientation.NORTH)


def test3():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("ff")
    assert not rover.is_at(Point(0, 0), Orientation.NORTH)
    assert rover.is_at(Point(0, 2), Orientation.NORTH)


def test4():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("b")
    assert not rover.is_at(Point(0, 0), Orientation.NORTH)
    assert rover.is_at(Point(0, -1), Orientation.NORTH)


def test5():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("r")
    assert not rover.is_at(Point(0, 0), Orientation.NORTH)
    assert rover.is_at(Point(0, 0), Orientation.EAST)


def test6():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("l")
    assert not rover.is_at(Point(0, 0), Orientation.NORTH)
    assert rover.is_at(Point(0, 0), Orientation.WEST)


def test7():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("rr")
    assert not rover.is_at(Point(0, 0), Orientation.NORTH)
    assert rover.is_at(Point(0, 0), Orientation.SOUTH)


def test8():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("rl")
    assert rover.is_at(Point(0, 0), Orientation.NORTH)


def test9():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("rf")
    assert rover.is_at(Point(1, 0), Orientation.EAST)


def test10():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    rover.process("rb")
    assert rover.is_at(Point(-1, 0), Orientation.EAST)


def test11():
    rover = Rover(Point(0, 0), Orientation.NORTH)
    with pytest.raises(ValueError, match=Rover.INVALID_COMMAND):
        rover.process("a")
    assert rover.is_at(Point(0, 0), Orientation.NORTH)
