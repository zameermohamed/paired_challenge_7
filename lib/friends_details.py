from datetime import datetime
# EXAMPLE

class FriendsDetails:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   creates empty dict
        self.friends_dict={}

    def all_friends(self):
        # Parameters:
        #   None
        # Returns:
        #   self.dictiory of friends
        # Side-effects
        #   None
        new_dict={}        
        for key, value in self.friends_dict.items():
            new_dict[key]= value.strftime('%Y-%m-%d')
        return new_dict

    def add_friend(self, name: str, dob: str):
        # Parameters:
        #   name: string
        #   dob: str
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend dict
        dob_datetime=self._covert_dob_to_datetime_(dob)
        self.friends_dict[name] = dob_datetime

    def update_friend_dates(self, name: str, dob:str): 
        # Parameters:
        #   name: string
        #   dob: str
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend dict
        dob_datetime=self._covert_dob_to_datetime_(dob)
        self.friends_dict[name]=dob_datetime

    def update_friend_name(self, old_name: str, new_name:str): 
        # Parameters:
        #   old_name: string
        #   new_name: str
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend dict
        self.friends_dict[new_name]=self.friends_dict.pop(old_name)

    def upcoming_birthdays(self):
        # Parameters:
        #   None
        # Returns:
        #   list of tupples name and dob for each item
        # Side-effects
        #   None
        pass # No code here yet

    def upcoming_birthdays_ages(self, upcoming_birthdays_list: list):
        # Parameters:
        #   upcoming_birthdays_list a list of name and dob of upcoming birthdays
        # Returns:
        #   a dictionary of names and ages. Age is the age at the next bday
        #   or returns a list of strings, ["friend x will be x years old (on x date?)"]
        # Side-effects
        #   None
        pass # No code here yet

    def _covert_dob_to_datetime_(self, dob: str):
        # Parameters:
        #   dob in string format ('2012-05-01')
        # Returns:
        #   a datetime object
        # Side-effects
        #   None
        try:
            return datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in format 'YYYY-MM-DD'")