import packages.pkgcontact.contact_sequencer_actions

class contactSequencer():
    
    def __init__(self,seqName,startvalue,stepvalue,currentvalue):
        self.SEQNAME = seqName
        self.STARTVALUE = startvalue
        self.STEPVALUE = stepvalue
        self.CURRENTVALUE = currentvalue

    def getCurrentValue(self):
        return self.CURRENTVALUE

    def incrementSequencer(self):
        self.CURRENTVALUE  = self.CURRENTVALUE + self.STEPVALUE




    

