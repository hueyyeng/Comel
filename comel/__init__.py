__version__ = "0.2.1"


class ComelException(Exception):
    """Base Comel exception."""


class InvalidInstanceException(ComelException):
    """Error when passed in invalid instance."""
