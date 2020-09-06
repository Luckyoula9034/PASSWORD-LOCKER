class User:
    """
    Class that generates new instances of credentials.
    """
    user_list = [] #empty credential list

    def __init__(self, account_name, user_name, password, email):
        # instace variables are viriables that are unique to each new instance of the class
       
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email 

    def  save_user(self):
        '''
        save_credential method saves credential objects into credential_list

        '''
        User.user_list.append(self)
        
    def delete_user(self):   
        
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self) 
