from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

now = datetime.now()
created_at = now.strftime("%d%m%Y")

application_path = os.path.dirname(sys.executable)

url = "https://www.thesun.co.uk/sport/football/"

#Configure chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser-item teaser__small  theme-football"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./div/a/span').text
    subtitle = container.find_element(by='xpath', value='./div/a/h3').text
    link = container.find_element(by='xpath', value='./div/a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

data = {
    "Titles" : titles,
    "Subtitles" : subtitles,
    "Links" : links
}

file_name = f"headlines_{created_at}.csv"
final_file_name = os.path.join(application_path, file_name)

df = pd.DataFrame.from_dict(data)
df.to_csv(final_file_name, index=False)

driver.quit()