XboxLeaders Python API Wrapper
===================

A simple Python wrapper for the [XboxLeaders.com Xbox API](http://www.xboxleaders.com/docs/api)


Requirements
============

* Python 2.7 (3.0 may work, but is untested) 


Installation
============

If you have pip, then:

$ pip install git+https://github.com/pzelnip/XboxLeadersAPI.git

Or alternatively just include the xboxleaders/xboxleaders.py file in your
project.


Typical Usage
=============

    >>> from xboxleaders import fetch_profile, fetch_games, fetch_achievements, fetch_friends
    >>> fetch_profile("major nelson")
    {u'AvatarBody': u'http://avatar.xboxlive.com/avatar/Major%20Nelson/avatar-body.png', u'IsCheater'.....
    >>> fetch_games('pedle zelnip')
    {u'TotalEarnedGamerScore': 210120, u'Gamertag': u'Pedle Zelnip', u'TotalPercentCompleted': 94, ..... 
    >>> fetch_achievements('major nelson', 1161890128)
    {u'Achievements': [{u'Description': u'Win one round of Tank Superiority', u'Title': u'Superiority', .....
    >>> fetch_friends('pedle zelnip')
    {u'TotalOnlineFriends': 12, u'TotalFriends': 100, u'Friends': [{u'IsOnline': False, u'PresenceInfo': .....
