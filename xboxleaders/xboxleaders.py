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
    
    @raise ValueError: if gamertag is malformed (must be 1 to 15 alphanumeric 
    characters) or there was an error returned by the API
    '''
    if _valid_gamertag(gamertag):
        params = {'gamertag' : gamertag, 'region' : region}
        result = _fetch_from_api("profile", params)
        return result
    else:
        raise ValueError("%s is not a well-formed gamertag" % gamertag)


def fetch_games(gamertag, region=DEFAULT_REGION):
    '''
    Returns data pertaining to the requested gamers' played games. All game 
    data is returned except for achievements.
    
    @param gamertag: The gamertag to look up (1 to 15 alphanumeric characters)
    @type gamertag: str
    @param region: The region to return results from.
    @type region: str
    
    @raise ValueError: if gamertag is malformed (must be 1 to 15 alphanumeric 
    characters) or there was an error returned by the API
    '''
    if _valid_gamertag(gamertag):
        params = {'gamertag' : gamertag, 'region' : region}
        result = _fetch_from_api("games", params)
        return result
    else:
        raise ValueError("%s is not a well-formed gamertag" % gamertag)
    

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
    
    @raise ValueError: if gamertag is malformed (must be 1 to 15 alphanumeric 
    characters) or there was an error returned by the API
    '''
    if _valid_gamertag(gamertag):
        params = {'gamertag' : gamertag, 'titleid' : titleid, 'region' : region}
        result = _fetch_from_api("achievements", params)
        return result
    else:
        raise ValueError("%s is not a well-formed gamertag" % gamertag)


def fetch_friends(gamertag, region=DEFAULT_REGION):
    '''
    Returns all friend data for the requested gamer. Will error out if friends 
    list is private for the given gamer.
    
    @param gamertag: The gamertag to look up (1 to 15 alphanumeric characters)
    @type gamertag: str
    @param region: The region to return results from.
    @type region: str    
    
    @raise ValueError: if gamertag is malformed (must be 1 to 15 alphanumeric 
    characters) or there was an error returned by the API
    '''
    if _valid_gamertag(gamertag):
        params = {'gamertag' : gamertag, 'region' : region}
        result = _fetch_from_api("friends", params)
        return result
    else:
        raise ValueError("%s is not a well-formed gamertag" % gamertag)


def _fetch_from_api(service, params, req_type = REQ_TYPE):
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


def _valid_gamertag(gamertag):
    '''
    Return True if gamertag is a well-formed gamertag, and False otherwise. Note
    that a gamertag can be well-formed, but still not exist on XBL.
    '''
    gamer = "Z".join(gamertag.split()) # replace spaces with Z for alnum check
    return gamer.isalnum() and (1 <= len(gamer) <= 15) 

