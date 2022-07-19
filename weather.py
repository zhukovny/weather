from app.api_services import get_weather
from app.coordinates import get_current_coordinates
from app.exceptions import ApiServiceError
from app.exceptions import CantGetCoordinates
from app.formatter import format_weather


def main():
    try:
        coordinates = get_current_coordinates()
    except (CantGetCoordinates, ApiServiceError) as e:
        print(f"Can't get current coordinates")
        exit(1)

    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Can't get weather data from coordinates {coordinates}")
        exit(1)

    print(format_weather(weather))


if __name__ == '__main__':
    main()
