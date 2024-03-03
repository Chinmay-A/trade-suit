import mysql.connector as mysql

class sqlhelp:
    
    def __init__(self,username,password,database):
        
        self.user=username
        self.db=database
        try:
            self.connection=mysql.connect(username=username,password=password,host='localhost',database=database)
            print("connected to mysql with user: "+username+"@localhost")
        except:
            print("Authenticaion Error: Connection Failed")

    def add_table(self,security):
        
        query="CREATE TABLE "+security+" "
        query+="(date VARCHAR(255),time VARCHAR(255), open float, high float, low float, close float, volume float);"
        
        self.connection.cursor().execute(query)
    
    def add_data(self,instrument_key,data,connection):

        query='INSERT INTO '+instrument_key+' (date, time, open, low, high, close, volume) VALUES ('
        
        for i in range(len(data)):

            if i!=len(data)-1:
                query+= "'"+data[i]+"'"+','
            else:
                query+="'"+data[i]+"'"
        
        query+=');'

        #print(query)

        connection.cursor().execute(query)
        connection.commit()


    