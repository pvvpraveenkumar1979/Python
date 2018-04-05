import packages.pkgcontact.contact_sequencer_actions as SequencerAction
import time

def SaveDataLog(data):
    stringDataFormatted = '\n' + data+' @:{0}'.format(time()) +'\n'   
    fpDataLog.write(stringDataFormatted)

def SaveErrorLog(error):
    stringDataFormatted = '\n-------------------------------------'
    stringDataFormatted += '\n Error:'+' @:{0} \n'.format(time())+error
    stringDataFormatted += '\n-------------------------------------'    
    fpErrLog.write(stringDataFormatted)


def LoadGlobalData():    
   
    global ContactSequencer
    global PhoneSequencer
    global AddressSequencer
    global FormFields

    global DataFolderPath
    global MasterDataFolderPath
    global ContactsFilePath
    global PhoneNumberFilePath
    global AddressesFilePath
    global ContactSequencerFilePath
    global PhoneNumberSequencerFilePath
    global AddressSequencerFilePath

    global LogDataPath
    global LogErrorPath

    global fpDataLog
    global fpErrLog

    DataFolderPath = 'data'
    MasterDataFolderPath='masterdata'

    ContactsFilePath='.\{0}\contacts.data.txt'.format(DataFolderPath)
    PhoneNumberFilePath='.\{0}\phonenumber.data.txt'.format(DataFolderPath)
    AddressesFilePath='.\{0}\address.data.txt'.format(DataFolderPath)

    ContactSequencerFilePath ='.\{0}\Sequencer_Contact.txt'.format(MasterDataFolderPath)
    PhoneNumberSequencerFilePath ='.\{0}\Sequencer_PhoneNumber.txt'.format(MasterDataFolderPath)
    AddressSequencerFilePath ='.\{0}\Sequencer_Address.txt'.format(MasterDataFolderPath)

    LogDataPath ='.\logs\data\contacts.data.log'
    LogErrorPath = '.\logs\data\contacts.err.log'

    ContactSequencer = SequencerAction.getSequencerData(ContactSequencerFilePath)
    PhoneNumberSequencer= SequencerAction.getSequencerData(PhoneNumberSequencerFilePath)
    AddressSequencer = SequencerAction.getSequencerData(AddressSequencerFilePath)

    print('In Load Global Data',ContactSequencer)
    fpDataLog = open(LogDataPath,'a')
    fpErrLog =  open(LogErrorPath,'a')
  

def CleanUpResources():    
    fpDataLog.close()
    fpErrLog.close()
