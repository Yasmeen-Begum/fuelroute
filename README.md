# Fuel Route Optimizer API

A Django REST API that calculates the optimal fueling strategy for a vehicle traveling between two locations in the USA.  
The API returns:
- The driving route (via a free routing API).
- Recommended fuel stops along the route (based on cost effectiveness).
- Total fuel cost for the trip.

---

## Features
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

##  Requirements
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
## Setup
- Clone the repo
```
git clone https://github.com/Yasmeen-Begum/fuelroute.git
cd fuelroute
```
- Create virtual environment
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
- Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
- Load fuel price data Place fuel-prices-for-be-assessment.csv in the project root, then run:
```
python manage.py load_fuel_data
```
- Add your OpenRouteService API key
- Sign up at OpenRouteService (openrouteservice.org in Bing).
- Replace "YOUR_OPENROUTESERVICE_KEY" in api/views.py with your key.
- Start server
```
python manage.py runserver
```
## API Usage
-Endpoint
```
POST /route/
```
Request Body
```
{
  "start": [-74.006, 40.7128],   // New York
  "finish": [-87.6298, 41.8781]  // Chicago
}
```
Example Response
```
{
  "route": {
    "distance_miles": 790,
    "map_url": "https://maps.openrouteservice.org/?..."
  },
  "fuel_stops": [
    {"station": "Shell NY", "location": [40.7, -74.0], "cost": 150.25},
    {"station": "BP OH", "location": [41.0, -82.0], "cost": 120.75}
  ],
  "total_cost": 271.00
}
```


