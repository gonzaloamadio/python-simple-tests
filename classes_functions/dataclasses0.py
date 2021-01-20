from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    debug: bool
    tracing: bool

try:
    cfg = Config()
    print(cfg)
except Exception as err:
    print("Error trying to initialize Config() with no parameters")
    print(f"Error: {err}")


print("\n--------------------------------------------------------------\n")
# Annotation as Optional does not mean is not required

@dataclass
class Config2:
    debug: Optional[bool]
    tracing: Optional[bool]

try:
    cfg = Config2()
    print(cfg)
except Exception as err:
    print("Error trying to initialize Config2() with no parameters")
    print(f"Error: {err}")


print("\n--------------------------------------------------------------\n")
# Also annotations does not enforce type, it is just a hint

@dataclass
class Config3:
    debug: Optional[bool] = False
    tracing: Optional[bool] = None

try:
    cfg = Config3()
    print(cfg)
except Exception as err:
    print("Error trying to initialize Config3() with no parameters")
    print(f"Error: {err}")
