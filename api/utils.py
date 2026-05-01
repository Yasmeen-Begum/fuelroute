# api/utils.py
import openrouteservice
def get_route(start, finish, api_key):
    client = openrouteservice.Client(key=api_key)
    route = client.directions(
        coordinates=[start, finish],
        profile='driving-car',
        format='geojson'
    )
    return route