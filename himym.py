from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import operator
import time
import pdb

ppl = dict()

def infinitenumbers(start,stop):
    count = start
    while True:
        if (count == stop):
            break
        yield count
        count += 1

class HMBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.browser = webdriver.Chrome(r'C:\Users\Kayra\Desktop\Projects\chromedriver_win32\chromedriver.exe',chrome_options=options)
        self.browser.get("https://transcripts.foreverdreaming.org/viewforum.php?f=177")

    def enterEpisode(self):
        WebDriverWait(self.browser, 1).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'p')))
        for i in infinitenumbers(0,-1):
            try:
                a = self.browser.find_elements_by_tag_name("p")[i].text
                if (":" in a):
                    # print(a[:a.index(":")+1])
                    person = a[:a.index(":")+1]
                    if person in ppl.keys():
                        ppl[person] += 1
                    else:
                        ppl[person] = 1
            except Exception as e:
                # print(e)
                break
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(0.5)

bot = HMBot()


attempt = 0
link = 6
pg = 1
try:
    for i in infinitenumbers(0,-1):
        if (pg >= 9):
            break
        link += 1
        if (attempt > 3):
            attempt = 0
            pg += 1
            try:
                pages = bot.browser.find_element_by_link_text(f"{pg}")
            except:
                pass
            pages.click()
            link = 6
        try:
            time.sleep(0.5)
            attempt += 1

            ep = bot.browser.find_element_by_css_selector(f"#pagecontent > div.box.community-content.forum-box > div.boxbody > table > tbody > tr:nth-child({link}) > td.topic-titles.row2 > h3 > a")
            bot.browser.implicitly_wait(0.5)
            print(ep.text)
            header = ep.text

            most = open("mosttalk.txt","a+")
            ppl = dict()
            ep.click()
            bot.enterEpisode()
            mostt = max(ppl.items(), key=operator.itemgetter(1))[0]
            print(mostt,ppl[mostt])
            # tes = ep.text + "\t" + mostt + "\t" + str(ppl[mostt]) + "\n"
            most.write(header[:header.index(" - ")] + "\t" + mostt+"\n")
            most.close()

            print("==========================")
            attempt = 0
        except Exception as e:
            print(e)
        pass
except:
    lok = open("error.txt","a+")
    lok.write(ppl.keys())
    lok.write("\n")
    lok.write(ppl.values())
    lok.close()

# file = open("Talks.txt","a+")
# ppl = {k: v for k, v in sorted(ppl.items(), key=lambda item: item[1],reverse=True)}
# for key,value in ppl.items():
#     file.write(key+" "+str(value)+"\n")
# file.close()
