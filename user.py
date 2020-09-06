class User:
    """
    Class that generates new instances of credentials.
    """
    user_list = [] #empty credential list

    def __init__(self, account_name, user_name, password, email):

       
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email 