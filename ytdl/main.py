import re
import os
import scraper
import time
from youtubedl import downloadVideo

base_url = "https://youtu.be/"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
)

headers = {"user-agent": USER_AGENT}


def getURL():
    yt_url = input("\nEnter Youtube Video URL: ")
    if yt_url != "":
        video_id = re.search(
            r"^[^v]+v=(.{11}).*", yt_url)
        if video_id:
            yt_id = video_id.group(1)
            search_url = base_url + yt_id
            return search_url, yt_id
        else:
            print("\nYouTube video ID not found. Try again!")
            exit(0)
    else:
        print("\nNo URL entered. Run the program again!")
        exit(0)


def showData():
    url, videoID = getURL()
    time.sleep(1)
    print("\nFetching data! Please wait...")
    result = scraper.scrapeURL(url, custom_headers=headers)
    result_string = "\nVideo Title: {}\nVideo ID: {}\nDate Published: {}\nVideo Length: {}\nChannel Name: {}\nSubscribers: {}".format(
        result[0]['Video Title'], videoID, result[0]['Date Published'], result[0]['Video Length'], result[0]['Channel Name'], result[0]['Subscribers'])
    print(result_string)
    choice = input("\nWant to download the video? (Y/N): ")
    if choice == 'y' or choice == 'Y':
        downloadVideo(url)
    elif choice == 'n' or choice == 'N':
        print("\nThank you for using the program!")
        exit(0)
    else:
        print("\nInvalid choice. Exiting...")
        exit(0)


print("\nWELCOME TO YOUTUBE INFO & VIDEO DOWNLOADER")
time.sleep(1)
showData()