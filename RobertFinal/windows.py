# importing libraries
# for creating the interface window
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# import the class from another file
from player import Player

# for the visualisation of the graphs
import matplotlib.pyplot as plt

# for calculating with numpy
import numpy as np


# creating class for the window, first window
class Window(QMainWindow):
    """
    A class to create windows.

    You can set size, title, text fields, buttons to click on.
    It takes the player name and opens a new window.
    """
    # initialize it
    def __init__(self):
        """
        Constructs all the necessary attributes.
        Starts creation of window."""
        super().__init__()
        self.createWindowUI()

        # showing all the widgets
        self.show()

    # the user interface window
    def createWindowUI(self):
        """
        Creates the user interface window.
        Chosing title, design, place of text and text.
        Creates a button that leads to new function.
        """
        # setting title
        self.setWindowTitle("Stat generator")

        # setting geometry
        self.setGeometry(0,0, 200, 200)
        self.title = QLabel("Stat generator",self)
        self.title.move(50,25)
        # summoner name label
        self.snlabel = QLabel("Your player name", self)
        self.snlabel.move(10,50)
        # textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(10,75)
        self.textbox.resize(150,40)
        # Button
        self.btn1 = QPushButton('Search', self)
        self.btn1.move(30, 150)
        self.btn1.clicked.connect(self.on_search_click)

    # Button search
    def on_search_click(self):
        """
        Takes the name and creates new type of window with new class"""
        self.Player = Player(self.textbox.text())
        self.playerWindow = SummonerWindow(self.Player)
        #self.close()

