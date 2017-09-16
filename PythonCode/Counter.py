import pandas

countryCoordinates = {}
def countryCounts(data,year):
    counts = {}
    for (i,country) in enumerate(data["Country"]):
        if country in counts:
            counts[country] += 1
        else:
            counts[country] = 1
            countryCoordinates[country] = (data.loc[i,"Lat"],data.loc[i,"Lng"])
    outputFile = open("countryCounts_"+str(year)+".csv", "a")
    outputFile.write("Name,Count,Lat,Lng")
    for (key, value) in sorted(counts.items(),key=lambda item: (item[1], item[0]), reverse=True):
        Lat= str(countryCoordinates[str(key)][0])
        Lng = str(countryCoordinates[str(key)][1])
        outputFile.write("\n"+str(key)+","+str(value)+","+Lat+","+Lng)

def main():
    print("***Finding Country Counts***")
    for year in range(2005, 2018):
       print("Current Year:",year)
       data = pandas.read_csv("Top500_" + str(year) + ".csv", encoding="ISO-8859-1")
       countryCounts(data, year)


main()
print("Done.")


