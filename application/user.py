class User:
    '''creates user objects dynamically'''
    def __init__(self, first_name, last_name, username, password, secret_phrase):
        #all attributes come from user/UI
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.secret_phrase = secret_phrase
        #except for last login which comes from logger, not user
        self.last_login = str

    def new_user():
        #can also be defined outside of class
        #should take user input
        pass
    
    def login(self):
        pass

    def change_password(self):
        pass

    def change_phrase(self):
        pass
