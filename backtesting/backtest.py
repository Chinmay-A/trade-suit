class Backtest:

    def __init__(self,Trader,sql,starting_capital):
        self.Trader=Trader
        self.sql=sql
        self.capital=starting_capital
    
    def start_backtest(self):

        self.profits=[0]
        self.net_worth=[self.capital]
        self.trades=[]

        days=self.sql.get_unique_days()
        securities=self.sql.get_securities()

        print("Starting Backtest.....")

        for day in days:

            print(f"running test for {day} |", end="")
            
            current_data=self.sql.get_data_for_day(day)
            n_tickers=len(current_data['ongc'])

            current_trader=self.Trader(self.capital,securities,1,20,n_tickers/5)
            
            
            for i in range(0,n_tickers,5):

                ltps={}

                for security in securities:

                    ltps[security]=current_data[security]['close'][i]
                
                current_trader.backtest_trade(ltps,ltps)

            #self.trades.append(current_trader.get_trades_for_day())
            self.profits.append(current_trader.get_profits_for_day())
            self.capital=self.capital+current_trader.get_profits_for_day()
            print(f" Profits for {day}: {self.profits[-1]} | Charges incurred: {current_trader.get_charges_for_day()}")   
            self.net_worth.append(self.net_worth[-1]+self.profits[-1])

        import statistics

        print(f"Sharpe : {statistics.mean(self.profits)/statistics.stdev(self.profits)}")
        print(f"Net Worth: {self.net_worth[-1]}")
        
        #print(self.trades)
        
        from matplotlib import pyplot as plt

        plt.plot(self.net_worth)
        plt.show()

        return self.net_worth,self.profits,self.trades         

                    
                



        