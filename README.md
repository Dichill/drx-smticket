# SM Ticket <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Django">

<img src="https://sa.kapamilya.com/absnews/abscbnnews/media/2019/business/06/26/20190626-sm-cinema.jpg?ext=.jpg" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="200" height="170">

DrX - SM Ticket is a API and a Website and can be accesible to anyone to get daily events, searches, and more in any SM Branch in the Philippines. This is not the official API being used by the professionals. This is just a fun project to upcoming programmers who are
trying to have some fun in coding and such. Feel free to contribute and make some changes in the **<a href="https://github.com/Dichill/drx-smticket/issues">Issues</a>** page.

* Official Website of **<a href="https://smtickets.com/">SM Ticket</a>**
* Help the victims of **<a href="https://www.nbcnews.com/better/lifestyle/how-help-victims-hurricane-dorian-ncna1050851#:~:text=You%20can%20make%20a%20donation,phone%20bill%2C%20Cooper%20says).">Hurricane Dorian</a>**

## Documentation
```python
import scrapy as sm 
```
<p style="text-align=center;">What we need to do is import <strong>scrapy.py</strong> In order to import it, the file must be in the same directory as <strong>scrapy.py</strong>, if it doesn't work use <strong>importlib</strong></p>

<hr>

```python
import scrapy as sm

sm.Search = Input("What to Search: ")
```
<p style="text-align=center;">Now we call one of the variables in Scrappy which is <strong>Search</strong>, The <strong>Search</strong> Variable contains what to search on 
     <strong><a href="https://smticket.com/">SM Ticket</a></strong>, we want to know what the user really wants to search so we add <strong>Input</strong> (Any method is fine as long as you pass a string variable.)</p>

## USAGE [![Run on Repl.it](https://repl.it/badge/github/plibither8/2048.cpp)](https://repl.it/@Dichill/DrX-SMTicket)
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
## OUTPUT [![Run on Repl.it](https://repl.it/badge/github/plibither8/2048.cpp)](https://repl.it/@Dichill/DrX-SMTicket)
```bash
Title of Movie: Fate
[DrX] Link: https://smtickets.com/events/search/Fate
[DrX] Scraping ./.
[DrX] Finished Appending
SM Cinema Bacoor Fate Stay Night III - Spring Song | November 21, 2020 | SM CINEMA - BACOOR | https://smtickets.com/events/view/9470

SM Cinema Masinag Fate Stay Night III - Spring Song | November 21, 2020 | SM CINEMA - MASINAG | https://smtickets.com/events/view/9471

SM Cinema San Mateo Fate Stay Night III - Spring Song | November 21, 2020 | SM CINEMA - SAN MATEO | https://smtickets.com/events/view/9472
```
