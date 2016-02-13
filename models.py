class NewUser(object):
    """ Represents a new user """
    def __init__(self, form):
        self.name = form['name']
        self.email = form['email']
        self.password = form['password']
