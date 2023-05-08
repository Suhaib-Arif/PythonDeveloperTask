from bs4 import BeautifulSoup
import requests
import json

News_Endpoint = "https://www.reuters.com"

response = requests.get(url=News_Endpoint)

markup = response.text

soup = BeautifulSoup(markup, "html.parser")

news_list = []

for item in soup.select('div[data-testid*=StoryCard]'):

    Heading = item.find(attrs={"data-testid": "Heading"}).getText()
    Date = item.find(name="time")["datetime"].split("T")[0]
    url = f'{News_Endpoint}{item.find(attrs={"data-testid": "Heading"})["href"]}'

    try:
        Subtitle = item.find(attrs={"data-testid": "Body"}).getText()
    except AttributeError:
        Subtitle = "Not Found"

    data_dict = {
        "Heading":Heading,
        "Date":Date,
        "URL":url,
        "Subtitle":Subtitle
    }

    news_list.append(data_dict)

with open(file="data.json",mode="w") as file_data:
    json.dump(news_list,file_data)