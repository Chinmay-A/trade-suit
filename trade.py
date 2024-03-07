class Trader:

    def __init__(self,starting_capital,securities,frequency,max_lookback):
        
        self.capital=starting_capital
        self.positions={}
        self.trades=[]
        self.securities=securities
        self.ltps={}
        self.vol={}
        self.charges=0
        self.frequency=frequency
        self.timestamp=0
        self.profits=0
        self.lookback=max_lookback
        self.takeprofit=0.01
        self.stoploss=0.05

        positons_template={
            'quantity':0,
            'price':0,
            'type':0
        }

        for security in self.securities:
            self.ltps[security]=[]
            self.vol[security]=[]
            self.positions[security]=positons_template

        print(f"Trader Initialized timestamp: {self.timestamp}")

    def take_position(self,security,price,quantity,position_type):

        if(self.positions[security]['quantity']!=0):
            raise Exception("Cannot take new position in a security with a active position")
        else:

            if(self.capital<price*quantity):
                raise Exception("Not Enough Margin Available")
            else:
                self.capital=self.capital-price*quantity
                self.charges=self.charges+0.0005*price*quantity
            
            #take position
            self.positions[security]['quantity']=quantity
            self.positions[security]['price']=price
            self.positions[security]['type']=position_type
            
            if(position_type==1):
                self.trades.append(f"BUY {quantity} OF {security} AT {price}")
                print(f"BUY {quantity} OF {security} AT {price}")
            else:
                self.trades.append(f"SELL {quantity} OF {security} AT {price}")
                print(f"SELL {quantity} OF {security} AT {price}")
    
    def exit_position(self,security,exit_price):

        if(self.positions[security]['quantity']==0):
            raise Exception("Cannot exit position in a secuirty with no active position")
        else:
            
            if(self.positions[security]['type']==1):
                self.charges=self.charges+0.005*exit_price*self.positions[security]['quantity']
                self.profits=self.profits+(exit_price-self.positions[security]['price'])*self.positions[security]['quantity']
            elif(self.positions[security]['type']==-1):
                self.charges=self.charges+0.005*exit_price*self.positions[security]['quantity']
                self.profits=self.profits+(self.positions[security]['price']-exit_price)*self.positions[security]['quantity']
            else:
                raise Exception("Cannot exit position of security with no active position")
            
            #exit position
            self.positions[security]['quantity']=0
            self.positions[security]['price']=0
            self.positions[security]['type']=0




    
    def backtest_trade(self,update,vol_update,close_time):

        import sys
        sys.path.append('../')
        import indicators

        self.timestamp+=1
        
        #print(f"timestamp: {self.timestamp}")

        for security in self.securities:
            self.ltps[security].append(update[security])
            self.vol[security].append(vol_update[security])
        
        if self.timestamp<self.lookback:
            return None
        
        if self.timestamp==close_time:

            print("Closing all Positions before market close")
            for security in self.securities:

                position=self.positions[security]
                
                if position['quantity']!=0:

                    if(position['type']==1):
                        self.trades.append(f"{self.timestamp}: SELL {position['quantity']} of {security} at {update[security]}")
                        self.profits+=(update[security]-position['price'])*position['quantity']
                        self.charges+=0.0005*position['quantity']*update[security]
                    elif(position['type']==-1):
                        self.trades.append(f"{self.timestamp}: BUY {position['quantity']} of {security} at {update[security]}")
                        self.profits+=(position['price']-update[security])*position['quantity']
                        self.charges+=0.0005*position['quantity']*update[security]
                    else:
                        raise Exception("There's a bug")
                
                self.positions[security]['quantity']=0
                self.positions[security]['price']=0
                self.positions[security]['type']=0
            
            return None

        for security in self.securities:

            if(self.positions[security]['quantity']==0):
                
                if(self.capital<=update[security]):
                    continue
                
                b,m,u=indicators.bollinger_bands(self.lookback,self.ltps[security],devs=2)

                if(update[security]>b):
                    
                    self.positions[security]['quantity']=int(max(update[security],min(self.capital,1000))/update[security])
                    self.positions[security]['price']=update[security]
                    self.positions[security]['type']=1

                    self.trades.append(f"{self.timestamp}: BUY {self.positions[security]['quantity']} of {security} at {self.positions[security]['price']}")

                    self.charges+=0.0005*self.positions[security]['price']

                elif(update[security]<u):

                    self.positions[security]['quantity']=int(max(update[security],min(self.capital,1000))/update[security])
                    self.positions[security]['price']=update[security]
                    self.positions[security]['type']=-1

                    self.trades.append(f"{self.timestamp}: SELL {self.positions[security]['quantity']} of {security} at {self.positions[security]['price']}")
            else:

                position=self.positions[security]

                if(position['type']==1):

                    if((update[security]>=(1+self.takeprofit)*position['price']) or (update[security]<=(1-self.stoploss)*position['price'])):
                        
                        self.positions[security]['quantity']=0
                        self.positions[security]['type']=0
                        self.positions[security]['price']=0

                        self.profits+=(update[security]-position['price'])*position['quantity']
                        self.charges+=0.0005*update[security]

                        self.trades.append(f"{self.timestamp}: SELL {position['quantity']} of {security} at {update[security]}")
                elif(position['type']==-1):

                    if((update[security]<=(1-self.takeprofit)*position['price']) or (update[security]>=(1+self.stoploss)*position['price'])):
                        
                        self.positions[security]['quantity']=0
                        self.positions[security]['type']=0
                        self.positions[security]['price']=0

                        self.profits+=(position['price']-update[security])*position['quantity']
                        self.charges+=0.0005*update[security]

                        self.trades.append(f"{self.timestamp}: BUY {position['quantity']} of {security} at {update[security]}")
        
        return None
    def get_profits_for_day(self):
        return self.profits-self.charges
    def get_trades_for_day(self):
        return self.trades
    
        

        

        
        

