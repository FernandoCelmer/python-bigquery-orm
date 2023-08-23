class ExceptionInvalidDataClass(Exception):

    def __init__(self):
        message = " Invalid DataClass for the context of this package. "
        super(ExceptionInvalidDataClass, self).__init__(message)
