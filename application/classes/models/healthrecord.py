'''
    This file contains the Health Record class.
'''

import uuid

class HealthRecord:
    '''
        A parent class for the system healthrecords.
    '''

    def __init__(self):
        self.__num_records = 0

    # Creates a record and returns the inserted id
    def add_record(self, new_health_record_details):
        nhrd = new_health_record_details
        query = "INSERT INTO record_items(uuid, record_id, complains, height, weight, blood_pressure) VALUES (?, ?, ?, ?, ?, ?)"
        values = (nhrd['uuid'], (self.__num_records + 1), nhrd['complains'], nhrd['height'], 
                  nhrd['weight'], nhrd['blood_pressure'])
        print(values) 
        self.__num_records += 1             
        return self.db_manager.do_insert(query, values,  False)   

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.db_manager = db_manager 
