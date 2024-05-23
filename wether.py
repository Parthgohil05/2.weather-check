import requests
import json
import pyttsx3
text_speech = pyttsx3.init()
city = input("Enter the name of the city..\n")

url = f"https://api.weatherapi.com/v1/current.json?key=8d69264e2fff4d178a644536240805&q={city}"
r =requests.get(url)
wdic = json.loads(r.text)
temp=(wdic["current"]["temp_c"])
print(f"The current tempature of {city} is {temp}")
text_speech.say(f"The current tempature of {city} is {temp}")
text_speech.runAndWait()
