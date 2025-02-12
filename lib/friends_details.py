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


        if any(char for char in name if char.isalpha()):
            if self.friends_dict.get(name, False):
                raise Exception(f"{name} already exists")
            else:
                dob_datetime=self._covert_dob_to_datetime_(dob)
                self.friends_dict[name] = dob_datetime
        else:
            raise Exception('Name cannot be empty')

    def update_friend_dates(self, name: str, dob:str): 
        if self.friends_dict.get(name, False):
            dob_datetime=self._covert_dob_to_datetime_(dob)
            self.friends_dict[name]=dob_datetime
        else:
            raise Exception(f'{name} not found')


    def update_friend_name(self, old_name: str, new_name:str): 
        if self.friends_dict.get(old_name, False):
            self.friends_dict[new_name]=self.friends_dict.pop(old_name)
        else:
            raise Exception(f"{old_name} doesn't exist")
    
    def upcoming_birthdays(self):
        # Parameters:
        #   None
        # Returns:
        #   list of tupples name and dob for each item
        # Side-effects
        #   None
        
        #iterate through friend dict, and somehow filter for dobs in the next 30 days, then 

        upcoming_bdays={}        
        limit = datetime(datetime.today().year, datetime.today().month+1, datetime.today().day)
        for key, value in self.friends_dict.items():            
            next_birthday = datetime(limit.year, value.month, value.day)
            if next_birthday <= limit:
                upcoming_bdays[key]=value.strftime('%Y-%m-%d')
        return upcoming_bdays


    def upcoming_birthdays_ages(self):
        # Parameters:
        #   upcoming_birthdays_list a list of name and dob of upcoming birthdays
        # Returns:
        #   a dictionary of names and ages. Age is the age at the next bday
        #   or returns a list of strings, ["friend x will be x years old (on x date?)"]
        # Side-effects
        #   None
        age_dict={}
        bday_dict=self.upcoming_birthdays()
        for key, value in bday_dict.items():
            bday_year=self._covert_dob_to_datetime_(value).year
            age=datetime.today().year - bday_year
            age_dict[key]=age
        return age_dict
        

    def _covert_dob_to_datetime_(self, dob: str):
        try:
            return datetime.strptime(dob, '%Y-%m-%d')
        except:
            raise Exception("Date must be in format 'YYYY-MM-DD'")