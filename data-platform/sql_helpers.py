import mysql.connector as mysql

class SQL:
    
    def __init__(self,username,password,database):
        
        self.user=username
        self.db=database
        try:
            self.connection=mysql.connect(username=username,password=password,host='localhost',database=database)
            print("connected to mysql with user: "+username+"@localhost")
            self.cursor=self.connection.cursor()
            self.cursor.execute("show tables;")
            self.securities=[security[0] for security in self.cursor.fetchall()]
        except:
            print("Authenticaion Error: Connection Failed")
    
    def get_connection(self):
        return self.connection

    def add_table(self,security):
        
        query="CREATE TABLE "+security+" "
        query+="(date VARCHAR(255),time VARCHAR(255), open float, high float, low float, close float, volume float);"
        
        #print(query)
        self.connection.cursor().execute(query)
    
    def add_data(self,instrument_key,data):

        query='INSERT INTO '+instrument_key+' (date, time, open, high, low, close, volume) VALUES ('
        
        for i in range(len(data)):

            if i!=len(data)-1:
                query+= "'"+str(data[i])+"'"+','
            else:
                query+="'"+str(data[i])+"'"
        
        query+=');'

        #print(query)

        self.connection.cursor().execute(query)
        self.connection.commit()
    
    def get_unique_days(self):

        
        self.cursor.execute("select distinct date from ongc;")
        results=self.cursor.fetchall()
        return [day[0] for day in results]
    
    def get_data_for_day(self,day):

        import pandas as pd

        data_for_day={}

        columns_mapping={
            0:'date',
            1:'time',
            2:'open',
            3:'high',
            4:'low',
            5:'close',
            6:'volume'
        }

        for security in self.securities:

            #print(f"select * from {security} where date='{day}'")
            self.cursor.execute(f"select * from {security} where date='{day}'")
            results=self.cursor.fetchall()

            curr_df=pd.DataFrame(results)
            curr_df.rename(columns=columns_mapping,inplace=True)

            curr_df=curr_df.iloc[::-1]
            data_for_day[security]=curr_df.reset_index().drop(columns='index')
        
        return data_for_day


        
        
        


    