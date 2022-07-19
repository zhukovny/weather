from app.api_services import Weather


class WeatherStorage:
    def save(self, weather: Weather):
        raise NotImplementedError


def save_weather(weather: Weather, storage: WeatherStorage):
    storage.save(weather)
