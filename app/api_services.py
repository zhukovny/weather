import json
from datetime import datetime
from enum import Enum
from typing import Literal
from typing import NamedTuple
from typing import Union
from urllib.error import URLError
from urllib.request import urlopen

from app.config import OPENWEATHER_URL
from app.coordinates import Coordinates
from app.exceptions import ApiServiceError

Celsius = int


class WeatherType(str, Enum):
    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    FOG = "Fog"
    CLOUDS = "Clouds"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    weather_response = _get_openweather_response(coordinates)
    return _parse_openweather_response(weather_response)


def _get_openweather_response(coordinates: Coordinates) -> bytes:
    url = OPENWEATHER_URL.format(
        latitude=coordinates.latitude,
        longitude=coordinates.longitude,
    )

    try:
        return urlopen(url).read()
    except URLError as e:
        raise ApiServiceError()


def _parse_openweather_response(response: bytes) -> Weather:
    openweather_dict = json.loads(response)

    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=_parse_city_name(openweather_dict),
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return openweather_dict["main"]["temp"]


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(openweather_dict: dict, time: Union[Literal["sunrise"], Literal["sunset"]]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def _parse_city_name(openweather_dict: dict) -> str:
    return openweather_dict['name']
