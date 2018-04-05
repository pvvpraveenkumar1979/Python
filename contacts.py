# this is the main file
# Built in modules
import sys
import os
# end Built in modules

import packages.pkgcontact.contact_actions as contact_actions
import packages.pkgcontact.contact_sequencers
import packages.pkgcontact.contact_globals as GlobalData

def ContactsApplication():
     os.system('cls')
     print('\n\n Welcome to Contacts Manager \n\n')
     GlobalData.LoadGlobalData()

     Quit = 'N'
     while Quit !='y' and Quit!='Y':

          print('What do you want to do ?')
          print('[A].Add New Contact')
          print('[U].Update Contact')
          print('[D].Delete Contact')
          print('[L] List Contacts')
          print('[S] Search Contacts')
          print('[X] Exit')
          
          action = input()
          
          if action == 'a' or action == 'A':
               print('Add New Contact')
               contact_actions.CreateContact()
          elif action =='d' or action =='D':
               print('Delete Contact')
          elif action == 'U' or action == 'u':
               print('Update Contact')
          elif action == 'L' or action =='l':
               print('Read contacts')
               contact_actions.ReadContacts()
          elif action=='S' or action =='l':
               print('Searching contacts....')
               contact_actions.FindContact()
          elif action =='X' or action =='x':
               exit()
               
          print('Do you want to quit (yes/no)')
          Quit = input()

     print('Cleaning up resources')
     GlobalData.CleanUpResources()
