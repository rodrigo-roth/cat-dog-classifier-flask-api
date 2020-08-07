import sqlite3

class SQLConnection:

    def __init__(self, path):
        
        self.conn = sqlite3.connect(path)

        self.cur = self.conn.cursor()

    
    def insert_data(self, user, timestamp, cd_class):
        
        self.cur.execute("INSERT INTO class_classifier (user, timestamp, cd_class) VALUES (?, ?, ?)", (user, timestamp, cd_class))
        
        self.conn.commit()
    

  

