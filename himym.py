from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def infinitenumbers(start):
    count = start
    while True:
        yield count
        count += 1

class HMBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.browser = webdriver.Chrome(r'C:\Users\Kayra\Desktop\Projects\chromedriver_win32\chromedriver.exe',chrome_options=options)
        self.browser.get("https://transcripts.foreverdreaming.org/viewforum.php?f=177")

    def enterEpisode(self,episode):
        ep = self.browser.find_element_by_css_selector(f"#pagecontent > div.box.community-content.forum-box > div.boxbody > table > tbody > tr:nth-child({episode}) > td.topic-titles.row2 > h3 > a")
        print(ep.text)
        ep.click()
        for i in infinitenumbers(0):
            try:
                a = self.browser.find_elements_by_tag_name("p")[i].text
                if (":" in a):
                    print(a[:a.index(":")+1])
            except:
                break
        self.browser.execute_script("window.history.go(-1)")

bot = HMBot()

for i in infinitenumbers(7):
    try:
        bot.enterEpisode(i)
    except:
        pass
