import requests


def weather_service():
    print("Starting weather service")


    # Формируем URL запроса
    url = f'https://67a88a6a6e9548e44fc14e3a.mockapi.io/user'

    try:
        weather_data = requests.get(url).json()

        print(weather_data)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    weather_service()