import os
import sys

# Dynamically modify the path
fpath = os.path.join(os.path.dirname(__file__), 'classes')
sys.path.append(fpath)

from classes.country import Country
from classes.role import Role
from classes.permission import Permission

class AuthSeeder():
    """sqlite3 database class to seed the db operations"""  
    
    countries = {"BR":"Brazil",        
        "CA":"Canada",        
        "DK":"Denmark",       
        "FR":"France",        
        "DE":"Germany",        
        "IT":"Italy",       
        "JP":"Japan", 
        "NL":"Netherlands",       
        "NO":"Norway",  
        "RU":"Russian Federation",      
        "ES":"Spain",  
        "SE":"Sweden",
        "SZ":"Switzerland",        
        "GB":"United Kingdom",
        "US":"United States"       
    }

    roles = {"1":"Superadmin",        
        "2":"Moderator",        
        "3":"Astronaut"  
    }

    permissions = {"1":"create-user",        
        "2":"aproove-user",        
        "3":"delete-user",
        "4":"assign-role",
        "5":"update-record"  
    }

    def __init__(self):
       
        self.__country = Country()   
        self.__role = Role() 
        self.__permission = Permission()    

    # where is a tuple
    def seed_countries( self ):

        added_ids = []

        for k, v in self.countries.items():           
            id = self.__country.add_country(k, v)
            if id:
                added_ids.append(id) 
        return added_ids
    
    # where is a tuple
    def seed_roles( self ):

        added_ids = []

        for k, v in self.roles.items():           
            id = self.__role.add_role(v)
            if id:
                added_ids.append(id) 
        return added_ids
    
    # where is a tuple
    def seed_permissions( self ):

        added_ids = []

        for k, v in self.permissions.items():           
            id = self.__permission.add_permission(v)
            if id:
                added_ids.append(id) 
        return added_ids
    
    def run_seeder(self):

        c = self.seed_countries()
        r = self.seed_roles()   
        p = self.seed_permissions()       
    

obj_seeder = AuthSeeder()
obj_seeder.run_seeder()

