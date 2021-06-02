class CarpathianBeerException(Exception):
    ...


class InvalidIdException(CarpathianBeerException):
    # exception class for invalid id
    # TODO: refactor (
    def __init__(self, message=None):
        if not message:
            # Set some default useful error message
            message = "Invalid id!"
        super().__init__(message)
