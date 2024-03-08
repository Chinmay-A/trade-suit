class Trader:

    def __init__(self,starting_capital,securities,frequency,max_lookback,close_time):
        
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
        self.takeprofit=0.02
        self.stoploss=0.3
        self.closetime=close_time

        for security in self.securities:
            self.ltps[security]=[]
            self.vol[security]=[]
            positons_template={
                'quantity':0,
                'price':0,
                'type':0
            }
            self.positions[security]=positons_template
        
        #print(self.positions)

        print(f"Trader Initialized with capital: {self.capital}")

    def take_position(self,security,price,quantity,position_type):

        #print(f"Before taking position Security: {security} ",self.positions[security])
        #print("Inside func: ",self.positions)

        #print("inside func: ", security)
        
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
            
            #print("end func: ", security)
            #print("End func: ",self.positions)
            # print(f"After taking position Security: {security} ",self.positions[security])
    
    def exit_position(self,security,exit_price):

        #print(self.positions[security])

        if(self.positions[security]['quantity']==0):
            raise Exception("Cannot exit position in a secuirty with no active position")
        else:
            
            if(self.positions[security]['type']==1):
                self.charges=self.charges+0.0005*exit_price*self.positions[security]['quantity']
                self.profits=self.profits+(exit_price-self.positions[security]['price'])*self.positions[security]['quantity']
                
                self.trades.append(f"SELL EXIT {self.positions[security]['quantity']} OF {security} AT {exit_price}")
                print(f"SELL EXIT {self.positions[security]['quantity']} OF {security} AT {exit_price}")
            elif(self.positions[security]['type']==-1):
                self.charges=self.charges+0.0005*exit_price*self.positions[security]['quantity']
                self.profits=self.profits+(self.positions[security]['price']-exit_price)*self.positions[security]['quantity']

                self.trades.append(f"BUY BACK {self.positions[security]['quantity']} OF {security} AT {exit_price}")
                print(f"BUY BACK {self.positions[security]['quantity']} OF {security} AT {exit_price}")
            else:
                raise Exception("Cannot exit position of security with no active position")
            
            #exit position
            self.positions[security]['quantity']=0
            self.positions[security]['price']=0
            self.positions[security]['type']=0

    def backtest_trade(self,update,vol_update):

        #print(f"at timestamp: {self.timestamp}")
        import sys
        sys.path.append('../')
        import indicators

        self.timestamp+=1

        #process updates to memory
        for security in self.securities:
            self.ltps[security].append(update[security])
            self.vol[security].append(vol_update[security])
        
        #do nothing if timestamp is less than maximum lookback period
        if self.timestamp<self.lookback:
            return None
        
        #close all positions if market is at close
        if(self.timestamp>=self.closetime):

            print("Closing all Positions before market close")
            
            for security in self.securities:

                if(self.positions[security]['quantity']!=0):
                    
                    self.exit_position(security,update[security])

            
            return None
        else:

            #during active trading hours
            for security in self.securities:
                
                #rsi=indicators.rsi(self.ltps[security],10)
                #for securities with no active positions
                if(self.positions[security]['quantity']==0):
                    
                  print("Update under progress")
                    
                #for securities with active positions
                else:
                    #print(self.positions)
                    #position=self.positions[security]

                    #if the active position is long
                    if(self.positions[security]['type']==1):

                        #check if the position has hit take profit or stoploss
                        if((update[security]<=(1+self.takeprofit)*self.positions[security]['price']) or (update[security]<=(1-self.stoploss)*self.positions[security]['price'])):
                            
                            self.exit_position(security,update[security])   
                    #if the active position is short
                    elif(self.positions[security]['type']==-1):

                        if((update[security]<=(1-self.takeprofit)*self.positions[security]['price']) or (update[security]>=(1+self.stoploss)*self.positions[security]['price'])):
                            self.exit_position(security,update[security])
        
        return None
    def get_profits_for_day(self):
        return self.profits-self.charges
    def get_charges_for_day(self):
        return self.charges
    def get_trades_for_day(self):
        return self.trades
    
        

        

        
        

