import bcrypt


class AuthSeeder():
    """sqlite3 database class to seed the db operations"""
    def __init__(self):
        self.countries = {"BR": "Brazil",
                          "CA": "Canada",
                          "DK": "Denmark",
                          "FR": "France",
                          "DE": "Germany",
                          "IT": "Italy",
                          "JP": "Japan",
                          "NL": "Netherlands",
                          "NO": "Norway",
                          "RU": "Russian Federation",
                          "ES": "Spain",
                          "SE": "Sweden",
                          "SZ": "Switzerland",
                          "GB": "United Kingdom",
                          "US": "United States"
                          }

        self.roles = ["Superadmin", "Moderator", "Astronaut"]

        self.permissions = ["create-user", "delete-user", "view-all-users", "view-user-details",
                            "update-user-details", "add-health-record", "add-own-health-record",
                            "view-user-health-records", "view-own-health-records",
                            "update-user-health-record", "delete-user-health-records",
                            "view-temperature", "view-radiation", "change-password"
                            ]

        self.role_has_permissions = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                                     (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14),
                                     (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 12),
                                     (2, 13), (2, 14), (3, 7), (3, 9), (3, 12), (3, 13), (3, 14)]

        self.records = [
            {
                'uuid': '12345',
                'complains': 'headache',
                'height': '180',
                'weight': '80',
                'blood_pressure': '120',
            }
        ]

        self.users = [
            {
                'name': 'Brad',
                'role': 1,
                'date of birth': '09-09-1989',
                'country of employment': 'GB',
                'username': 'Braddarb',
                'password': 'password123',
                'secret phrase': 'ok',
                'uuid': '12345'
            },
            {
                'name': 'Michael',
                'role': 3,
                'date of birth': '30-06-1998',
                'country of employment': 'DE',
                'username': 'michael.sammueller',
                'password': 'michael123',
                'secret phrase': 'ok',
                'uuid': '987654'
            },
        ]

    def __call__(self):
        # encrypt user passwords
        for i in range(len(self.users)):
            self.users[i]['password'] = bcrypt.hashpw(self.users[i]['password'].encode('utf-8'),
                                                      bcrypt.gensalt())
        # seed database
        self.run_seeder()

    # where is a tuple
    def seed_countries(self):

        added_ids = []

        for k, v in self.countries.items():
            id = self.__country.add_country(k, v)
            if id:
                added_ids.append(id)
        return added_ids

    # where is a tuple
    def seed_health_records(self):

        added_ids = []

        for record in self.records:
            id = self.__health_record.add_record(record)
            if id:
                added_ids.append(id)
        return added_ids

    # where is a tuple
    def seed_roles(self):

        added_ids = []

        for name in self.roles:
            id = self.__role.add_role(name)
            if id:
                added_ids.append(id)
        return added_ids

    # where is a tuple
    def seed_permissions(self):

        added_ids = []

        for name in self.permissions:
            id = self.__permission.add_permission(name)
            if id:
                added_ids.append(id)
        return added_ids

    def seed_role_has_permissions(self):

        added_ids = []

        for t in self.role_has_permissions:
            id = self.__permission.add_role_has_permissions(t[1], t[0])
            if id:
                added_ids.append(id)
        return added_ids

    def seed_users(self):

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
        hr = self.seed_health_records()

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

    def connect_health_record(self, health_record):
        """Connects the health_record"""
        self.__health_record = health_record

    def connect_encryption(self, encryption):
        """Connects the encryption"""
        self.__encryption_service = encryption
