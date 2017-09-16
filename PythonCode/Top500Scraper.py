from urllib.request import urlopen
from bs4 import BeautifulSoup
import googlemaps

countryCoordinates = {}

def getLocInfo(url):
    soup = BeautifulSoup(urlopen(url))
    tableRows = soup.find('table', class_='table table-condensed').findAll("tr")[1:]
    country = str(tableRows[2].findAll('td')[0].text).strip()
    if country == "Korea, South":
        country = "South Korea"
    return country
callsCount = 0
def getCoordinates(country):
    gmaps = googlemaps.Client(key='Your API Key')
    geocode_result = gmaps.geocode(country)
    lat = str(geocode_result[0]['geometry']['location']['lat']).strip()
    lng = str(geocode_result[0]['geometry']['location']['lng']).strip()
    global callsCount
    callsCount += 1
    print("Calls Count=",callsCount)
    return (lat,lng)

def main():
    urls = [
        'https://www.top500.org/list/2017/06/?page=',
        'https://www.top500.org/list/2016/06/?page=',
        'https://www.top500.org/list/2015/06/?page=',
        'https://www.top500.org/list/2014/06/?page=',
        'https://www.top500.org/list/2013/06/?page=',
        'https://www.top500.org/list/2012/06/?page=',
        'https://www.top500.org/list/2011/06/?page=',
        'https://www.top500.org/list/2010/06/?page=',
        'https://www.top500.org/list/2009/06/?page=',
        'https://www.top500.org/list/2008/06/?page=',
        'https://www.top500.org/list/2007/06/?page=',
        'https://www.top500.org/list/2006/06/?page=',
        'https://www.top500.org/list/2005/06/?page='
    ]
    year = 2017
    for url in urls:
        print("Current Year:",year)
        outputFile = open('Top500_'+str(year)+'.csv', 'a')
        #Writing Header Row
        outputFile.write("Rank,Country,Lat,Lng")
        rank = 1
        for i in range(1,6):
            page = urlopen(url + str(i))
            soup = BeautifulSoup(page)
            table = soup.find('table', class_='table table-condensed table-striped')
            for row in table.findAll("tr")[1:]:
                print("Rank: ", rank)
                try:
                    #First, getting the city and country
                    cells = row.findAll('td')
                    url_1 = "https://www.top500.org" + str(cells[1].findAll("a")[0]['href'])
                    country = getLocInfo(url_1)
                    print(country)
                    (lat, lng) = (0,0)
                    if country in countryCoordinates:
                        (lat, lng) = countryCoordinates[country]
                    else:
                        (lat, lng) = getCoordinates(country)
                        countryCoordinates[country] =(lat, lng)
                    #print(str(rank),name,country,lat, lng)
                    outputFile.write("\n" + str(rank) + "," + country + "," + lat + "," + lng)
                except:
                    outputFile.write("\n" + str(rank) + ",NULL,NULL,NULL")
                rank += 1
        outputFile.close()
        year -= 1
    print("End of Crawling!")

main()
