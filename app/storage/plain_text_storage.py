from datetime import datetime
from pathlib import Path

from app.api_services import Weather
from app.formatter import format_weather
from app.storage.weather_storage import WeatherStorage


class PlainFileWeatherStorage(WeatherStorage):
    def __init__(self, txt_file_path: Path):
        self._file = txt_file_path

    def save(self, weather: Weather):
        now = datetime.now()

        formatted_weather = format_weather(weather)
        with open(self._file, "a") as file:
            file.write(f"{now}\n{formatted_weather}\n")
