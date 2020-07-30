import requests
import re
import os
import json
import string
from bs4 import BeautifulSoup

base_url = "https://1337x.to"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
)
headers = {"user-agent": USER_AGENT}

query = input("\nEnter keyword to search: ")

if query != "":
    search_url = base_url + "/search/" + query + "/1/"
    response = requests.post(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        urls = []
        data = []
        table = soup.find(
            "table", attrs={"class": "table-list table table-responsive table-striped"})
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td", attrs={"class": "coll-1 name"})
            for col in cols:
                torrents = col.find_all("a", href=True, class_=None)
                for torrent in torrents:
                    urls.append(base_url + torrent["href"])
        for url in urls:
            resp = requests.post(url, headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, "lxml")
                division = soup.find(
                    "div", attrs={"class": "box-info-heading clearfix"})
                title = division.find("h1", text=True, class_=None)
                seeds = soup.find("span", attrs={"class": "seeds"})
                size = soup.find("span", text=re.compile(
                    r'([0-9].[0-9]) ([A-Z])'), class_=None)
                magnet = soup.find("a", href=re.compile(
                    r'[magnet]([a-z]|[A-Z])\w+'), class_=True).attrs["href"]
                data.append({"Title": title.contents[0].encode('ascii', 'ignore').decode('ascii').strip(
                ), "Seeders": seeds.contents[0], "Size": size.contents[0], "Magnet": magnet})
        file = open("output.json", "w", encoding="utf-8")
        json.dump(data, file, indent=4)
        file.close()
        print("\nSuccessfully saved torrents to output.json")

else:
    print("\nNo keyword specified. Re-run the script!")
    exit(0)
