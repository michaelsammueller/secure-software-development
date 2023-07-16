'''
    This file contains the Health Record class.
'''


class HealthRecord:
    '''
        A parent class for the system healthrecords.
    '''

    def __init__(self):
        self.__num_records = 0

    def add_record(self, new_health_record_details):
        '''
            Adds a health record to the database
        '''
        nhrd = new_health_record_details
        query = ("INSERT INTO record_items"
                 "(uuid, record_id, complaints, height, weight, blood_pressure)"
                 "VALUES (?, ?, ?, ?, ?, ?)")
        values = (nhrd['uuid'], (self.__num_records + 1), nhrd['complaints'], nhrd['height'],
                  nhrd['weight'], nhrd['blood_pressure'])
        self.__num_records += 1
        return self.__db_manager.do_insert(query, values,  False)

    def view_user_health_records(self, user_identifiers):
        '''
            View a users health records from the database
        '''
        query = "SELECT * FROM record_items WHERE uuid = ?"
        where = (user_identifiers['uuid'],)

        # call do_select method from DBManager.
        result = self.__db_manager.do_select(query, where)
        if result:
            json = [
                {result[j].keys()[i]: value for i, value in enumerate(result[j])}
                for j in range(len(result))]
        else:
            json = {}
        return json

    def delete_user_health_records(self, user_identifiers):
        '''
            Delete a user from the database
        '''
        query = "DELETE FROM record_items WHERE uuid = ?"
        where = (user_identifiers['uuid'],)
        # call do_delete method from DBManager
        return self.__db_manager.do_delete(query, where, False)

    def update_health_record(self, user_information):
        '''
            Update a health record in the database
        '''
        field = user_information['field']
        value = user_information['new value']
        if field in ['complaints']:
            value = f"'{value}'"
        query = f"UPDATE record_items SET {field} = {value} WHERE record_id = ?"
        where = (user_information['record id'],)
        # call do_delete method from DBManager
        return self.__db_manager.do_update(query, where, False)

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.__db_manager = db_manager
