import requests

# Overpass API URL
overpass_url = "http://overpass-api.de/api/interpreter"

# Overpass query (same as before)
overpass_query = """
[out:json];
area[name="Tangerang"]->.searchArea;
area[name="Tangerang Selatan"]->.searchArea;
(
  way["natural"="water"](area.searchArea);
  way["waterway"="river"](area.searchArea);
  way["waterway"="stream"](area.searchArea);
  relation["waterway"="river"](area.searchArea);
  relation["natural"="water"](area.searchArea);
);
out geom;
"""

response = requests.get(overpass_url, params={'data': overpass_query})

if response.status_code == 200:
    try:
        data = response.json()
        print(data)
        print(response)
        print("JSON data successfully decoded!")
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
else:
    print(f"Error: Unable to fetch data. Status Code {response.status_code}")