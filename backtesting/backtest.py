class Backtest:

    def __init__(self,trader,sql):
        self.trader=trader
        self.sql=sql
    
    def start_backtest(self):

        self.profits=[]
        days=self.sql.get_unique_days()
        

        