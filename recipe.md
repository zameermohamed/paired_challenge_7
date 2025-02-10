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
        #   a list containing tuple of names and ages
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
# assert friends_details.all_friends() == {}
assert friends_details.all_friends() == {}


```




_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
