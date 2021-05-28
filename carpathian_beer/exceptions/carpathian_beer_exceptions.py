class CarpathianBeerException(Exception):
    ...


class InvalidIdException(CarpathianBeerException):
    # exception class for invalid id
    def __init__(self, message=None):
        if not message:
            # Set some default useful error message
            message = "Invalid id!"
        super(CarpathianBeerException, self).__init__(message)


class InvalidMonthOrYearException(CarpathianBeerException):
    # exception class for month or year
    def __init__(self, message=None):
        if not message:
            # Set some default useful error message
            message = "Invalid month or year!"
        super(CarpathianBeerException, self).__init__(message)
