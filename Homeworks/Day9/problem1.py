'''
1. **Weather Data Retrieval:**
   Write a program that fetches the current weather data for a specific city using a weather API.
   - Utilize a weather API (such as OpenWeatherMap) to retrieve the current weather details (temperature, humidity, wind speed, etc.) for a user-input city.
   '''


import requests

def know_temperature(city_name):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=8b1131c784c8f149fd80563f0d86d31f"
    response = requests.get(api_url)

    if response.status_code == 200: 
        #Standard response code 200 means the request was successful.

        data = response.json()
        #Getting rsopnse as json format
    
        print(f"City name: {city_name}")
        print(f"Temperature: {data['main']['temp']}")
        print(f"Humidity: {data['main']['humidity']}")
        print(f"Wind Speed: {data['wind']['speed']}")
        print(f"Weather Status: {data['weather'][0]['main']}")
        print(f"Weather Description: {data['weather'][0]['description']}")

    else:
        print(f"Error occurred: {response.status_code}")

result = know_temperature(city_name="london")


'''
OUTPUT:-

City name: london
Temperature: 283.57
Humidity: 76
Wind Speed: 3.09
Weather Status: Clouds
Weather Description: overcast clouds

'''
