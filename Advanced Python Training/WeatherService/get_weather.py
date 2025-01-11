from threading import Thread
from weather_service import getWeather

def getWeatherForCity(city):
    try:
        weather = getWeather(city)

        print('------------------------------------------------------------')
        print(f'Weather forcast for {city}')
        print(f'Current Weather: {weather['weather'][0]['description']}')
        print(f'Wind Speed: {weather['wind']['speed']}')
        print(f'Feels like: {weather['main']['feels_like']}')
        print(f'Current Temperature: {weather['main']['temp']}')
        print(f'Min. Temperature: {weather['main']['temp_min']}')
        print(f'Max. Temperature: {weather['main']['temp_max']}')
    except Exception as err:
        print('******************EXCEPTION******************')
        print(f'Error while fetching the weather information for {city}')
        print('******************EXCEPTION******************')

def main():
    # cities = ['abc', 'Athlone', 'Dublin', 'Galway', 'Belfast', 'Genoa', 'Cork', 'Budapest', 'Kista']
    cities = ['abc', 'Athlone', 'Dublin', 'Galway']

    for city in cities:
        thread = Thread(target=getWeatherForCity, args=(city,), kwargs={})
        # threads.append(thread)
        thread.start()

    print('printing from main thread')

    print('----------------------------------------')
    print('printing after all threads are executed')

if __name__ == '__main__':
    main()
