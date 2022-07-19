import json
from datetime import datetime
from pathlib import Path
from typing import TypedDict

from app.api_services import Weather
from app.formatter import format_weather
from app.storage.weather_storage import WeatherStorage


class HistoryRecord(TypedDict):
    date: str
    weather: str


class JSONFileWeatherStorage(WeatherStorage):
    def __init__(self, json_file_path: Path):
        self._file = json_file_path
        self._init_storage()

    def save(self, weather: Weather):
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": format_weather(weather),
        })
        self._write(history)

    def _init_storage(self):
        if not self._file.exists():
            self._file.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._file, "r") as file:
            return json.load(file)

    def _write(self, history: list[HistoryRecord]):
        with open(self._file, "w") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)
