
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

    permissions = ["create-user", "aproove-user", "delete-user", "assign-role", "update-record"]
    

    role_has_permissions = [ (1,1), (1,4), (2,2), (2,3), (3,5) ]

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

        for v in self.roles:           
            id = self.__role.add_role(v)
            if id:
                added_ids.append(id) 
        return added_ids
    
    # where is a tuple
    def seed_permissions( self ):

        added_ids = []

        for v in self.permissions:           
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

    def connect_role_service(self, role_service):
        '''
            Connects the role service
        '''
        self.__role = role_service   

    def connect_permission_service(self, permission_service):
        '''
            Connects the permission service
        '''
        self.__permission = permission_service

    def connect_country_service(self, country_service):
        '''
            Connects the country service
        '''
        self.__country = country_service

