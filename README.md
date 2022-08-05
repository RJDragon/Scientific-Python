Scientific python

In my past I used to play a lot of League of Legends and therefore used websites to check the meta and compare different stats. I thought it might be fun to write a similar programme using real data via API access from Riot Games (the game’s developer) and allow you to compare yourself to a friend. With the normal API key, you only have limited access to the data. I tried to get a product key which would have allowed much more requests per second, but that was not possible. So I decided to look at the last 19 ranked matches, which seemed to me to be the best mix of number of games and performance. For a casual player, this can give you an overview of the season. But if you are playing 10 games per day, you will only find how you were doing for the last two days.
The stats I chose are the ranks (for both ranked game types solo and flex), average kills, deaths, assists, kda (kill-death-assist-ratio), wards, creep score (cs) and the top champions including the number of matches and the corresponding win rate. I decided to calculate the cs-score per minute, because it has a higher significance than the general cs-score per game (which can be strongly influenced by the duration of the game). The top champs correspond to the three most played champs of the last games. There is a threshold above which the message summarising the comparison changes to indicate that there is something to learn from the other player. If one stat is 25 per cent lower than the other player’s, it is identified as something that could be improved. Besides the chart from the comparison, you can also visualise your kills over the last games. This is an additional feature I developed while working on the project.

Please make sure you have installed all the packages listed in the requirements.txt.

IMPORTANT NOTES
You need an API key and insert it in line 5 of the generals file. I will insert a new key directly before sending the project, so you may not need to create a new key depending on when you access the project. If you access the project 24 hours after my submission, you need to retrieve the key from the Riot Games website (https://developer.riotgames.com/). Log in, refresh the key, copy that API key and paste it into the code. If you do not have a Riot Games account, you can also use my old account (nickname: Siedlerdrache; password: Meister08).

How to use the program
Run the main file. A window will pop up asking you to enter your player name. For the programme to make sense, you should enter a real player name who has played ranked games this year (I will make a list of exanples in case you do not play or know players). Also, the account needs to be an EUW server account (which is usually the case; just remember that you can only analyse players on that server and that your favourite Korean player may not have a current account in Europe). The main function of the programme is then to compare yourself with another player by pressing the “compare” button. You will then get a graphical representation of the statistics and the message about what to improve. You also can check the kills of the last games of you or the compared player by using the “avg kills” button.

Remember that this programme is more of a fun programme. When you compare, a player with worse stats can still be portrayed as being much better simply by having a much higher rank with tougher opponents. The different roles also skew the results, as a support player usually places more wards than a toplaner. The stats can be affected by many factors, I have only included a few particularly significant ones into the analysis. A more detailed programme would have been too extensive for a final project.

