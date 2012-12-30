'''
Unit tests for the xboxleaders module

Created on Dec 26, 2012

@author: aparkin
'''
from unittest import TestCase

from xboxleaders import fetch_achievements, fetch_friends, fetch_games, \
    fetch_profile


# Valid (well-formed and active) values for testing
VALID_GAMERTAG = "major nelson" # I don't think he'll get banned anytime soon. :)
VALID_GAME_ID = 1161890128 # Battlefield 3

# Invalid (malformed) values for testing
INVALID_GAMERTAG = '''this is not a valid gamertag because it is way 
                toooooooooooooo long!!!!!!!'''
INVALID_GAME_ID = 2222  # too short

# if anyone ever takes this gamertag, these tests will break. :(
VALID_BUT_NOT_ON_XBL_GAMERTAG = "KIJHBVQWSS88GD" 


class TestFetchProfile(TestCase):
    '''
    Unit tests for the fetch_profile function
    '''                        
    def test_malformed_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_profile, INVALID_GAMERTAG)
        
    def test_empty_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_profile, "")
        
    def test_nonexistant_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_profile, 
                          VALID_BUT_NOT_ON_XBL_GAMERTAG)
        
    def test_result_seems_valid(self):
        '''
        Rough test to see that result returned contains valid data
        '''
        # Arrange: we cannot compare values, as they will change over time, so
        # instead just look for the expected keys in the result.
        expected_keys = {"Tier", "IsValid", "IsCheater", "IsOnline", 
                         "OnlineStatus", "XBLLaunchTeam", "NXELaunchTeam",
                         "KinectLaunchTeam", "AvatarTile", "AvatarSmall",
                         "AvatarLarge", "AvatarBody", "AvatarTileSSL",
                         "AvatarSmallSSL", "AvatarLargeSSL", "AvatarBodySSL",
                         "Gamertag", "GamerScore", "Reputation", "Name", 
                         "Motto", "Location", "Bio"}
        
        # Act
        result = fetch_profile(VALID_GAMERTAG)
        result_keys = set(result.keys())
        
        # Assert
        self.assertTrue(expected_keys.issubset(result_keys))


class TestFetchGames(TestCase):
    '''
    Unit tests for the fetch_games function
    '''                        
    def test_malformed_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_games, INVALID_GAMERTAG)

    def test_empty_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_games, "")
        
    def test_nonexistant_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_games, 
                          VALID_BUT_NOT_ON_XBL_GAMERTAG)
        
    def test_result_seems_valid(self):
        '''
        Rough test to see that result returned contains valid data
        '''
        # Arrange: we cannot compare values, as they will change over time, so
        # instead just look for the expected keys in the result.
        expected_keys = {"Gamertag", "Gamerpic", "GameCount", 
                         "TotalEarnedGamerScore", "TotalPossibleGamerScore", 
                         "TotalEarnedAchievements", "TotalPossibleAchievements",
                         "TotalPercentCompleted", "PlayedGames"}
        expected_game_keys = {"Id", "Title", "Url", "BoxArt", "LargeBoxArt",
                              "EarnedGamerScore", "PossibleGamerScore",
                              "EarnedAchievements", "PossibleAchievements",
                              "PercentageCompleted", "LastPlayed"}                         
        
        # Act
        result = fetch_games(VALID_GAMERTAG)
        result_keys = set(result.keys())
        # note that the next line assumes at least 1 game played
        result_game_keys = set(result['PlayedGames'][0].keys())
        
        # Assert
        self.assertTrue(expected_keys.issubset(result_keys))
        self.assertTrue(expected_game_keys.issubset(result_game_keys))


class TestFetchAchievements(TestCase):
    '''
    Unit tests for the fetch_achievements function
    '''                        
    def test_malformed_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_achievements, 
                          INVALID_GAMERTAG, VALID_GAME_ID)

    def test_empty_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_achievements, "", VALID_GAME_ID)
        
    def test_nonexistant_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_achievements, 
                          VALID_BUT_NOT_ON_XBL_GAMERTAG, VALID_GAME_ID)

    def test_result_seems_valid(self):
        '''
        Rough test to see that result returned contains valid data
        '''
        # Arrange: we cannot compare values, as they will change over time, so
        # instead just look for the expected keys in the result.
        expected_keys = {'Title', 'Url', 'EarnedGamerScore', 'BoxArt', 
                         'PossibleGamerScore', 'EarnedAchievements', 
                         'Achievements', 'LastPlayed', 'Id', 'LargeBoxArt', 
                         'PossibleAchievements'}                   
        expected_ach_keys = {'DateEarned', 'EarnedOffline', 'IsSecret', 
                             'Description', 'Title', 'TileUrl', 'Unlocked', 
                             'GamerScore', 'Id'}
                
        # Act
        result = fetch_achievements(VALID_GAMERTAG, VALID_GAME_ID)
        result_keys = set(result.keys())
        result_ach_keys = set(result['Achievements'][0].keys())
        
        # Assert
        self.assertTrue(expected_keys.issubset(result_keys))
        self.assertTrue(expected_ach_keys.issubset(result_ach_keys))


class TestFetchFriends(TestCase):
    '''
    Unit tests for the fetch_friends function
    '''                        
    def test_malformed_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_friends, INVALID_GAMERTAG)

    def test_empty_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_friends, "")
        
    def test_nonexistant_gamertag_raises_valueerror(self):
        self.assertRaises(ValueError, fetch_friends, 
                          VALID_BUT_NOT_ON_XBL_GAMERTAG)

    def test_result_seems_valid(self):
        '''
        Rough test to see that result returned contains valid data
        '''
        # Arrange: we cannot compare values, as they will change over time, so
        # instead just look for the expected keys in the result.
        expected_keys = {'TotalOnlineFriends', 'TotalFriends', 'Friends', 
                         'TotalOfflineFriends'}                   
        expected_friend_keys = {'IsOnline', 'PresenceInfo', 'Gamertag', 
                                'AvatarSmall', 'GamerScore', 'AvatarLarge'}
        expected_presence_keys = {'OnlineStatus', 'Game', 'LastOnline'}
        expected_game_presence_keys = {"Title", "Id", "Url"}
                
        # Act
        result = fetch_friends(VALID_GAMERTAG)
        result_keys = set(result.keys())
        result_friend_keys = set(result['Friends'][0].keys())
        result_presence_keys = set(result['Friends'][0]['PresenceInfo'].keys())
        result_game_presence_keys = set(result['Friends'][0]['PresenceInfo']['Game'].keys())
        
        # Assert
        self.assertTrue(expected_keys.issubset(result_keys))
        self.assertTrue(expected_friend_keys.issubset(result_friend_keys))
        self.assertTrue(expected_presence_keys.issubset(result_presence_keys))
        self.assertTrue(expected_game_presence_keys.issubset(result_game_presence_keys))
