class Indicators:

    def __init__(self):
        self.name="Indicators"
    
    def sma(self,window, series):
        
        if(window>len(series)):
            return -1

        return (sum(series[-window:])/window)