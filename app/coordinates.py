from dataclasses import dataclass
import geocoder

from app.exceptions import CantGetCoordinates


@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float
    

def get_current_coordinates() -> Coordinates:
    try:
        result = geocoder.ip('me')
    except ConnectionError:
        raise CantGetCoordinates

    if not result.ok:
        raise CantGetCoordinates

    return Coordinates(*result.latlng)
