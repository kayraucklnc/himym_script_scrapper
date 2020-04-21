from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

ppl = dict()

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
        self.browser.implicitly_wait(5)
        print(ep.text)
        ep.click()
        WebDriverWait(self.browser, 3).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'p')))
        for i in infinitenumbers(0):
            try:
                a = self.browser.find_elements_by_tag_name("p")[i].text
                if (":" in a):
                    # person = a[:a.index(":")]
                    # if True:
                    #     ppl[person] += 1
                    # else:
                    #     ppl[person] = 1
                    print(a[:a.index(":")+1])
            except Exception as e:
                print(e)
                break
        self.browser.execute_script("window.history.go(-1)")

bot = HMBot()


attempt = 0
link = 7
pg = 1
for i in infinitenumbers(0):
    if (pg >= 4):
        break
    link += 1
    if (attempt > 2):
        attempt = 0
        pg += 1
        pages = bot.browser.find_element_by_link_text(f"{pg}")
        pages.click()
        link = 7
    try:
        time.sleep(0.6)
        attempt += 1
        bot.enterEpisode(link)
        attempt = 0
    except Exception as e:
        print(e)
        pass

file = open("Talks.txt","a+")
for key,value in ppl:
    file.write(key+":"+value)
file.close()
