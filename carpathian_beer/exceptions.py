class CarpathianBeerException(Exception):
    ...


class InvalidIdException(CarpathianBeerException):
    # exception class for invalid id
    ...


class ArgumentsException(CarpathianBeerException):
    # exception class for invalid arguments
    ...
