class PhoneNumber:
    def __init__(self,ContactId,PhoneType,PhoneNumber):
        self.ContactId = ContactId
        self.PhoneType = PhoneType
        self.PhoneNumber = PhoneNumber
    def GetPhoneNumbers(self):
        phonenumbers =""        
        if hasattr(self,'PhoneNumbers'):
            phs = getattr(self,'PhoneNumbers')
            for ph in list(phs):
                if hasattr(phs[0],'PhoneType'):
                 phonenumbers = phonenumbers + ph.ContactId + ',' + ph.PhoneType  + ','+str(ph.PhoneNumber)             
        return phonenumbers;
