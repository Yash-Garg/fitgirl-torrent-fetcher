import wikipedia
import webbrowser
from os import system


def getRandomArticle():
    wiki_page = wikipedia.random(1)
    wiki_load = wikipedia.page(wiki_page)
    choice = input(
        "\nWould you like to read about {} ? (Y/N/Q): ".format(wiki_page))
    if (choice == "Y" or choice == "y"):
        print("\nSummary about " + wiki_page +
              ":\n\n" + wikipedia.summary(wiki_page))
        browserchoice = input("\nOpen Wikipedia page in browser? (Y/N): ")
        if (browserchoice == "Y" or browserchoice == "y"):
            webbrowser.open(wiki_load.url, new=2)
            ch = input(
                "\nWill you like to continue viewing articles or quit? (C/Q): ")
            if (ch == "C" or ch == "c"):
                system("cls")
                getRandomArticle()
            else:
                exit(0)
        else:
            system("cls")
            getRandomArticle()
        exit(0)
    elif (choice == "q" or choice == "Q"):
        print("\nThanks for using this program!")
        exit(0)
    else:
        system("cls")
        getRandomArticle()


# system("cls") will only work with windows
system("cls")
print("\nWelcome to random wikipedia article fetcher!")
getRandomArticle()
