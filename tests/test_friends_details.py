from lib.friends_details import FriendsDetails
from datetime import datetime
import pytest
# EXAMPLE

"""
initialise an instance of FriendsDetails()
"""
def test_initialise_instance_of_friends_data():
    friends_details=FriendsDetails()
    assert isinstance(friends_details, FriendsDetails)


"""
initialise an empty dict, all_friends returns empty dictionary
"""
def test_return_empty_dict():
    friends_details=FriendsDetails()
    assert friends_details.all_friends() == {}


"""
initialise a friend_details class, check convert_dob_to_datime methods, converts string to datetime
"""
def test_convert_datetime_method_works():
    friends_details=FriendsDetails()
    result = friends_details._covert_dob_to_datetime_('2000-01-01')
    assert isinstance(result, datetime)


"""
initialise a friend_details class, check convert_dob_to_datime method raises error eith invalid date
"""
def test_convert_datetime_method_error():
    friends_details=FriendsDetails()
    with pytest.raises(Exception) as e:
        result = friends_details._covert_dob_to_datetime_('01-01-2000')
    error_message=str(e.value)
    assert error_message == "Date must be in format 'YYYY-MM-DD'"


"""
initialise a new class, add friend, all_friends returns whats been added
"""

def test_all_friends_returns_whats_been_added():
    friends_details=FriendsDetails()
    friends_details.add_friend("friend one", "2000-01-01")
    assert friends_details.all_friends() == {"friend one": "2000-01-01"}



"""
initialise a new class, add two friend, all_friends returns whats been added
"""
def test_add_two_friends_and_all_friends_returns_correct():
    friends_details=FriendsDetails()
    friends_details.add_friend("friend one", "2000-01-01")
    friends_details.add_friend("friend two", "2001-12-25")
    assert friends_details.all_friends() == {"friend one": "2000-01-01", "friend two": "2001-12-25"}


"""
initialise a new class, add friend, ,update friend dob, all_friends returns whats been updated
"""
def test_update_dob():
    friends_details=FriendsDetails()
    friends_details.add_friend("friend one", "2000-01-01")
    friends_details.update_friend_dates("friend one", "1999-02-03")
    assert friends_details.all_friends() == {"friend one":"1999-02-03"}

"""
initialise a new class, add friend, ,update friend name, all_friends returns whats been updated
"""
def test_update_friend_name():
    friends_details=FriendsDetails()
    friends_details.add_friend("friend one", "2000-01-01")
    friends_details.update_friend_name("friend one", "friend two")
    assert friends_details.all_friends() == {"friend two":"2000-01-01"}


"""
initialise a new class, add 2 friend, upcoming bdays reutnrs only the friend whos bday in within next month
"""
def test_upcoming_bday():
    friends_details=FriendsDetails()
    
    friends_details.add_friend("friend one", "2000-03-01") # need to use datetime as input for dob
    friends_details.add_friend("friend two", "2000-04-01") # need to use datetime as input for dob
    assert friends_details.upcoming_birthdays() == {"friend one", "2000-03-01"}


# """
# initialise a new class, add 2 friend, upcoming bdays retunrs no friends as bdays after a month
# """
# friends_details=FriendsDetails()
# friends_details.add_friend("friend one", "2000-05-01") # need to use datetime as input for dob
# friends_details.add_friend("friend two", "2000-04-01") # need to use datetime as input for dob
# assert friends_details.upcoming_birthdays() == {} # could be string or empyt dictionry?


# """
# initialise a new class, add 2 friend, upcoming bday ages returns age of friends with upcoming bdays
# """
# friends_details=FriendsDetails()
# friends_details.add_friend("friend one", "2000-03-01") # need to use datetime as input for dob
# assert friends_details.upcoming_birthdays_ages() == {"friend one": 25}

# """
# initialise a new class, add 2 friend, upcoming bday ages returns empty dict with no bdays within month
# """
# friends_details=FriendsDetails()
# friends_details.add_friend("friend one", "2000-05-01") # need to use datetime as input for dob
# friends_details.add_friend("friend two", "2000-04-01") # need to use datetime as input for dob
# assert friends_details.upcoming_birthdays_ages() == {}

# """
# initialise a new class, add 2 friend, upcoming bday ages returns only one friend + age whos bday within the next month
# """
# friends_details=FriendsDetails()
# friends_details.add_friend("friend one", "2000-05-01") # need to use datetime as input for dob
# friends_details.add_friend("friend two", "2010-03-01") # need to use datetime as input for dob
# assert friends_details.upcoming_birthdays_ages() == {"friend two": 15}

# """
# Friend with birthday on current date should be included in upcoming birthdays
# """



# ## errors and edgecases.... 



# """
# Test empty string as name raises Error
# """
# friends_details = FriendsDetails()
# with pytest.raises(Exception) as err:
#     friends_details.add_friend("", "2000-01-01")
# err_msg =str(err.value)
# assert err_msg == '"Name cannot be empty"'


# """
# Test whitespace-only string as name raises Error
# """
# friends_details = FriendsDetails()
# with pytest.raises(Exception) as err:
#     friends_details.add_friend(" ", "2000-01-01")
# err_msg =str(err.value)
# assert err_msg == '"Name cannot be empty"'

# """
# Adding friend with invalid date format raises Error
# """

# friends_details = FriendsDetails()
# with pytest.raises(Exception) as err:
#     friends_details.add_friend("friend one", "01/01/2000")
# err_msg = str(err.value)
# assert err_msg == "Date must be in format 'YYYY-MM-DD'"

# """
# Adding friend with invalid date (e.g., February 01 2000) raises Error
# """

# friends_details = FriendsDetails()
# with pytest.raises(Exception) as err:
#     friends_details.add_friend("friend one", "February 01 2000")
# err_msg = str(err.value)
# assert err_msg == "Date must be in format 'YYYY-MM-DD'"

# """
# Adding friend with duplicate (name and dob) raises Error (duplicate)
# """

# friends_details = FriendsDetails()
# friends_details.add_friend("friend one", "2000-01-01")
# with pytest.raises(Exception) as err:
#     friends_details.add_friend("friend one", "2000-01-01")
# err_msg = str(value.err) 
# assert err_msg == 'friend one already exists'

# """
# Trying to Update name on non existent friend raises Error
# """
# friends_details = FriendsDetails()
# with pytest.raises(Exception) as err:
#     friends_details.update_friend_name("non-existent", "new name")
# err_msg = str(value.err)
# assert err_msg == 'non-existent not found'

# """
# Trying to Update dob on non existent friend raises Error
# """

# friends_details = FriendsDetails()
# with pytest.raises(Exception) as err:
#     friends_details.update_friend_dates("non-existent", "2000-01-01")
# err_msg = str(value.err)
# assert err_msg == 'non-existent not found'
