class Backtest:

    def __init__(self,Trader,sql,starting_capital,frequency,max_lookback):
        self.Trader=Trader
        self.sql=sql
        self.capital=starting_capital
        self.frequency=frequency
        self.max_lookback=max_lookback
    
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
            n_tickers=len(current_data[securities[0]])

            current_trader=self.Trader(self.capital,securities,self.max_lookback,n_tickers/self.frequency)
            
            
            for i in range(0,n_tickers,self.frequency):

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

                    
                



        