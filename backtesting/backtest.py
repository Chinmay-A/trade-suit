class Backtest:

    def __init__(self,Trader,sql,starting_capital):
        self.trader=trader
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

            print(f"testing for {day} ", end="")

            current_trader=Trader()
            current_data=self.sql.get_data_for_day(day)

            current_position={}

            n_tickers=len(current_data['ongc'])

            for i in range(n_tickers):

                ltps={}

                for security in securities:

                    ltps[security]=current_data[security]['close'][i]
                
                current_trader.trade(ltps)

            self.trades.append(current_trader.get_trades_for_day())
            self.profits.append(current_trader.get_profits_for_day())
            print(f" Profits: {self.profits[-1]}")   
            self.net_worth.append(self.net_worth[-1]+self.profits[-1])

        import statistics

        print(f"Sharpe : {statistics.mean(self.profits)/statistics.stdev(self.profits)}")
        
        from matplotlib import pyplot as plt

        plt.plot(self.net_worth)

        return self.net_worth,self.profits,self.trades         

                    
                



        