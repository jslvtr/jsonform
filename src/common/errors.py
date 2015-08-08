__author__ = 'jslvtr'


class NoChildrenInFormError(Exception):
    def __init__(self, message):
        self.message = message


class FieldFormatError(Exception):
    def __init__(self, message):
        self.message = message
