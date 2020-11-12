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

for article in scraper.FetchMovieResults():
    for x in range(0, int(article['results'])):
        print(article['title'][x] + " | " + article['date'][x] + " | " + article['location'][x] + " | " + article['link'][x] + "\n")
