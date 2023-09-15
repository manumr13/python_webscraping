import requests
import bs4
def select_url():
    url = input("enter the url")
    result = requests.get(url)
    return result
def selecting_title(url):
    soup = bs4.BeautifulSoup(url.text,"lxml")
    title = input("enter the select element")
    value  = soup.select(title)
    if len(value)==1:
        print(value[0].text)
    elif len(value)>1:
        for i in range(len(value)):
            print(value[i].text)
    else:
        again = input("invalide value do you want to enter again Yes or No (to quite):")
        if again.capitalize() == "Yes":
            selecting_title(url)
        elif again.capitalize() == "NO":
            exit()
url = select_url()
selecting_title(url)
                