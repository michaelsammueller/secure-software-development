class AuthSeeder():
    """sqlite3 database class to seed the db operations"""  
    def __init__(self):
        self.countries = {"BR":"Brazil",        
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

        self.roles = ["Superadmin", "Moderator", "Astronaut"]

        self.permissions = ["create-user", "delete-user", "view-all-users",
                    "view-user-details", 
                    "add-health-record", "view-user-health-records",
                    "delete-user-health-records",
                    "view-temperature", "view-radiation", 
        ]

        self.role_has_permissions = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
                                (1,7), (1,8), (1,9),
                                (2,5), (2,6), (2,8), (2,9),
                                (3,5), (3,8), (3,9)
        ]

        self.users = [
            {
                'name': 'Brad',
                'role': 1,
                'date of birth': '09-09-1989',
                'country of employment': 'GB',
                'username': 'Braddarb',
                'password': 'password123'
            }
        ]

    def __call__(self): 
        self.run_seeder()  

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

        for name in self.roles:           
            id = self.__role.add_role(name)
            if id:
                added_ids.append(id) 
        return added_ids
    
    # where is a tuple
    def seed_permissions( self ):

        added_ids = []

        for name in self.permissions:           
            id = self.__permission.add_permission(name)
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
    
    def seed_users( self ):
            
        added_ids = []

        for u in self.users:           
            id = self.__user.add_user(u)
            if id:
                added_ids.append(id) 
        return added_ids
            
    def run_seeder(self):

        c = self.seed_countries()
        r = self.seed_roles()   
        p = self.seed_permissions()  
        rhp = self.seed_role_has_permissions()
        u = self.seed_users()

    def connect_country(self, country):
        """Connects the country"""
        self.__country = country

    def connect_role(self, role):
        """Connects the role"""
        self.__role = role

    def connect_permission(self, permission):
        """Connects the permission"""
        self.__permission = permission
    
    def connect_user(self, user):
        """Connects the user"""
        self.__user = user
