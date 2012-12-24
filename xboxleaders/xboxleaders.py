'''
A simple Python wrapper for the XboxLeaders.com Xbox API By Jason Clemons.

@author: aparkin
@see: http://www.xboxleaders.com/docs/api/
'''
from urllib import urlencode
import urllib2
import json


API_BASE_URL = "http://www.xboxleaders.com/api/"

DEFAULT_REGION = "en-US"
REQ_TYPE = "json"  # reportedly can be json, xml, or php


def fetch_profile(gamertag, region=DEFAULT_REGION):
    '''
    Returns data pertaining to the requested gamers' profile on Xbox LIVE.
    
    @param gamertag: The gamertag to look up (1 to 15 alphanumeric characters)
    @type gamertag: str
    @param region: The region to return results from.
    @type region: str
    '''
    params = {'gamertag' : gamertag, 'region' : region}
    result = __fetch_from_api("profile", params)
    return result


def fetch_games(gamertag, region=DEFAULT_REGION):
    '''
    Returns data pertaining to the requested gamers' played games. All game 
    data is returned except for achievements.
    
    @param gamertag: The gamertag to look up (1 to 15 alphanumeric characters)
    @type gamertag: str
    @param region: The region to return results from.
    @type region: str
    '''
    params = {'gamertag' : gamertag, 'region' : region}
    result = __fetch_from_api("games", params)
    return result


def fetch_achievements(gamertag, titleid, region=DEFAULT_REGION):
    '''
    This method will return all achievement information for the requested gamer 
    and game

    @param gamertag: The gamertag to look up (1 to 15 alphanumeric characters)
    @type gamertag: str
    @param titleid: The unique title id for the requested game (see the return
        value from fetch_games() for title id's).
    @type titleid: int
    @param region: The region to return results from.
    @type region: str
    '''
    params = {'gamertag' : gamertag, 'titleid' : titleid, 'region' : region}
    result = __fetch_from_api("achievements", params)
    return result


def fetch_friends(gamertag, region=DEFAULT_REGION):
    '''
    Returns all friend data for the requested gamer. Will error out if friends 
    list is private for the given gamer.
    
    @param gamertag: The gamertag to look up (1 to 15 alphanumeric characters)
    @type gamertag: str
    @param region: The region to return results from.
    @type region: str    
    '''
    params = {'gamertag' : gamertag, 'region' : region}
    result = __fetch_from_api("friends", params)
    return result


def __fetch_from_api(service, params, req_type = REQ_TYPE):
    '''
    Fetch the appropriate result from the public API & return the result as a
    Python structure.
    
    @raise ValueError: if the API returned an error
    '''
    url = "%s%s.%s?%s" % (API_BASE_URL, service, req_type, urlencode(params))
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, timeout=60)
    jsonstr = response.read()
    result = json.loads(jsonstr)
    
    # if error executing request...
    if result.get('error', None):
        raise ValueError(result['error'].get('message', "Unknown error"), 
                         result['error'].get('code', "Unknown errorcode"))
        
    # some responses produce errors in a slightly different format
    elif result.get('Error', None):
        raise ValueError(result['Error'], 200)
    
    else:
        return result['Data']


if __name__ == "__main__":
    print(fetch_profile("pedle zelnip")['IsCheater'])
    try:
        print(fetch_profile("pedle zelnipfdsa"))
    except ValueError as e:
        (msg, code) = e.args
        print(msg)
        print(code)
    print("-------------------")

    print(fetch_games("pedle zelnip")['GameCount'])
    try:
        print(fetch_games("pedle zelnipfdsa"))
    except ValueError as e:
        (msg, code) = e.args
        print(msg)
        print(code)
    print("-------------------")

    print(fetch_achievements("pedle zelnip", 1096157387)['Title'])
    try:
        print(fetch_achievements("pedle zelnipfdsa", 1096157387))
    except ValueError as e:
        (msg, code) = e.args
        print(msg)
        print(code)
    print("-------------------")

    print(fetch_friends("major nelson")['Friends'])
    try:
        print(fetch_friends("pedle zelnipfdsa"))
    except ValueError as e:
        (msg, code) = e.args
        print(msg)
        print(code)
    print("-------------------")
