class contactException(Exception):
    def __init__(self,msg):
        self.message = msg

class contactFieldLengthException(contactException):
    def __init__(self,fieldName):
        self.message = '{0} has invalid length'.format(fieldName)

