import json
import os
# Custom modules below
from packages.pkgcontact.Utility import *
from packages.pkgcontact.contact_classes import *
import packages.pkgcontact.contact_globals as GlobalData

#end Custom Modules

FirstName =""
LastName =""
Gender =""
Contacts = []

def CreateGeneralContact():
     try:          
          print('in Create General Contact',GlobalData.ContactSequencer)
          print('Please provide below details:')
          print('-----------------------------')
          print('First Name:')
          FirstName = input()
          print('Last Name:')
          LastName = input()
          print('Gender:')
          Gender = input()
          NewContact = Contact(FirstName,LastName,Gender,'GC')     
          Contacts.append(NewContact)
          return NewContact
     except Exception as exp:
          print(exp)

def CreatePersonalContact():
     print('Please provide below details:')
     print('-----------------------------')
     print('First Name:')
     FirstName = input()
     print('Last Name:')
     LastName = input()
     print('Gender:')
     Gender = input()
     print('Relationship:')
     Relationship = input()
     NewContact = PersonalContact(FirstName,LastName,Gender,Relationship,'PC')
     Contacts.append(NewContact)
     return NewContact

def CreateOfficialContact():
     print('Please provide below details:')
     print('-----------------------------')
     print('First Name:')
     FirstName = input()
     print('Last Name:')
     LastName = input()
     print('Gender:')
     Gender = input()
     print('Office Name:')
     OfficeName = input()
     NewContact = OfficialContact(FirstName,LastName,Gender,OfficeName,'OC')
     Contacts.append(NewContact)
     return NewContact

def AddPhoneNumberToContact(Contact,PhoneNumberDetails):
     Contact.AddPhoneNumber(PhoneNumberDetails)
     return

def CreateContact():
   os.system('cls')
   print('What contact do you want to create ?')
   print('\n 1. General Contact')
   print('\n 2. Personal Contact')
   print('\n 3. Official Contact')
   NewContact = None
   try:
        contactType = int(input())        
        if contactType ==1:
             print('Creating General Contact....')
             NewContact =CreateGeneralContact()
        elif contactType == 2:
            print('Creating Personal Contact....')
            NewContact = CreatePersonalContact()
        elif contactType== 3:
            print('Creating Official Contact')
            NewContact= CreateOfficialContact()
        else:
            print('Your choice is not available. Quitting app....')
        
   except Exception as ex:           
        print('Exception details',ex)
        print('Your choice is not valid quitting now')
   else:
        NewContact.SaveContactToFile()
        print('Contact Created Successfully')        
        

def ReadContacts():
   os.system('cls')
   print('Which contacts you want to read ?')
   print('\n 1. General Contact')
   print('\n 2. Personal Contact')
   print('\n 3. Official Contact')
   print('\n 4. All Contacts')
##   print(GlobalData.ContactsFilePath)  
   ReadContacts = int(input())
   if ReadContacts  == 4:
        print('\n Reading contacts...')
        ReadAllContactsFromFile()
        
   else:
        print('Action still under development')


def ReadAllContactsFromFile():
   Records = []   
   try:        
        file = open(GlobalData.ContactsFilePath,'r')
        line = file.readline()
        print(line)
        while line != '':
            dictobject = json.loads(line)
            Records.append(dictobject)
            line = file.readline()
   except IOError as exp:
        print('Error reading file',exp)
   except Exception as exp:
        print('Error reading file',exp)
   finally:  
        file.close()
   return Records

