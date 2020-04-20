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
        print("Entering: ",f"#pagecontent > div.box.community-content.forum-box > div.boxbody > table > tbody > tr:nth-child({episode}) > td.topic-titles.row2 > h3 > a")
        ep.click()

        while True:
            try:
                self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[2]/p[5]")
                break
            except:
                pass
        attempt = 0
        for i in infinitenumbers(1):
            if (attempt > 100):
                self.browser.execute_script("window.history.go(-1)")
                break
            attempt += 1
            try:
                self.browser.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[2]/p[{i}]")
                print(a.text[:a.text.index(":")+1])
                attempt = 0
            except:
                pass

bot = HMBot()

attempt = 0
for i in infinitenumbers(7):
    if (attempt > 30):
        break
    try:
        bot.enterEpisode(i)
        attempt += 1
    except Exception as e:
        print(e)
        pass
