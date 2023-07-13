import sys
import os
import sqlite3


# Connect to SQL database or create database if it doesn't exist
class DBManager():
    """sqlite3 database class to manage db operations"""  
    pass

    def __init__(self, db_path='data/securespace.db'):
       
        self.__db_connection = sqlite3.connect(db_path, check_same_thread=False)
        self.__db_connection.row_factory = sqlite3.Row # associative array
        self.__db_cursor = self.__db_connection.cursor()
        
    def __del__(self):
        self.__db_connection.close()    

    # where is a tuple
    def do_select( self, query, where = () ):
        try: 
            if where:
                self.__db_cursor.execute( query, where )   
            else:
                self.__db_cursor.execute( query )

            return self.__db_cursor.fetchall()        
        
        except sqlite3.DatabaseError as e:
            print("Error: %s" % (e.args[0]))
    
    # where is a tuple
    def do_update( self, query, where = (), dry = True ):
        
        if where:      
            try:
                self.__db_cursor.execute( query, where )       
                if not dry:                    
                    self.__db_connection.commit()

                return True
            
            except sqlite3.DatabaseError as e:
                print("Error: %s" % (e.args[0]))    

        # No data passed
        else:
            return False
    
    
    
    # where is a list of tuples
    # we need to return the id of the inserted row
    def do_insert( self, query, row = (), dry=True ):
       
        if row:      
            try:
                self.__db_cursor.execute( query, row )       
                if not dry:                    
                    self.__db_connection.commit()

                return self.__db_cursor.lastrowid                
            
            except sqlite3.DatabaseError as e:
                print("Error: %s" % (e.args[0]))    

        # No data passed
        else:
            return False
        
    # where is a tuple
    # delete returns void
    def do_delete( self, query, where = (), dry=True ):
        
        if where:      
            try:         
                self.__db_cursor.execute( query, where )       
                if not dry:
                    self.__db_connection.commit()

                return True
            
            except sqlite3.DatabaseError as e:
                print("Error: %s" % (e.args[0])) 
        # No data passed      
        else:
            return False
        
    # def dict_factory(self, row):
    #     d = {}
    #     for idx, col in enumerate(self.__db_cursor.description):
    #         d[col[0]] = row[idx]
    #     return d
           
#dbman = DBManager()

# test

# mono = dbman.do_select('SELECT * FROM checks WHERE id = ?', (2,) ) 
# print(mono['name'])

#print( dbman.do_insert("INSERT INTO roles(name) VALUES (?) ", ('Astronaut2',),  False ) )

# print( dbman.do_select("SELECT * FROM checks") )

# print( dbman.do_update("UPDATE checks SET name = 'Mono3'  WHERE id = ? ", (5,), False ) )

# print( dbman.do_select("SELECT * FROM checks") )

#print( dbman.do_update("UPDATE checks SET name = 'Mono'  WHERE id = ? ", (2,) ) )

# print( dbman.do_delete("DELETE FROM checks WHERE id = ?", (10,), False ) )
# print( dbman.do_select("SELECT * FROM checks") )

# print( uuid.uuid4() )

# Add error handling
