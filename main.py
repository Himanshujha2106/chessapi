from bs4 import BeautifulSoup
import requests
import json
url = 'https://www.chess.com/stats/live/rapid/dontknow8782'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

script_tags_with_data = soup.find_all('script', text=lambda t: t and 'window.chesscom.stats' in t)
for script_tag in script_tags_with_data:
    # Extract the JSON data from the script tag
    start_index = script_tag.text.find('{')
    end_index = script_tag.text.rfind('}') + 1
    json_data = script_tag.text[start_index:end_index]
    # Parse the JSON data into a Python dictionary
    # data_dict = json.loads(json_data)

    # Convert the dictionary to JSON format
    # json_output = json.dumps(data_dict, indent=2)
print(type(json_data))
  
with open("scraped_page.html", "w", encoding="utf-8") as f:
  for script in script_tag:
      f.write(str(json_data))

f.close()
print("Saved HTML to scraped_page.html")