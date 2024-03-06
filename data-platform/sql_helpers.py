import mysql.connector as mysql

class SQL:
    
    def __init__(self,username,password,database):
        
        self.user=username
        self.db=database
        try:
            self.connection=mysql.connect(username=username,password=password,host='localhost',database=database)
            print("connected to mysql with user: "+username+"@localhost")
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

        cursor=self.connection.cursor()
        cursor.execute("select distinct date from ongc;")
        results=cursor.fetchall()
        return [day[0] for day in results]
    
    def get_data_for(self):
        print("under construction")


    