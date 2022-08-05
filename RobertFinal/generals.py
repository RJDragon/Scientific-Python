from riotwatcher import LolWatcher
import pandas as pd

# type in the api key: need a new one every day
api_key = 'RGAPI-17e3767c-f98b-43e6-bae9-631304c966eb'
# get access to api with riotwatcher library
watcher = LolWatcher(api_key)
# there are different servers. we are usually playing in euw
my_region = 'euw1'


def get_panda_df_last_matches(user_name, last_matches):
    """
    Creating dataframe with needed stats of player.
    Dives into the match details searching for the stats and first creates
    a dictionary with all players, then filters wanted player.
    """
    # list of participants in a game
    participants = []
    # accessing the needed stats for the last games
    for match in last_matches:
        match_details = watcher.match.by_id(my_region, match)
        # first of all players
        for row in match_details['info']['participants']:
            participants_row = {}
            participants_row['summonerName'] = row['summonerName']
            participants_row['championName'] = row['championName']
            participants_row['win'] = row['win']
            participants_row['kills'] = row['kills']
            participants_row['deaths'] = row['deaths']
            participants_row['assists'] = row['assists']
            participants_row['wardsPlaced'] = row['wardsPlaced']
            participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
            participants_row['neutralMinionsKilled'] = row['neutralMinionsKilled']
            participants_row['gameDuration'] = match_details['info']['gameDuration']
            participants.append(participants_row)
            df = pd.DataFrame(participants)
    # then filtering the stats of wanted player
    allSummonerStatsIndex = df['summonerName'] == user_name

    return df[allSummonerStatsIndex]




def get_puuid(summoner):
    """
    Just returns the puuid. Its a special game id needed from riot to orientate with the api access.
    """
    return summoner['puuid']

# with puuid accessing last 19 games; time is this year, so we just get the stats of this season
def get_last_matches(puuid):
    """
    With puuid accessing last 19 games; time (the long number) is beginning of this year, so we just get the stats of this season.
    """
    return watcher.match.matchlist_by_puuid(my_region, puuid, 0, 19, None, 'ranked', 1640995201)


def get_ranked_stats(summoner):
    """
    Getting general stats stored in player data, so no need to go through
    the match data for that.
    """
    return watcher.league.by_summoner(my_region, summoner['id'])


def get_summoner(user_name):
    """
    Stores name typed in.
    """
    return watcher.summoner.by_name(my_region, user_name)



def get_rank(ranked_stats):
    """
    Accessing solo and flex ranked. Displays ranks in a dictionary.
    """
    queue_type = ranked_types_played(ranked_stats)
    rank_dic = {}
    if queue_type == 'both':
        flex_rank = get_flex_rank(ranked_stats)
        solo_rank = get_solo_rank(ranked_stats)
        rank_dic = {"solo": solo_rank, "flex": flex_rank }


    elif queue_type == 'solo':
        solo_rank = get_solo_rank(ranked_stats)
        rank_dic = {"solo": solo_rank, "flex": 'no flex rank'}


    elif queue_type == 'flex':
        flex_rank = get_flex_rank(ranked_stats)
        rank_dic = {"solo": 'no solo rank', "flex": flex_rank }



    return rank_dic


def ranked_types_played(ranked_stats):
    """
    Filtering for the types of games: just ranked games of league of legends, no special mode.
    """
    is_solo = False
    is_flex = False

    for index in range(len(ranked_stats)):
        if ranked_stats[index]['queueType'] == 'RANKED_SOLO_5x5':
            is_solo = True
        if ranked_stats[index]['queueType'] == 'RANKED_FLEX_SR':
            is_flex = True
    if is_solo and is_flex:
        return 'both'
    elif is_solo:
        return 'solo'
    elif is_flex:
        return 'flex'
    else:
        return 'no rank'

# accessing solo rank
def get_solo_rank(ranked_stats):
    """
    Merging the tier and the rank to get the overall solo rank.
    """
    solo_rank = ''
    for index in range(len(ranked_stats)):
        if ranked_stats[index]['queueType'] == 'RANKED_SOLO_5x5':
            solo_rank += ranked_stats[index]['tier']
            solo_rank += " "
            solo_rank += ranked_stats[index]['rank']
    return solo_rank

# accessing flex rank
def get_flex_rank(ranked_stats):
    """
    Merging the tier and the rank to get the overall flex rank."""
    flex_rank = ''
    for index in range(len(ranked_stats)):
        if ranked_stats[index]['queueType'] == 'RANKED_FLEX_SR':
            flex_rank += ranked_stats[index]['tier']
            flex_rank += " "
            flex_rank += ranked_stats[index]['rank']
    return flex_rank

