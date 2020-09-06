class User:
    """
    Class that generates new instances of credentials.
    """
    user_list = [] #empty credential list

    def __init__(self, account_name, user_name, password, email):
        