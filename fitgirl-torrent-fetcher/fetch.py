import requests
import urllib
import sys
import re
from bs4 import BeautifulSoup

base_url = "https://fitgirl-repacks.site/page/"
page_num = input("\nWhich page to fetch torrents from? : ")
filename = input("\nEnter filename to save info to : ")
fetch_url = base_url + page_num + "/"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
)
headers = {"user-agent": USER_AGENT}

resp = requests.post(fetch_url, headers=headers)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    data1 = []
    data2 = []
    tables = soup.find_all("article", attrs={"class": "type-post"})
    for table in tables:
        headings = table.find_all("h1")
        for heading in headings:
            titles = heading.find_all("a", href=True, text=True)
            title = [re.sub(r'<.+?>', r'', str(a)) for a in titles]
            if titles:
                #print("\n", title)
                data1.append(str(title) + "\n")
        rows = table.find_all("ul")
        for row in rows:
            cols = row.find("li")
            magnets = cols.find_all("a", text="magnet", href=True)
            for magnet in magnets:
                #print(" " + magnet["href"])
                data2.append(magnet["href"] + "\n")
    file = open(filename, "w", encoding="utf-8")
    file.writelines(data1)
    file.writelines(data2)
    file.close()
    print("\nPage", page_num, "torrents are saved to", filename)
