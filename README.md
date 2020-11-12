# SM Ticket

<img src="https://sa.kapamilya.com/absnews/abscbnnews/media/2019/business/06/26/20190626-sm-cinema.jpg?ext=.jpg" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="170" height="170">

DrX - SM Ticket is a API and a Website and can be accesible to anyone to get daily events, searches, and more in any SM Branch in the Philippines. This is not the official API being used by the professionals. This is just a fun project to upcoming programmers who are
trying to have some fun in coding and such. Feel free to contribute and make some changes in the **<a href="https://github.com/Dichill/drx-smticket/issues">Issues</a>** page.

* Official Website of **<a href="https://smtickets.com/">SM TICKET</a>**
<iframe height="400px" width="100%" src="https://repl.it/@Dichill/drx-smticket?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
## USAGE
```python
# Gets only the "title" in a list
for article in FetchMovieResults():
    print(article['title'])

# Gets only the "location" in a list
for article in FetchMovieResults():
    print(article['location'])

# Gets only the "date" in a list
for article in FetchMovieResults():
    print(article['date'])

# Gets the 'link' to the website to be scraped.
for article in FetchMovieResults():
    print(article['link'])

# Specify what no. of list to show.
for article in FetchMovieResults():
    print(article['link'][0])

# Gets all the list of search results.
for article in FetchMovieResults():
    print(article['title'])
    print(article)
    
# Gets all of them in an organized manner.
for article in FetchMovieResults():
    for x in range(0, int(article['results'])):
        print(article['title'][x] + " | " + article['date'][x] + " | " + article['location'][x] + " | " + article['link'][x] + "\n")
```
## OUTPUT
```bash
Title of Movie: Fate
[DrX] Link: https://smtickets.com/events/search/Fate
[DrX] Scraping ./.
[DrX] Finished Appending
SM Cinema Bacoor Fate Stay Night III - Spring Song | November 21, 2020 | SM CINEMA - BACOOR | https://smtickets.com/events/view/9470

SM Cinema Masinag Fate Stay Night III - Spring Song | November 21, 2020 | SM CINEMA - MASINAG | https://smtickets.com/events/view/9471

SM Cinema San Mateo Fate Stay Night III - Spring Song | November 21, 2020 | SM CINEMA - SAN MATEO | https://smtickets.com/events/view/9472
```
