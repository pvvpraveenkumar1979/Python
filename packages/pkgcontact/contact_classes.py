from packages.pkgcontact.Utility import *
import packages.pkgcontact.contact_globals as GlobalData
import packages.pkgcontact.contact_sequencer_actions as contactSequencerActions
import packages.pkgcontact.file_utility as FileUtility
import packages.pkgcontact.contact_exceptions as contact_exceptions

# TODO:Format each field based on length
# ID: 10 chars
# First Name 25 char
# Last Name 25 char
# Gender 6
# Relationship 25 char
# Company Name 25 char
# Contact can be general, official or personal ... but for each of these there can be different phone numbers and addresses




class Contact():
    contacts = []
    def __init__(self,fName, LastName ,Gender,CType='GC'):
        self.__FirstName = fName
        self.LastName = LastName
        self.Gender = Gender        
        self.Id = GlobalData.ContactSequencer['CURRENTVALUE']
        self.CType = CType

    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self,fname):
        if len(fname) > 25:
            raise contact_exceptions.contactFieldLengthException('ContactName')
        else:
            self.__FirstName = fname



        GlobalData.ContactSequencer['CURRENTVALUE'] += GlobalData.ContactSequencer['STEPVALUE']
        contactSequencerActions.saveSequencerData(GlobalData.ContactSequencer,GlobalData.ContactSequencerFilePath)
##        self.PhoneNumbers = []
##        self.Addresses = []
        
        
    def AddPhoneNumber(self,PhoneNumber):
        self.PhoneNumbers.append(PhoneNumber)
        
    def AddAddress(self,Address):
        self.Addresses.append(Address)

    def SetContactType(self):
        self.CType='GC'

    def SaveContactToFile(self):
        Contact.contacts.append(self)
        FileUtility.saveDataToFile(Contact.contacts,GlobalData.ContactsFilePath)
    

    def ReadContactFromFile(self):
        Records = []
        file = open(GlobalData.ContactsFilePath,'r')
        Record = file.readline()
        while Record != '':
            print(Record)
            Record = file.readline()
        file.close()
        return Records
        
        
class PersonalContact(Contact):
    def __init__(self,FirstName, LastName ,Gender,relationshipName):
        super(PersonalContact,self).__init__(FirstName, LastName ,Gender)
        self.relationshipname = relationshipName #see here the name of parameter and instance member name are different

    def SetContactType(self):
        self.CType='PC'


class OfficialContact(Contact):
    def __init__(self,FirstName, LastName ,Gender,OfficeName):
        super(OfficialContact,self).__init__(FirstName, LastName ,Gender)
        self.OfficeName = OfficeName

    def SetContactType(self):
        self.CType='OC'
