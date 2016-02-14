class NewUser(object):
    """ Represents a new user """
    def __init__(self, form):
        self.name = form['name']
        self.email = form['email']
        self.password = form['password']

class LoginUser(object):
    """ Represents a login user """
    def __init__(self, form):
        self.email = form['email']
        self.password = form['password']
