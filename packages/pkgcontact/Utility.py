class Utility():
     
     def FormatId(contact):
          if hasattr(contact,'Id'):
               print('has contact id')
               return '{:10}'.format(str(contact.Id))

     def FormatGender(contact):
           FormattedString = ""
           if hasattr(contact,'Gender'):        
             if (getattr(contact,'Gender') == 'm') or (getattr(contact,'Gender') == 'M'):            
                 FormattedString = 'Male'
             else:
                 FormattedString = 'Female'
           else:
             print('contact has no gender field')
           return '{:6}'.format(FormattedString)
         
     def FormatName(contact):
         FormattedString ="" 
         if hasattr(contact,'FirstName'):
             if hasattr(contact,'LastName'):               
                 FormattedString = str(contact.FirstName).capitalize() + " " + str(contact.LastName).capitalize()
             else:               
                 FormattedString =  str(contact.FirstName).capitalize()
         elif hasattr(contact,'LastName'):             
             FormattedString =  str(contact.LastName).capitalize()
         else:
             FormatterString = ' No First Name and Last Name Available'

         return '{:25}'.format(FormattedString)

     def FormatOthers(contact):
         FormattedString =""
         if hasattr(contact,'relationshipname'):
             FormattedString=getattr(contact,'relationshipname')
         if hasattr(contact,'OfficeName'):
             FormattedString=getattr(contact,'OfficeName')
         return '{:5}'.format(FormattedString);

     def FormatInputString(contact):
       return Utility.FormatId(contact) + Utility.FormatName(contact) + Utility.FormatGender(contact) + Utility.FormatOthers(contact)

    
          


     
