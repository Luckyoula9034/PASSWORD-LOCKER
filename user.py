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
        delete_credential method deletes a saved credential from the credential_list
        '''

        User.user_list.remove(self) 

    @classmethod
    def find_by_name(cls, name):
         '''
        Method that takes in a name and returns a credential that matches that name.

        Args:
            name: user name to search for
        Returns :
            Credential of person that matches the name.
        '''
         for user in cls.user_list:
            if user.user_name == name:
                return True
            #cls does not allows the entire class to pass when the method is called
            return False
    
    @classmethod
    def user_exist(cls, name):
        '''
          Method that checks if a credential exists from the credential list.
        Args:
              name: user name to search if it exists
        Returns :
              Boolean: True or false depending if the credential exists
        '''
        for user in cls.user_list:
            if user.password == name:
                return True

            return False        