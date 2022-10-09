from dataclasses import dataclass

__author__ = "Tony Duran"
__version__ = "1.0.0"


@dataclass
class Message:
    name = str
    ip_addr = str
    port = int
    type = str
