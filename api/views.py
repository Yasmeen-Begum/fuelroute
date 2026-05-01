# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_route
from .services import calculate_fuel_stops

class RoutePlanner(APIView):
    def post(self, request):
        start = request.data.get("start")   # [lon, lat]
        finish = request.data.get("finish") # [lon, lat]
        api_key = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImM2ZDEyZWY0N2Q5NTQ1NjA4MDI4MmNmOGMzMmNmMjMyIiwiaCI6Im11cm11cjY0In0="

        route = get_route(start, finish, api_key)
        fuel_stops, total_cost = calculate_fuel_stops(route)

        return Response({
            "route": route,
            "fuel_stops": fuel_stops,
            "total_cost": total_cost
        })