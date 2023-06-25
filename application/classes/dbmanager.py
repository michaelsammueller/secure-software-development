import sys
import sqlite3

# Connect to SQL database or create database if it doesn't exist
class DBManager():
    """sqlite3 database class to manage db operations"""  
    pass

    def __init__(self):
       
        self.__db_connection = sqlite3.connect(sys.path[0].rstrip('classes') + 'data/securespace.db')
        self.__db_cursor = self.__db_connection.cursor()
        
    def __del__(self):
        self.__db_connection.close()    

    # where is a tuple
    def do_select( self, query, where = () ):
        
        if where:               
            self.__db_cursor.execute( query, where )           
            
        else:
            self.__db_cursor.execute( query )

        return self.__db_cursor.fetchall()
    
    # where is a tuple
    def do_update( self, query, where = () ):
        
        if where:               
            self.__db_cursor.execute( query, where )           
            
        else:
            self.__db_cursor.execute( query )

        return self.__db_cursor.fetchall()
    
    
    
    # where is a tuple
    def do_insert( self, query, where = [], dry=True ):
        
        if where:               
            self.__db_cursor.executemany( query, where )       
            if not dry:
                self.__db_connection.commit()

            return self.__db_cursor.fetchall()
        else:
            return False
        
    # where is a tuple
    def do_delete( self, query, where = (), dry=True ):
        
        if where:               
            self.__db_cursor.execute( query, where )       
            if not dry:
                self.__db_connection.commit()

            return self.__db_cursor.fetchall()
        else:
            return False
           
# dbman = DBManager()

# test
# print( dbman.do_select('SELECT count(*) FROM checks WHERE id = ? OR id = ? ', (2,1) ) )

#print( dbman.do_insert("INSERT INTO checks(id, name) VALUES (?, ?) ", [(3, 'Anotherone'),], False ) )

# print( dbman.do_select("SELECT * FROM checks") )

# print( dbman.do_update("UPDATE checks SET name = 'Mono'  WHERE id = ? ", (2,) ) )

# print( dbman.do_select("SELECT * FROM checks") )

# print( dbman.do_update("UPDATE checks SET name = 'Mono'  WHERE id = ? ", (2,) ) )

# print( dbman.do_delete("DELETE FROM checks WHERE id = ?", (3,), False ) )

# print( dbman.do_select("SELECT * FROM checks") )
