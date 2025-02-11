# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class FriendsDetails:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   creates empty dict
        pass

     def all_friends(self):
        # Parameters:
        #   None
        # Returns:
        #   self.dictiory of friends
        # Side-effects
        #   None
        pass # No code here yet

    def add_friend(self, name: str, dob: str):
        # Parameters:
        #   name: string
        #   dob: str
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend dict
        pass # No code here yet

    def update_friend_dates(self, name: str, dob:str:): 
        # Parameters:
        #   name: string
        #   dob: str
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend dict
        pass # No code here yet

    def update_friend_name(self, old_name: str, new_name:str:): 
        # Parameters:
        #   old_name: string
        #   new_name: str
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend dict
        pass # No code here yet

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
        pass # No code here yet

        # will need to import datetime from datetime and timedelta
        # try:
        #     return datetime.strptime(dob, '%Y-%m-%d')
        # except ValueError:
        #     raise ValueError("Date must be in format 'YYYY-MM-DD'")
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
initialise an instance of FriendsDetails()
"""
friends_details=FriendsDetails()
assert isinstance(friends_details, FriendsDetails)


"""
initialise an empty dict, all_friends returns empty dictionary
"""
friends_details=FriendsDetails()
assert friends_details.all_friends() == {}


"""
initialise a friend_details class, check convert_dob_to_datime methods, converts string to datetime
"""
friends_details=FriendsDetails()
result = friends_details._covert_dob_to_datetime_('2000-01-01')
assert isistance(result, datetime) #???


"""
initialise a new class, add friend, all_friends returns whats been added
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-01-01")
assert friends_details.all_friends() == {"friend one": "2000-01-01"}

"""
initialise a new class, add two friend, all_friends returns whats been added
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-01-01")
friends_details.add_friend("friend two", "2001-12-25")
assert friends_details.all_friends() == {"friend one": "2000-01-01", "friend two": "2001-12-25"}


"""
initialise a new class, add friend, ,update friend dob, all_friends returns whats been updated
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-01-01")
friends_details.update_friend_dates("friend one", "1999-02-03")
assert friends_details.all_friends() == {"friend one":"1999-02-03"}

"""
initialise a new class, add friend, ,update friend name, all_friends returns whats been updated
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-01-01")
friends_details.update_friend_name("friend one", "friend two")
assert friends_details.all_friends() == {"friend two":"2000-01-01"}


"""
initialise a new class, add 2 friend, upcoming bdays reutnrs only the friend whos bday in within next month
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-03-01") # need to use datetime as input for dob
friends_details.add_friend("friend two", "2000-04-01") # need to use datetime as input for dob
assert friends_details.upcoming_birthdays() == {"friend one", "2000-03-01"}


"""
initialise a new class, add 2 friend, upcoming bdays retunrs no friends as bdays after a month
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-05-01") # need to use datetime as input for dob
friends_details.add_friend("friend two", "2000-04-01") # need to use datetime as input for dob
assert friends_details.upcoming_birthdays() == {} # could be string or empyt dictionry?


"""
initialise a new class, add 2 friend, upcoming bday ages returns age of friends with upcoming bdays
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-03-01") # need to use datetime as input for dob
assert friends_details.upcoming_birthdays_ages() == {"friend one": 25}

"""
initialise a new class, add 2 friend, upcoming bday ages returns empty dict with no bdays within month
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-05-01") # need to use datetime as input for dob
friends_details.add_friend("friend two", "2000-04-01") # need to use datetime as input for dob
assert friends_details.upcoming_birthdays_ages() == {}

"""
initialise a new class, add 2 friend, upcoming bday ages returns only one friend + age whos bday within the next month
"""
friends_details=FriendsDetails()
friends_details.add_friend("friend one", "2000-05-01") # need to use datetime as input for dob
friends_details.add_friend("friend two", "2010-03-01") # need to use datetime as input for dob
assert friends_details.upcoming_birthdays_ages() == {"friend two": 15}

"""
Friend with birthday on current date should be included in upcoming birthdays
"""



## errors and edgecases.... 



"""
Test empty string as name raises Error
"""
friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.add_friend("", "2000-01-01")
err_msg =str(err.value)
assert err_msg == '"Name cannot be empty"'


"""
Test whitespace-only string as name raises Error
"""
friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.add_friend(" ", "2000-01-01")
err_msg =str(err.value)
assert err_msg == '"Name cannot be empty"'

"""
Adding friend with invalid date format raises Error
"""

friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.add_friend("friend one", "01/01/2000")
err_msg = str(err.value)
assert err_msg == "Date must be in format 'YYYY-MM-DD'"

"""
Adding friend with invalid date (e.g., February 01 2000) raises Error
"""

friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.add_friend("friend one", "February 01 2000")
err_msg = str(err.value)
assert err_msg == "Date must be in format 'YYYY-MM-DD'"

"""
Adding friend with duplicate (name and dob) raises Error (duplicate)
"""

friends_details = FriendsDetails()
friends_details.add_friend("friend one", "2000-01-01")
with pytest.raises(Exception) as err:
    friends_details.add_friend("friend one", "2000-01-01")
err_msg = str(value.err) 
assert err_msg == 'friend one already exists'

"""
Trying to Update name on non existent friend raises Error
"""
friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.update_friend_name("non-existent", "new name")
err_msg = str(value.err)
assert err_msg == 'non-existent not found'

"""
Trying to Update dob on non existent friend raises Error
"""

friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.update_friend_dates("non-existent", "2000-01-01")
err_msg = str(value.err)
assert err_msg == 'non-existent not found'

```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
