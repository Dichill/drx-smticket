
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
# https://stackoverflow.com/questions/57013133/how-to-extract-the-on-click-value/57013342
# https://stackoverflow.com/questions/39289206/how-to-get-href-link-from-onclick-function-in-python
# https://stackoverflow.com/questions/58443772/get-url-from-onclick-attribute-of-a-tag-python
# https://stackoverflow.com/questions/55056003/beautiful-soup-get-data-inside-a-button-tag
# and a lot more! Just do a handful of google search and there's a lot of topics that revolves around BS4

# Documentation
# https://www.crummy.com/software/BeautifulSoup/doc
# https://tedboy.github.io/bs4_doc/
# https://www.kite.com/python/docs/bs4.BeautifulSoup

# Important!
IsDebugging = True

# Store the Error Message
ErrorMessage = set()
IsError = False


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import requests
import time
import json


# Urls
url = 'https://smtickets.com/' # Main Domain of the SM Website
searchurl = url + 'events/search/' # Search URL

# Login Credentials
login_route = 'users/login'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

# Example of what to search. This will be used on Django sooner or later.
Search = input("Title of Movie: ")
Username = "DichillTomarong" #input("Username: ")
Password = "dichill1212" #input("Password: ")

# This is where the magic begins
def FetchMovieResults():
    # We want to make Search global so that we have access to it.
    global ErrorMessage
    global Search

    # We want to replace whitespace with %20 since. -------  "which indicates space in website."
    Search = Search.replace(" ", "%20") # Replace spaces with %20 which indicates space in web.
    
    # Movie Data | In this part we want to store the data that we have scraped. And the reason why we have set() is to remove
    #              Duplicates that are going to be stored later on.
    
    movie_title = []
    movie_date = []
    movie_location = []
    movie_link = []

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
    soup = bs4(r.content, "html5lib")
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
                    
                    #title = li.find('div') ~ NA
                    #data.add(article.text) ~ NA

                    # Title - Gets the title of the Movie
                    article = li.find_all('div', {"class":""})
                    movie_title.append(article[0].text)

                    # Location - Where is it happening and etc.
                    location = article[2].text
                    movie_location.append(location)

                    # Date - Gets the date of the movie
                    date = li.find("span", {"class":"o-date"})
                    #movie_date.add(date.text)
                    movie_date.append(date.text)

                    # Link - Use for scraping the links
                    #button = li.find_all("button", {"class":"o-button o-button--green o-button--green-small"}).attrs['onclick']

                    # Theres a lot of buttons but we have to make sure that one of them contains a http.
                    for bttn in li.select('button[onclick*="http"]'):
                        # Now we fetch the data from 'onclick' in our bttn and it will retrieve the link.
                        movie_link.append(bttn['onclick'].split("'")[1])
                    IsError = False

    except Exception as e:
        IsError = True
        if IsDebugging == True:
            ErrorMessage.clear()
            ErrorMessage.add("No Results | " + str(e))
        elif IsDebugging == False:
            ErrorMessage.add("No Results")

    # We're going to make a data where the results of our scraping are gonna be stored to.
    # The reason why we have to put 'list(object)' is to make it into a list inorder for it to append to our movie_result list.
    data = {
        'results': str(len(movie_title)),
        'title': list(movie_title),
        'location': list(movie_location),
        'date': movie_date,
        'link': list(movie_link)
    }

    # Now we give the data to the movie_result
    movie_result.append(data)
    print("[DrX] Finished Appending")
    
    # Debugging is needed when it comes to big projects, so we have to create one
    #if IsDebugging == True:
        #print("[DrX] Debugging: " + str(IsDebugging))
        #if IsError == True:
            #print("[DrX] Error: " + str(IsError))
            #knownerrors = json.loads(open("errors.json").read())
            #for error in knownerrors:
                #if list(ErrorMessage) in knownerrors:
                    #print(error[ErrorMessage])
                



    # Returns the movie_result so that we can use StartScrape from any other python scripts as long as it is imported.
    # We also want to clear them when someone decides to load up another one.
    
    if IsError == False:
        return movie_result
        movie_title.clear()
        movie_location.clear()
        movie_date.clear()
        movie_link.clear()
        movie_result.clear()
    elif IsError == True:
        return ErrorMessage
        movie_title.clear()
        movie_location.clear()
        movie_date.clear()
        movie_link.clear()
        movie_result.clear()
                        
    #for x in range(len(list(data))):
    #    movie_result.append(list(data)[x])

def FetchSelectedResult(username, pwd, link):
    s = requests.session()

    login_payload = {
        'login': username,
        'password': pwd
    }

    login_req = s.post(url + login_route, headers=HEADERS, data=login_payload)
    print("[DrX] Login Confirmation: " + str(login_req.status_code))
    
    cookies = login_req.cookies
    
    print(s.get(link).text)
    
    #r = requests.get(link)
    #soup = bs4(r.content, features='lmxl')
    #print("[DrX] Scraping selected Result ./.")



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
# WILL NOT WORK ANYMORE!
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
#for article in FetchMovieResults():
#    print(article['title'])

# Gets only the "location" in a list
#for article in FetchMovieResults():
#    print(article['location'])

# Gets only the "date" in a list
#for article in FetchMovieResults():
#    print(article['date'])

# Gets the 'link' to the website to be scraped.
#for article in FetchMovieResults():
#    print(article['link'])

# Specify what no of list to show.
#for article in FetchMovieResults():
#    print(article['link'][0])

# Gets all the list of search results.
#for article in FetchMovieResults():
#    print(article)

for article in FetchMovieResults():
    for x in range(0, int(article['results'])):
        print(article['title'][x] + " | " + article['date'][x] + " | " + article['location'][x] + " | " + article['link'][x] + "\n")

#FetchSelectedResult(Username, Password, "https://smtickets.com/events/view/9471")
# =======================================================================================================#
