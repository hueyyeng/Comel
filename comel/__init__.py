__version__ = "0.3.0"


class ComelException(Exception):
    """Base Comel exception."""


class InvalidInstanceException(ComelException):
    """Error when passed in invalid instance."""
