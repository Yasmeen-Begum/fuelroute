# Fuel Route Optimizer API

A Django REST API that calculates the optimal fueling strategy for a vehicle traveling between two locations in the USA.  
The API returns:
- The driving route (via a free routing API).
- Recommended fuel stops along the route (based on cost effectiveness).
- Total fuel cost for the trip.

---

## 🚀 Features
- Built with **latest stable Django** + Django REST Framework.
- Uses **OpenRouteService** (free API) for routing.
- Loads fuel price data from the provided CSV file.
- Vehicle constraints:
  - Maximum range: **500 miles per tank**.
  - Fuel efficiency: **10 miles per gallon**.
- Minimizes external API calls (one route call per request).
- Fast response time with local fuel price lookups.
- Demonstrated via Postman + Loom walkthrough.

---

## 📦 Requirements
- Python ≥ 3.11
- Django ≥ 5.x
- Django REST Framework
- pandas
- requests
- openrouteservice

Install dependencies:
```
pip install -r requirements.txt
```
