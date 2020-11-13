# SM Ticket <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Django"> <img alt="Dichill" src="https://img.shields.io/badge/SM-Tickets-blue"> 

<img src="https://sa.kapamilya.com/absnews/abscbnnews/media/2019/business/06/26/20190626-sm-cinema.jpg?ext=.jpg" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="200" height="170">

DrX - SM Ticket is a API and a Website and can be accesible to anyone to get daily events, searches, and more in any SM Branch in the Philippines. This is not the official API being used by the professionals. This is just a fun project to upcoming programmers who are
trying to have some fun in coding and such. Feel free to contribute and make some changes in the **<a href="https://github.com/Dichill/drx-smticket/issues">Issues</a>** page.

* Official Website of **<a href="https://smtickets.com/">SM Ticket</a>**
* Help the victims of **<a href="https://www.nbcnews.com/better/lifestyle/how-help-victims-hurricane-dorian-ncna1050851#:~:text=You%20can%20make%20a%20donation,phone%20bill%2C%20Cooper%20says).">Hurricane Dorian</a>**

# Installation
```bash
pip install -r requirements.txt
```

# Documentation <img alt="Read the Docs" src="https://img.shields.io/readthedocs/pip">
### Table of Contents
* Fetch Attractions Function *(Coming Soon)*
* Fetch Other Venues Function *(Coming Soon)*
* Fetch SM Venues Function *(Coming Soon)*
* Fetch Events Function *(Coming Soon)*
* Fetch Events View Function *(Coming Soon)*
* Search Function

<hr>

## Search Function <img alt="Read the Docs" src="https://img.shields.io/readthedocs/pip">
### Importing

```python
import scrapy as sm 
```
<p style="text-align=center;">What we need to do is import <strong>scrapy.py</strong> In order to import it, the file must be in the same directory as <strong>scrapy.py</strong>, if it doesn't work use <strong>importlib</strong></p>

<hr>

### Search Variable
```python
import scrapy as sm

sm.Search = Input("What to Search: ")
```
<p style="text-align:center;">Now we will call one of the variables in Scrappy which is <strong>Search</strong>, The <strong>Search</strong> Variable contains what to search on 
     <strong><a href="https://smticket.com/">SM Ticket</a></strong>, we want to know what the user really wants to search so we add <strong>Input</strong> <italic>(Any method is fine as long as you pass a string variable.)</italic></p>
     
<hr>

### Fetching Movie Results
 ```python
import scrapy as sm

sm.Search = Input("What to Search: ")

try:
    for article in sm.FetchMovieResults():
        for x in range(0, int(article['results'])):
            print(article['title'][x] + " | " + article['date'][x] + " | " + article['location'][x] + " | " + article['link'][x] + "\n")
except Exception as e:
    print(e)
```
<p style="text-align:center;">Now we want to add a try/except to make it neat and to know what caused the problem. Mostly the problem that users will meet is that
if they search an invalid movie title it will return a 'NoneType' exception or a Iterable exception.</p>

<hr>

### Why find the Range?
```python
int(article['results'])
```
<p style="text-align:center;">Now in the third example, why are we finding for the range of our results? Well its simple, we want to know how many results returned, lets say for example it returned a number of 9. Since we are in a for loop we want to print out on how many title, date, location, and link that the result gave.</p>

<hr>

### Working with List
```python

# Let x be any integer number
article['title'][x]
```
<p style="text-align:center;">As what it said, Let x be any integer number. As long as that number doesn't exceed on how many results are there in the search results it wont return an error. If you let x be '1' then it will print out the first title in the list.</p>

<hr>

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

## Update Logs <img alt="Updates" src="https://img.shields.io/badge/Logs-Updates-orange">
```bash
[+] November 12 2020 | 6:00 PM  -> Updated Scraper
[+] November 11 2020 | 11:00 PM -> Creation of SM Ticket
```
