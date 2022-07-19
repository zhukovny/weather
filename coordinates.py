from dataclasses import dataclass
import geocoder

from exceptions import CantGetCoordinates


@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float
    

def get_current_coordinates() -> Coordinates:
    try:
        result = geocoder.ip('me')
    except ConnectionError:
        raise CantGetCoordinates("Can't get coordinates. Connection error")

    if not result.ok:
        raise CantGetCoordinates(f"Can't get coordinates. {result.json['status']}")

    return Coordinates(*result.latlng)
