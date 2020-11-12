#================================#
#                                #
#   ________       ____  ___     #
#   \______ \______\   \/  /     #
#    |    |  \_  __ \     /      #
#    |    `   \  | \/     \      #
#   /_______  /__| /___/\  \     #
#           \/           \_/     #
#                                #
#       Made by Dichill          #
#                                #
#================================#

#=========================================================================#
#         _________                    .___.__  __                        #
#          \_   ___ \_______   ____   __| _/|__|/  |_  ______             #
#          /    \  \/\_  __ \_/ __ \ / __ | |  \   __\/  ___/             #
#          \     \____|  | \/\  ___// /_/ | |  ||  |  \___ \              #
#           \______  /|__|    \___  >____ | |__||__| /____  >             #
#                  \/             \/     \/               \/              #
#                                                                         #
# Some Useful Articles that were very helpful during my research for bs4  #
#=========================================================================#

# from scraper import Search
# from scraper import FetchMovieResults
import scraper


scraper.Search = input("What to search? ")

for article in scraper.FetchMovieResults():
    for x in range(0, int(article['results'])):
        print(article['title'][x] + " | " + article['date'][x] + " | " + article['location'][x] + " | " + article['link'][x] + "\n")
