from app.api_services import Weather


def format_weather(weather: Weather) -> str:
    return (f"{weather.city}, temperature {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"Sunrise: {weather.sunrise.strftime('%H:%M')}\n"
            f"Sunset: {weather.sunset.strftime('%H:%M')}\n")
