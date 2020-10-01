from requests_html import HTMLSession
import lxml
from bs4 import BeautifulSoup

session = HTMLSession()


def scrapeURL(url, custom_headers):
    response = session.get(url)
    response.html.render(sleep=1)
    if response.status_code == 200:
        soup = BeautifulSoup(response.html.html, "lxml")
        
        data = []

        title = soup.find("h1").text.strip()
        date_published = soup.find("div", {"id": "date"}).text[1:]
        duration = soup.find("span", {"class": "ytp-time-duration"})
        vid_length = duration.text
        channel = soup.find("yt-formatted-string",
                            {"class": "ytd-channel-name"}).find("a")
        channel_name = channel.text
        channel_subs = soup.find(
            "yt-formatted-string", {"id": "owner-sub-count"}).text.strip()

        data.append({"Video Title": title, "Date Published": date_published,
                "Video Length": vid_length, "Channel Name": channel_name, "Subscribers": channel_subs})
        return data

    else:
        print("\nError sending request to given URL")
        exit(0)
