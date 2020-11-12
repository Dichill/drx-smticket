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

# from scraper import Search
# from scraper import FetchMovieResults
import scraper


scraper.Search = input("What to search? ")

# Add a try and except in order to indicate what happend and why it gave us an error.
try:
    for article in scraper.FetchMovieResults():
        for x in range(0, int(article['results'])):
            print(article['title'][x] + " | " + article['date'][x] + " | " + article['location'][x] + " | " + article['link'][x] + "\n")
except Exception as e:
    print(e)
