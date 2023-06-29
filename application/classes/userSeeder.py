from user import User
# Connect to SQL database or create database if it doesn't exist
class UserSeeder():
    """sqlite3 database class to manage db operations"""  
    pass

    def __init__(self, User):
       
        self.__user = User        
        
    def __del__(self):
        self.__db_connection.close()    

    # where is a tuple
    def do_select( self, query, where = () ):
        
        if where:               
            self.__db_cursor.execute( query, where )           
            
        else:
            self.__db_cursor.execute( query )

        return self.__db_cursor.fetchall()