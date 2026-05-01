# api/services.py
from .models import FuelStation
import math

MAX_RANGE = 500  # miles
MPG = 10

def split_route(route, max_distance=MAX_RANGE):
    # Simplified: assume route["features"][0]["properties"]["summary"]["distance"] in meters
    total_miles = route["features"][0]["properties"]["summary"]["distance"] / 1609.34
    segments = math.ceil(total_miles / max_distance)
    return [total_miles / segments] * segments

def find_cheapest_station():
    # For demo: just return global cheapest
    return FuelStation.objects.order_by("price_per_gallon").first()

def calculate_fuel_stops(route):
    segments = split_route(route)
    stops = []
    total_cost = 0
    for seg_miles in segments:
        station = find_cheapest_station()
        gallons = seg_miles / MPG
        cost = gallons * station.price_per_gallon
        total_cost += cost
        stops.append({
            "station": station.name,
            "location": [station.latitude, station.longitude],
            "cost": round(cost, 2)
        })
    return stops, round(total_cost, 2)