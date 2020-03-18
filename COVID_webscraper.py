from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = "https://www.worldometers.info/coronavirus/"

uClient = uReq(myUrl)
pageHTML = uClient.read()
uClient.close()

# scrapes text to get the number of total cases, deaths, and recovered patients
pageSoup = soup(pageHTML, "html.parser")
counters = pageSoup.findAll("div", {"class":"maincounter-number"})
listOfCases = list()
for counter in counters:
    numberOf = counter.span
    text = soup.get_text(numberOf)
    listOfCases.append(text)

labeler = dict()
labeler["total cases:"] = listOfCases[0]
labeler["total deaths:"] = listOfCases[1]
labeler["total recovered:"] = listOfCases[2]

# scraping the time data was last updated
lastUpdated = pageSoup.find("div", {"style":"font-size:13px; color:#999; text-align:center"})
lastUpdatedText = soup.get_text(lastUpdated)


# print results
print(lastUpdatedText)
for key, value in labeler.items():
    print(key, value)

timeConverterUrl = "https://savvytime.com/converter/gmt-to-est"
timeClient = uReq(timeConverterUrl)
timeHTML = timeClient.read()
timeClient.close()

timeSoup = soup(timeHTML, "html.parser")
originalGSTtime = ""
