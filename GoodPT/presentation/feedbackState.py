class feedState:
    def __init__(self,questionnum,questionlist,answerlist):
        self.__questionnum = questionnum
        self.__questionlist = questionlist
        self.__answerlist = answerlist
        
    @property
    def questionnum(self):
        return self.__questionnum
    
    @property
    def questionlist(self):
        return self.__questionlist    
    
    @property
    def answerlist(self):
        return self.__answerlist
    
      
    @questionlist.setter
    def questionlist(self,questionlist):
        self.__questionlist = questionlist
    
    @questionnum.setter
    def questionnum(self,questionnum):
        self.__questionnum = questionnum
        
    @answerlist.setter
    def answerlist(self,answerlist):
        self.__answerlist = answerlist
        
InitialState = feedState(1,['blank1','blank2','blank3','blank4','blank5'],[])