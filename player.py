# importing needed files
import generals
import specifics

# creating class for the player, separated into general and specific infos
class Player:
    """
    A class to represent a Player.

    ...

    Attributes
    ----------
    name : player name
    puuid : special game id
    ranked stats: general stats
    rank: rank
    last matches: last 19 matches, this year
    creep score: average per minute cs score
    wards: avg wards per game
    top 3 champs: most played champs last 19 games
    kda: average kill-death-assist ratio

    """
    # initialize it
    def __init__(self, user_name):
        # stores name and stats you can find directly
        self.name = generals.get_summoner(user_name)['name'] # summoner name, check if summoner exist?
        self.summoner = generals.get_summoner(self.name) # api summoner info, outsource?,
        self.puuid = generals.get_puuid(self.summoner)
        self.ranked_stats = generals.get_ranked_stats(self.summoner) # api ranked_stats, outsource?
        self.rank = generals.get_rank(self.ranked_stats) # {solo: , flex: }
        self.last_matches = generals.get_last_matches(self.puuid) # list of last (<=20) matches

        self.panda_df_last_matches = generals.get_panda_df_last_matches(self.name, self.last_matches)

        # stats you have to calculate
        self.average_cs = specifics.get_average_cs(self.panda_df_last_matches, self.last_matches) # check cs average, helpfunction done (?) :)
        self.average_wards = specifics.get_average_wards(self.panda_df_last_matches) # done :)
        self.top_3_champs = specifics.get_top_3_champs(self.panda_df_last_matches, self.last_matches) # done
        self.kda = specifics.get_kda(self.panda_df_last_matches) # done
