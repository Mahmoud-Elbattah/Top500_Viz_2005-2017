import json
import csv

for year in range(2005,2018):
    output = { "type": "FeatureCollection",
           "features": []}
    with open('countryCounts_'+str(year)+'.csv') as csv_file:
        for (i,row) in enumerate(csv.DictReader(csv_file)):
            output['features'].append({
            'type': 'Feature',
            'properties': {"Name": row["Name"],
                           "Count": row["Count"]
                           },
            "geometry":{"type": "Point",
                        "coordinates":[float(row["Lng"]),float(row["Lat"])]}
            })
            output_json = json.dumps(output)
        print("Year "+str(year)+"\n"+ output_json)