from pathlib import Path

from app.api_services import get_weather
from app.coordinates import get_current_coordinates
from app.exceptions import ApiServiceError
from app.exceptions import CantGetCoordinates
from app.formatter import format_weather
from app.storage.json_storage import JSONFileWeatherStorage
from app.storage.plain_text_storage import PlainFileWeatherStorage
from app.storage.weather_storage import save_weather


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
    txt_storage = PlainFileWeatherStorage(Path.cwd() / "history.txt")
    json_storage = JSONFileWeatherStorage(Path.cwd() / "history.json")
    save_weather(weather, txt_storage)
    save_weather(weather, json_storage)


if __name__ == '__main__':
    main()
