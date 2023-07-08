'''
    This file contains the Role class.
'''

import datetime
import time

class HealthRecord:
    '''
        A parent class for the system healthrecords.
    '''

    # Creates a record and returns the inserted id
    def add_record(self, new_health_record_details):
        name = new_health_record_details['name']
        height = new_health_record_details['height']
        weight = new_health_record_details['weight']
        blood_pressure = new_health_record_details['blood_pressure']
        created_at = time.mktime(datetime.datetime.now().timetuple()) 
        updated_at = time.mktime(datetime.datetime.now().timetuple())  
        query = "INSERT INTO record_items(name, height, weight, blood_pressure, created_at, updated_at) VALUES (?, ?, ?, ?)"
        values = [name, height, weight, blood_pressure, created_at, updated_at]              
        return self.db_manager.do_insert(query, values,  False)   

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.db_manager = db_manager 
