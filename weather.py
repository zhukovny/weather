from api_services import get_weather
from config import OPENWEATHER_URL
from coordinates import get_current_coordinates
from formatter import format_weather


def main():
    coordinates = get_current_coordinates()
    # weather = get_weather(coordinates)
    # print(format_weather(weather))
    print(coordinates)
    print(OPENWEATHER_URL)

if __name__ == '__main__':
    main()
