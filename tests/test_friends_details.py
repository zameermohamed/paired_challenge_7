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
    date_30_days = datetime(datetime.today().year-20, datetime.today().month+1, datetime.today().day)
    date_60_days = datetime(datetime.today().year-20, datetime.today().month+1, datetime.today().day+1) 
    friends_details.add_friend("friend one", date_30_days.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    friends_details.add_friend("friend two", date_60_days.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    assert friends_details.upcoming_birthdays() == {"friend one": date_30_days.strftime('%Y-%m-%d')}


"""
initialise a new class, add 2 friend, upcoming bdays retunrs no friends as bdays after a month
"""
def test_upcoming_bday_after_2_months():
    friends_details=FriendsDetails()
    date_2_months = datetime(datetime.today().year-20, datetime.today().month+2, datetime.today().day)
    date_3_months = datetime(datetime.today().year-20, datetime.today().month+3, datetime.today().day+1) 
    friends_details.add_friend("friend one", date_2_months.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    friends_details.add_friend("friend two", date_3_months.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    assert friends_details.upcoming_birthdays() == {}


"""
initialise a new class, add 2 friend, upcoming bday ages returns age of friends with upcoming bdays

"""
def test_upcoming_bday_ages():
    friends_details=FriendsDetails()
    age_20 = datetime(datetime.today().year-20, datetime.today().month+1, datetime.today().day) #age 20
    age_30 = datetime(datetime.today().year-30, datetime.today().month, datetime.today().day+10) #age 30
    friends_details.add_friend("friend one", age_20.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    friends_details.add_friend("friend two", age_30.strftime('%Y-%m-%d')) # need to use datetime as input for dob    
    assert friends_details.upcoming_birthdays_ages() == {"friend one": 20, "friend two": 30}

"""
initialise a new class, add 2 friend, upcoming bday ages returns empty dict with no bdays within month
"""
def test_upcoming_bday_ages_invalid():
    friends_details=FriendsDetails()
    age_20 = datetime(datetime.today().year-20, datetime.today().month+2, datetime.today().day) #age 20
    age_30 = datetime(datetime.today().year-30, datetime.today().month+3, datetime.today().day+10) #age 30
    friends_details.add_friend("friend one", age_20.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    friends_details.add_friend("friend two", age_30.strftime('%Y-%m-%d')) # need to use datetime as input for dob    
    assert friends_details.upcoming_birthdays_ages() == {}

"""
initialise a new class, add 2 friend, upcoming bday ages returns only one friend + age whos bday within the next month
"""
def test_upcoming_bday_ages_one_valid_one_invalid():
    friends_details=FriendsDetails()
    age_20 = datetime(datetime.today().year-20, datetime.today().month+2, datetime.today().day) #age 20
    age_30 = datetime(datetime.today().year-30, datetime.today().month, datetime.today().day+10) #age 30
    friends_details.add_friend("friend one", age_20.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    friends_details.add_friend("friend two", age_30.strftime('%Y-%m-%d')) # need to use datetime as input for dob    
    assert friends_details.upcoming_birthdays_ages() == {"friend two": 30}


"""
Friend with birthday on current date should be included in upcoming birthdays
"""

def test_upcoming_bday_ages_today():
    friends_details=FriendsDetails()
    age_20 = datetime(datetime.today().year-25, datetime.today().month, datetime.today().day) #age 25
    friends_details.add_friend("friend one", age_20.strftime('%Y-%m-%d')) # need to use datetime as input for dob      
    assert friends_details.upcoming_birthdays_ages() == {"friend one": 25}

def test_upcoming_bday_today():
    friends_details=FriendsDetails()
    bday_2day = datetime(datetime.today().year-35, datetime.today().month, datetime.today().day)
    friends_details.add_friend("friend one", bday_2day.strftime('%Y-%m-%d')) # need to use datetime as input for dob
    assert friends_details.upcoming_birthdays() == {"friend one" : bday_2day.strftime('%Y-%m-%d')}



# ## errors and edgecases.... 



"""
Test empty string as name raises Error
"""
friends_details = FriendsDetails()
with pytest.raises(Exception) as err:
    friends_details.add_friend("", "2000-01-01")
err_msg =str(err.value)
assert err_msg == '"Name cannot be empty"'


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
