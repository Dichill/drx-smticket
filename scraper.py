
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

# Articles
# https://stackoverflow.com/questions/9061094/extract-element-with-no-class-attribute
# https://stackoverflow.com/questions/52905578/extracting-elements-without-class-or-id-using-beautifulsoup/52907043
# https://stackoverflow.com/questions/36165854/beautifulsoup-scraping-information-from-multiple-divs-using-loops-into-json
# https://stackoverflow.com/questions/62740766/how-to-select-specific-div-using-beautifulsoup-when-multiple-divs-have-the-same
# and a lot more! Just do a handful of google search and there's a lot of topics that revolves around BS4

# Documentation
# https://www.crummy.com/software/BeautifulSoup/doc
# https://tedboy.github.io/bs4_doc/
# https://www.kite.com/python/docs/bs4.BeautifulSoup

from bs4 import BeautifulSoup
import requests

# Urls
url = 'https://smtickets.com/' # Main Domain of the SM Website
searchurl = 'https://smtickets.com/events/search/' # Search URL

# Example of what to search. This will be used on Django sooner or later.
Search = "Demon Slayer"


# This is where the magic begins
def StartScrape():
    # We want to make Search global so that we have access to it.
    global Search

    # We want to replace whitespace with %20 since. -------  "which indicates space in website."
    Search = Search.replace(" ", "%20") # Replace spaces with %20 which indicates space in web.
    
    # Movie Data | In this part we want to store the data that we have scraped. And the reason why we have set() is to remove
    #              Duplicates that are going to be stored later on.
    
    movie_title = set()
    movie_date = set()
    movie_location = set()
    movie_link = set()

    # Move Result | This is where the final results comes in. It is stored here to be returned at the Django to pass information about
    #               The data that we have scraped.

    movie_result = []

    # We want to make sure that our code is executing properly and we want to know which step it is to know where it stopped and
    # What happened at that certain line.

    # Combine the Search Url (https://smtickets.com/events/search/) with the user what wishes to search on our website inorder to
    # Scrape it.
    print("[DrX] Link: " + searchurl + Search)
    r = requests.get(searchurl + Search)

    # This is the part where we are gonna get the source code of the website.
    soup = BeautifulSoup(r.content, features="lxml")
    print("[DrX] Scraping ./.")

    # We want to find the div that holds the search-results so we can get information from that.
    try:
        containers = soup.find_all("div", {"class":"c-list page-search-results"})
        for container in containers:
            wrappers = container.find_all("div")
            for wrapper in wrappers:
                # Cannot Find
                result = wrapper.find_all("ul", {"class":"c-list__items c-list__items--option-5"})
                for x in result:
                    li = x.find("li")
                    for l in li:

                        #title = li.find('div') ~ NA
                        #data.add(article.text) ~ NA

                        # Title - Gets the title of the Movie
                        article = li.find_all('div', {"class":""})
                        movie_title.add(article[0].text)

                        # Location - Where is it happening and etc.
                        location = article[2].text
                        movie_location.add(location)

                        # Date - Gets the date of the movie
                        date = li.find("span", {"class":"o-date"})
                        movie_date.add(date.text)

                        # Link - Use for scraping that new link

    except Exception:
        print(Exception + " If the bug persist please issue a github report regarding the issue.")

    # We're going to make a data where the results of our scraping are gonna be stored to.
    # The reason why we have to put 'list(object)' is to make it into a list inorder for it to append to our movie_result list.
    data = {
        'title': list(movie_title),
        'location': list(movie_location),
        'date': list(movie_date)
    }

    # Now we give the data to the movie_result
    movie_result.append(data)
    print("[DrX] Finished Appending")

    # Returns the movie_result so that we can use StartScrape from any other python scripts as long as it is imported.
    return movie_result
                        
    #for x in range(len(list(data))):
    #    movie_result.append(list(data)[x])

# =======================================================================================================#
#                                                                                                        #
#                      ___________                             .__                                       #
#                      \_   _____/__  ________    _____ ______ |  |   ____   ______                      #
#                       |    __)_\  \/  /\__  \  /     \\____ \|  | _/ __ \ /  ___/                      #
#                       |        \>    <  / __ \|  Y Y  \  |_> >  |_\  ___/ \___ \                       #
#                      /_______  /__/\_ \(____  /__|_|  /   __/|____/\___  >____  >                      #
#                              \/      \/     \/      \/|__|             \/     \/                       #
#                                                                                                        #
#                                                                                                        #
# =======================================================================================================#

# =======================================================================================================#
# OLD METHOD EXAMPLES
#
# Some Examples that worked with my previous method but now works with a new method that I came up with.
#
#print(GetTitle()[0]) # Specific number of what title via number 
#print(GetTitle()) # Get the list 
#
# Get all Results
#for x in range(len(GetTitle())):
#    print(GetTitle()[x])
#
# =======================================================================================================#

# =======================================================================================================#
# NEW METHOD EXAMPLES

# Gets only the "title" in a list
#for article in StartScrape():
#    print(article['title'])

# Gets only the "location" in a list
#for article in StartScrape():
#    print(article['location'])

# Gets only the "date" in a list
#for article in StartScrape():
#    print(article['date'])

# Gets all the list of search results.
for article in StartScrape():
    print(article)
#
# =======================================================================================================#