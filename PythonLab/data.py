# json

import urllib.request
import json

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"


def main():
    web = urllib.request.urlopen(url)

    if web.getcode() == 200:
        data = web.read()
        jsonData = json.loads(data)

        if "title" in jsonData["metadata"]:
            print(jsonData["metadata"]["title"])


if (__name__ == "__main__"):
    main()
