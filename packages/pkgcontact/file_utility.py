import json

def getDataFromFile(fileName):
    try:
        print('FileName in getSeq',fileName)
        filePointer = open(fileName,'r')
        data = None
        lstData = []
        record = filePointer.readline()
        while record:
            lstData.append(json.loads(record))
            filePointer.readline()
            
    except Exception as err:        
        print('Error Occurred...',err)
        lstData = None
    return lstData


def saveDataToFile(clsobjects,fileName):     
     fileSequencer = open(fileName,'w')
     
     for clsobject in clsobjects:
         stringData = json.dumps(clsobject, default=jsDefault)
         fileSequencer.write(stringData)
         
     fileSequencer.close()

def jsDefault(clsobject):
     return clsobject.__dict__;
