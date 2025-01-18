import psycopg2 

class PostgresDBConnection: 
    def __init__(self, dbname, user, password, host, port): 
        self.dbname = dbname 
        self.user = user 
        self.password = password 
        self.host = host 
        self.port = port 
        self.conn = None 
        self.cur = None 
    def connect(self): 
        try: 
            self.conn = psycopg2.connect( 
                                        dbname=self.dbname, 
                                        user=self.user, 
                                        password=self.password, 
                                        host=self.host, 
                                        port=self.port 
            ) 
            self.cur = self.conn.cursor() 
            print("Connection successful") 
        except Exception as e: 
            print(f"Error connecting to database: {e}") 
    
    def execute_query(self, query): 
        try: 
            self.cur.execute(query) 
            return self.cur.fetchall() 
        except Exception as e: 
            print(f"Error executing query: {e}") 
            return None 
        
    def close(self): 
        if self.cur: 
            self.cur.close() 
        if self.conn: 
            self.conn.close() 
        print("Connection closed") 
            
# Example usage
if __name__ == "__main__": 
    db = PostgresDB( 
                    dbname="your_dbname", 
                    user="your_username", 
                    password="your_password", 
                    host="your_host", port="your_port" 
    ) 
    db.connect() 
    results = db.execute_query("SELECT * FROM your_table") 
    if results: 
        for row in results: 
            print(row) 
    db.close()