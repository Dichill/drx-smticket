# SMTICKET | API | DJANGO | HEROKU
* DrX SMTICKET WEBSITE: *(Coming Soon)*
* DrX SMTICKET ANDROID: *(Coming Soon)*
* DrX SMTICKET PC: *(Coming Soon)*
* Official Link: https://smticket.com/

## FEATURES
* **Fast Search and Fast Automated Bot!**
* **Open source for more improvements!**
* **Get Data from https://smticket.com/ and be ahead of anyone**
* **Get Tickets easily with just a click!**

## SCRAPER USAGE FOR THOSE WHO ARE NEW TO PROGRAMMING AND WANT TO GET DATA FROM SMTICKET
```python
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

# Specify what no. of list to show.
#for article in FetchMovieResults():
#    print(article['link'][0])

# Gets all the list of search results.
for article in FetchMovieResults():
    #print(article['title'])
    print(article)

# =======================================================================================================#
```