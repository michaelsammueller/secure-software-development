class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = []
   
#system roles as child classes of Role class
class Astronaut(Role):
    def __init__(self):
        super().__init__("Astronaut")
        self.permissions = ["read", "write", "download"]

    def __str__(self):
        return f"{self.name} has {self.permissions} permissions"
        
class Moderator(Role):
    def __init__(self):
        super().__init__("Moderator")
        self.permissions = ["approve", "delete", "view"]

    def __str__(self):
        return f"{self.name} has {self.permissions} permissions"

class Superadmin(Role):
    def __init__(self):
        super().__init__("Superadmin")
        self.permissions = ["create user", "assign roles", "execute SQL", "delete", "view", "update"]

    def __str__(self):
        return f"{self.name} has {self.permissions} permissions"
