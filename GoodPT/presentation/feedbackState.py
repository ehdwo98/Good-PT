class feedState:
    def __init__(self,questionnum,questionlist):
        self.__questionnum = questionnum
        self.__questionlist = questionlist
        
    @property
    def questionnum(self):
        return self.__questionnum
    
    @property
    def questionlist(self):
        return self.__questionlist    
    
    @questionlist.setter
    def questionlist(self,questionlist):
        self.__questionlist = questionlist
    
    @questionnum.setter
    def questionnum(self,questionnum):
        self.__questionnum = questionnum
        
InitialState = feedState(1,['blank1','blank2','blank3','blank4','blank5'])