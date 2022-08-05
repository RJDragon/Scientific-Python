# importing needed variables
from generals import watcher
from generals import my_region


####### getting average cs score #######

# function to calculate average creep score (minions)
def get_average_cs(panda_df_last_matches, last_matches):
    """
    Calculates the stats of creep score. Need two instances as there is no data for all creeps;
    have to take in jungle monsters (neutral minions) and normal lane minions.
    Also takes in game duration to calculate average per minute.
    """
    # empty list to store cs values of the last games
    cs_lst = []
    # there are two types of creeps, typical minions on the lanes and jungle monsters, have to access both as there is no general cs score
    # they get added and then divided by minute (by dividing game length through 60)
    for match_index in range(len(last_matches)):
        x = panda_df_last_matches['gameDuration'].values[match_index]
        y = (panda_df_last_matches['totalMinionsKilled'].values[match_index])
        z = (panda_df_last_matches['neutralMinionsKilled'].values[match_index])
        cs_lst += [(z + y)/(x/60)]


    # calling function with values to return cs per minute average
    return calc_average(cs_lst)


# calculating average cs/minute score
def calc_average(lst):
    """
    Basic average calculation.
    """
    return round(sum(lst)/len(lst), 2)





####### Getting Average wards #######

# take wards of last games and get mean
def get_average_wards(panda_df_last_matches):
    """
    Gets the rounded mean for wards placed per game from the last 19 ranked matches.
    """
    return round(panda_df_last_matches['wardsPlaced'].mean(), 2)




######## Getting top 3 champs #######

# function to get the top 3 champs; most played champs in last 19 games
def get_top_3_champs(panda_df_last_matches, last_matches):
    """
    Searches through the last 19 matches, lists the champions and takes the 3 most played.
    Checks the winrate on these champions. Returns a dictionary with top 3 champs
    and the respective winrate and games played.
    """
    # store champs played
    top_3_dic = {}
    # store wins of champion played
    top_3_win_dic = {}
    # print(panda_df_last_matches)
    for i in range(3):
        win_counter = 0
        top_3_win_dic[panda_df_last_matches['championName'].value_counts().index[i]] = win_counter
        top_3_dic[panda_df_last_matches['championName'].value_counts().index[i]] = panda_df_last_matches['championName'].value_counts()[i]
        # look if the champion was played in the repective game and if so, was the match won? then increase win counter
        for match_index in range(len(last_matches)):
            if panda_df_last_matches['championName'].value_counts().index[i] == panda_df_last_matches['championName'].values[match_index]:
                if panda_df_last_matches['win'].values[match_index] == True:
                    win_counter += 1
                    top_3_win_dic[panda_df_last_matches['championName'].value_counts().index[i]] = win_counter
        # keys are the most played champs and values the winrate and the games played
        top_3_win_dic[panda_df_last_matches['championName'].value_counts().index[i]] =\
                    [round(win_counter/top_3_dic[panda_df_last_matches['championName'].value_counts().index[i]], 2),\
                    panda_df_last_matches['championName'].value_counts()[i]]



    return top_3_win_dic



###### getting kda ######


def get_kda(panda_df_last_matches):
    """
    Function taking in mean of kills, assists and deaths and calculates the kda.
    Kills plus assists divided by deaths.
    Also gives out every single stat for the summoner overview window.
    """
    kills = round(panda_df_last_matches['kills'].mean(), 2)
    deaths = round(panda_df_last_matches['deaths'].mean(), 2)
    assists = round(panda_df_last_matches['assists'].mean(), 2)
    kda = round((kills + assists) / deaths, 2)
    return [kda, kills, deaths, assists]
