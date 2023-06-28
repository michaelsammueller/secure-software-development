'''
    This file contains the Permission class.
'''
import datetime
import dbmanager


class Permission:
    def __init__(self, name):
        self._name = name
        self._created_at = None
        self._updated_at = None
        self._permission_id = None # return from databse

        # initialise instance of DBManager
        self.db_manager = dbmanager.DBManager()

        # set current_time to now
        self.current_time = datetime.datetime.now()

    def add_permission(self):
        # update created_at and updated_at attributes
        if self._created_at is None:
            self._created_at = self.current_time
        self._updated_at = self.current_time

        # prepare the data for updating the permissions table
        values = (self._name, self._permission_id, self._created_at, self._updated_at)

        # call do_insert method from DBManager
        query = "INSERT INTO permissions (name, permission_id, created_at, updated_at) \
            VALUES (?, ?, ?, ?)"
        self.db_manager.do_insert(query, [values], dry=False)

    def update_permission(self):
        # update the 'updated_at' attribute.
        self._updated_at = self.current_time

        # perform database query to update permission attributes.
        query = "UPDATE permissions SET name=?, updated_at=? WHERE permission_id=?"
        values = (self._name, self._updated_at, self._permission_id)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_permission(self):
        # identify records to delete with id
        query = "DELETE FROM permissions WHERE id = ?"
        where = (self._permission_id)

        # call do_delete method from DBManager
        result = self.db_manager.do_delete(query, where, dry=True)
        
        # if id is matched, records will be deleted.
        if result:
            print(f"Deleted {len(result)} record(s) from permissions table.")
            return True
        
        # if id is not matched, records will not be deleted.
        else:
            print("No records deleted.")
            return False
    
