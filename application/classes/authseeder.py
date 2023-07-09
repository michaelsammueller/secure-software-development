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

    roles = ["Superadmin", "Moderator", "Astronaut"]

    permissions = ["create-user", "delete-user", "update-user", 
                   "add-health-record", "view-health-record",
                   "update-health-record", "delete-health-record"
                   "view-temperature", "view-radiation", 
    ]

    role_has_permissions = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6)
                            (1,7), (1,8), (1,9),
                            (2,5), (2,6), (2,8), (2,9),
                            (3,4), (3,5), (3,6), (3,7), (3,8), (3,9)
    ]

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
    
    def seed_role_has_permissions( self ):

        added_ids = []

        for t in self.role_has_permissions:           
            id = self.__permission.add_role_has_permissions(t[1], t[0])            
            if id:
                added_ids.append(id) 
        return added_ids
        
    def run_seeder(self):

        c = self.seed_countries()
        r = self.seed_roles()   
        p = self.seed_permissions()  
        rhp = self.seed_role_has_permissions()     
    

obj_seeder = AuthSeeder()
obj_seeder.run_seeder()
