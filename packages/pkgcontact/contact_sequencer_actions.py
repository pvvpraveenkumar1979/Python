import json

def getSequencerData(fileName):
    try:
        print('FileName in getSeq',fileName)
        fileSequencer = open(fileName,'r')
        sequencerData = None
        record = fileSequencer.readline()
        sequencerData =json.loads(record)
    except Exception as err:        
        print('Error Occurred...',err)
        sequencerData = None
    return sequencerData


def saveSequencerData(sequenceObject,fileName):     
     stringSequencerData = json.dumps(sequenceObject, default=jsDefault)
     fileSequencer = open(fileName,'w')
     fileSequencer.write(stringSequencerData)
     fileSequencer.close()

def jsDefault(sequencer):
     return sequencer.__dict__;
