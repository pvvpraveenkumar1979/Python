class Address:
    def __init__(self,ContactId,AddressType,AddressDetails):
        self.ContactId = ContactId
        self.AddressType = AddressType
        self.AddressDetails = AddressDetails   
 
    def GetAddresses(self):
         addresses =""
         if hasattr(self,'Addresses'):
            adds = getattr(self,'Addresses')
            for add in list(adds):
                if hasattr(phs[0],'PhoneType'):
                 addresses = addresses + add.ContactId + ',' + add.AddressType  + ','+str(add.AddressDetails)
             
         return addresses;
