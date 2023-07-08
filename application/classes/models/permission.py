'''
    This file contains the Permission class.
'''
import uuid


class Permission:
    '''
        A parent class for the system permissions.
    '''

    def get_permission(self, uuid):
      
        if uuid:
            return self.__db_manager.do_select('SELECT * FROM permissions WHERE uuid = ?', (uuid,) )
        else:
            return False
    
    # Creates a record and returns the inserted id
    def add_permission(self, name):        
        if name:          
            return self.__db_manager.do_insert("INSERT INTO permissions(uuid, name) VALUES (?, ?) ", (str(uuid.uuid4()), name),  False )  
        else:
            return False

    def update_permission(self, uuid, name):
        # update the 'updated_at' attribute.
        # perform database query to update permission attributes.
        query = "UPDATE permissions SET name='" + name + "', updated_at= " + self._updated_at + " WHERE uuid=?"
        values = (uuid,)

        # call do_update method from DBmanager.
        self.__db_manager.do_update(query, values)

    def delete_permission(self, uuid):
        # identify records to delete with id
        query = "DELETE FROM permissions WHERE id = ?"
        where = (uuid,)
        # call do_delete method from DBManager
        return self.__db_manager.do_delete(query, where, False)   
    
    def add_role_has_permissions(self, permission_id, role_id):
        if role_id and permission_id:          
            return self.__db_manager.do_insert("INSERT INTO role_has_permissions(permission_id, role_id) VALUES (?, ?) ", (permission_id, role_id),  False )  
        else:
            return False
        
    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.__db_manager = db_manager
   

#obj_permission = Permission()
#print( obj_permission.add_permission('approve-accounts') )
# rows = obj_permission.get_permission() 
# for row in rows:
#     print( dict(row) )