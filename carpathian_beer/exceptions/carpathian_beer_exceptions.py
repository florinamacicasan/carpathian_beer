import logging


class CarpathianBeerException(Exception):
    ...


class InvalidIdException(CarpathianBeerException):
    # exception class for invalid id
    def __init__(self, message: str) -> None:
        super().__init__(message)
        logging.info("InvalidIdException object has been initialized")
