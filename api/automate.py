from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

CHROME_PATH = 'chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(executable_path=CHROME_PATH, options=chrome_options)

def Login(username, password, link):
    try:
        # Go to the browser
        browser.get(link)
        print("[Drx] Getting Browser Data")

        # Fetch Buttons
        print("[Drx] Finding Login Pop Up Button")
        button = browser.find_element_by_xpath(u"/html/body/header/div[1]/div[2]/div[1]/button[2]")
        browser.implicitly_wait(10)
        button.click()

        browser.implicitly_wait(10)
        browser.find_element_by_xpath(u"/html/body/div[26]/div/div[3]/a[1]").click()
        user = browser.find_element_by_xpath(u"/html/body/div[26]/div/div/div/form/div[1]/input")
        pwd = browser.find_element_by_xpath('//*[@id="password"]')
        bttn = browser.find_element_by_xpath(u"/html/body/div[26]/div/div/div/form/button")

        
        print("[Drx] Logging in")
        user.send_keys(username)
        pwd.send_keys(password)
        bttn.click()

        return browser.page_source
    except Exception as e:
        print(e)
        return False

def FetchData():
    data = browser.page_source
    soup = BeautifulSoup(data, features='lxml')
    
    title = soup.find("div", {"class":"c-event-banner__details-row"})
    title = title.find("h1", {"class":"h1 h1--title"}).text

    final_output = []

    pref_dates = []
    pref_times = []

    tickets_location = []
    tickets_section = []
    tickets_price = []
    tickets_quanity = []

    try:
        # Preferred
        dropdown = soup.find_all("div",{"class":"c-custom-select"})
        for d in dropdown:
            date = d.find_all("span", {"class":"date"})
            time = d.find_all("span", {"class":"time"})
        for da in date:
            pref_dates.append(da.text)
        for ta in time:
            pref_times.append(ta.text)

        # Tickets
        container = soup.find_all("div", {"class":"c-list"})
        
            

    except Exception as e:
        print(e)
   
    data = {
        'title': title,
        'date': pref_dates,
        'time': pref_times,
        'location': tickets_location
    }

    final_output.append(data)
    print(final_output)


if Login('DichillTomarong', 'dichill1212', 'https://smtickets.com/events/view/9473') == False:
    print("[DrX] Failed to Login")
else:
    print("[DrX] Success")
    FetchData()