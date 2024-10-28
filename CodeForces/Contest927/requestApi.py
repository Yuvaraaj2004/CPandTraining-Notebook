import requests
import json
# curl - -request GET \
# 	- -url 'https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations?fromStationCode=TJ&toStationCode=CBE&dateOfJourney=2024-10-17' \
# 	- -header 'x-rapidapi-host: irctc1.p.rapidapi.com' \
# 	- -header 'x-rapidapi-key: b60f8ca0damsh5c95a972939f48ep16c52ejsn72c4c71fed99'
start, dest, date = "MV", "TPJ", "2024-10-17"
r = requests.get(f'https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations?fromStationCode={start}&toStationCode={dest}&dateOfJourney={date}',
                 headers={
                     "x-rapidapi-host": "irctc1.p.rapidapi.com",
                     'x-rapidapi-key': 'b60f8ca0damsh5c95a972939f48ep16c52ejsn72c4c71fed99'})
print(r.content
      )