# second window for the stats
class SummonerWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    # initialize it
    def __init__(self, PlayerStats):
        """
        Constructs all the necessary attributes.
        Starts creation of window.
        Different structure than first window.
        Displays all stats and has the possibility with different buttons
        to either check vizualisation of one stat of player or to
        compare with another player.

        Summoner/Player name
        Rank Solo and Flex
        Average Kills, Deaths, Assists, Wards, Minions
        Top champs
        Compare with"""
        super().__init__()
        self.PlayerStats = PlayerStats
        # setting title
        self.setWindowTitle("Summoner Stats")
        # setting geometry
        self.setGeometry(0,0, 300, 400)
        self.move(250,0)
        # summoner name
        self.playerNameLabel = QLabel("Summoner Name: ", self)
        self.playerNameLabel.move(10,10)
        self.playerNameTextbox = QLineEdit(self)
        self.playerNameTextbox.setText(self.PlayerStats.name)
        self.playerNameTextbox.move(100,8)

        # different ranks, here solo rank
        self.rankSQLabel = QLabel("Rank Solo: ", self)
        self.rankSQLabel.move(10, 30)
        self.rankSQTextbox = QLineEdit(self)
        self.rankSQTextbox.setText(str(self.PlayerStats.rank['solo']))
        self.rankSQTextbox.move(100, 28)
        # flex rank
        self.rankFQLabel = QLabel("Rank Flex: ", self)
        self.rankFQLabel.move(10, 50)
        self.rankFQTextbox = QLineEdit(self)
        self.rankFQTextbox.setText(str(self.PlayerStats.rank['flex']))
        self.rankFQTextbox.move(100, 48)

        #avg Kills with button
        self.avgKillsBtn = QPushButton("Avg Kills: ", self)
        self.avgKillsBtn.move(10, 80)
        # leads to the function showing kills in last games
        self.avgKillsBtn.clicked.connect(self.on_kills_click)
        self.avgKillsTextbox = QLineEdit(self)
        self.avgKillsTextbox.setText(str(self.PlayerStats.kda[1]))
        self.avgKillsTextbox.move(100, 78)

        #avg Deaths
        self.avgDeathsLabel = QLabel("Avg Deaths: ", self)
        self.avgDeathsLabel.move(10, 100)
        self.avgDeathsTextbox = QLineEdit(self)
        self.avgDeathsTextbox.setText(str(self.PlayerStats.kda[2]))
        self.avgDeathsTextbox.move(100, 98)

        #avg Assists
        self.avgAssistsLabel = QLabel("Avg Assists: ", self)
        self.avgAssistsLabel.move(10, 120)
        self.avgAssistsTextbox = QLineEdit(self)
        self.avgAssistsTextbox.setText(str(self.PlayerStats.kda[3]))
        self.avgAssistsTextbox.move(100, 118)

        #avg WardsPlaced
        self.avgWardsPlacedLabel = QLabel("Avg Wards Placed: ", self)
        self.avgWardsPlacedLabel.move(10, 140)
        self.avgWardsPlacedTextbox = QLineEdit(self)
        self.avgWardsPlacedTextbox.setText(str(self.PlayerStats.average_wards))
        self.avgWardsPlacedTextbox.move(100, 138)

        #avg MinionsKilled
        self.avgMinionsKilledLabel = QLabel("Avg Minions Killed: ", self)
        self.avgMinionsKilledLabel.move(10, 160)
        self.avgMinionsKilledTextbox = QLineEdit(self)
        self.avgMinionsKilledTextbox.setText(str(self.PlayerStats.average_cs))
        self.avgMinionsKilledTextbox.move(100, 158)

        # legend for top champions
        self.topChamp1Label = QLabel("Most played champs. Name[winrate, games played] ", self)
        self.topChamp1Label.move(10, 200)

        # TopChamp1
        self.topChamp1Label = QLabel("Top Champ 1: ", self)
        self.topChamp1Label.move(10, 220)
        self.topChamp1Textbox = QLineEdit(self)
        self.topChamp1Textbox.setText(str(list(self.PlayerStats.top_3_champs.keys())[0]) + str(list(self.PlayerStats.top_3_champs.values())[0]))
        self.topChamp1Textbox.move(100, 218)
        # TopChamp2
        self.topChamp2Label = QLabel("Top Champ 2: ", self)
        self.topChamp2Label.move(10, 240)
        self.topChamp2Textbox = QLineEdit(self)
        self.topChamp2Textbox.setText(str(list(self.PlayerStats.top_3_champs.keys())[1]) + str(list(self.PlayerStats.top_3_champs.values())[1]))
        self.topChamp2Textbox.move(100, 238)
        # TopChamp3
        self.topChamp3Label = QLabel("Top Champ 3: ", self)
        self.topChamp3Label.move(10, 260)
        self.topChamp3Textbox = QLineEdit(self)
        self.topChamp3Textbox.setText(str(list(self.PlayerStats.top_3_champs.keys())[2]) + str(list(self.PlayerStats.top_3_champs.values())[2]))
        self.topChamp3Textbox.move(100, 258)

        # Compare option to type in other name and leading to new window plus graph
        self.vsLabel = QLabel("Compare with ", self)
        self.vsLabel.move(10, 280)
        self.vsTextbox = QLineEdit(self)
        self.vsTextbox.move(10,300)
        self.vsBtn = QPushButton('Compare', self)
        self.vsBtn.move(10, 320)
        self.vsBtn.clicked.connect(self.on_compare_click)

        self.show()

    # function to compare players
    def on_compare_click(self):
        """
        Takes a new name and creates the same window again with other stats.
        Creates other new window that visualises the three main stats and the difference.
        Tells player what to improve"""

        # takes in the new name and uses the summonerwindow class agzin to create a second window
        self.comparePlayer = Player(self.vsTextbox.text())
        self.comparePlayerWindow = SummonerWindow(self.comparePlayer)
        self.move(250,500)

        # variables to store the stats that will be compared
        kdaPlayer1 = self.PlayerStats.kda[0]
        csPlayer1 = self.PlayerStats.average_cs
        wardsPlayer1 = self.PlayerStats.average_wards

        kdaPlayer2 = self.comparePlayer.kda[0]
        csPlayer2 = self.comparePlayer.average_cs
        wardsPlayer2 = self.comparePlayer.average_wards

        # the y values given in a list, peparing the graph
        lastGamesStatsP1DF = [kdaPlayer1, csPlayer1, wardsPlayer1]
        lastGamesStatsP2DF = [kdaPlayer2, csPlayer2, wardsPlayer2]

        # variables that store the values where the second player is much better
        askAboutKda = kdaPlayer1 < 0.75*kdaPlayer2
        askAboutCs = csPlayer1 < 0.75*csPlayer2
        askAboutWards = wardsPlayer1 < 0.75*wardsPlayer2

        # basic matplot prep
        x = np.arange(3)
        width = 0.4

        plt.bar(x - 0.2,lastGamesStatsP1DF, width)
        plt.bar(x + 0.2, lastGamesStatsP2DF, width)
        plt.xticks(x, ['kda', 'cs', 'wards'])
        plt.legend([self.PlayerStats.name, self.comparePlayer.name])

        # text about if and what could be improved of first player in comparison to second player
        title1 = 'Stats comparison \n Things you could improve on and learn from '
        title1 += str(self.comparePlayer.name) + ": \n"
        #title2 = ''
        if askAboutKda == True:
            title1 += 'kda \n'
        if askAboutCs == True:
            title1 += 'csing \n'
        if askAboutWards == True:
            title1 += 'warding'
        if askAboutCs == False and askAboutKda == False and askAboutWards == False:
            title1 += 'nothing'

        # print adjusted title
        plt.title(title1)

        plt.show()
        # space of title had to be adjusted
        plt.tight_layout()

    # button for last kills visualisation
    def on_kills_click(self):
        """
        Function for the kills button, creates graph with kills for the last 19 games.
        """

        lastKillsDF = self.PlayerStats.panda_df_last_matches['kills'].reset_index(drop=True)
        killfig, killax = plt.subplots()
        killax.plot(lastKillsDF)
        killax.set_xticks(np.arange(len(lastKillsDF)))
        killax.set_title("Kills of last Games")
        killfig.show()

