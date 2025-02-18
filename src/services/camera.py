from geopy.distance import geodesic

# Camera locations (CUSAT - Kalamassery area)
cameras = [
    {"id": 1, "lat": 10.0261, "lng": 76.3125, "name": "Camera 1"},
    {"id": 2, "lat": 10.0280, "lng": 76.3150, "name": "Camera 2"},
    {"id": 3, "lat": 10.0480, "lng": 76.3256, "name": "CUSAT Main Gate"},
    {"id": 4, "lat": 10.0445, "lng": 76.3280, "name": "CUSAT Administrative Block"},
    {"id": 5, "lat": 10.0458, "lng": 76.3202, "name": "CUSAT Library Junction"},
    {"id": 6, "lat": 10.0409, "lng": 76.3268, "name": "CUSAT Science Block"},
    {"id": 7, "lat": 10.0502, "lng": 76.3225, "name": "Kalamassery Metro Station"},
    {"id": 8, "lat": 10.0471, "lng": 76.3186, "name": "Athulya IT Park Entrance"},
    {"id": 9, "lat": 10.0513, "lng": 76.3199, "name": "HMT Junction"},
    {"id": 10, "lat": 10.0432, "lng": 76.3235, "name": "CUSAT Men's Hostel Road"},
    {"id": 11, "lat": 10.0467, "lng": 76.3301, "name": "School of Engineering Entrance"},
    {"id": 12, "lat": 10.0490, "lng": 76.3289, "name": "Kalamassery Municipal Office"},
    {"id": 13, "lat": 10.0521, "lng": 76.3214, "name": "Kalamassery Railway Station"},
    {"id": 14, "lat": 10.0415, "lng": 76.3198, "name": "Kalamassery Police Station"},
    {"id": 15, "lat": 10.0462, "lng": 76.3174, "name": "Athulya Junction"},
    {"id": 16, "lat": 10.0389, "lng": 76.3253, "name": "NPOL Main Gate"},
    {"id": 17, "lat": 10.0448, "lng": 76.3161, "name": "Rajagiri Hospital Road"},
    {"id": 18, "lat": 10.0487, "lng": 76.3323, "name": "Kalamassery Town Junction"},
    {"id": 19, "lat": 10.0396, "lng": 76.3218, "name": "CUSAT Back Gate"},
    {"id": 20, "lat": 10.0517, "lng": 76.3282, "name": "Kalamassery Industrial Estate"},
    {"id": 21, "lat": 10.0375, "lng": 76.3227, "name": "Kendriya Vidyalaya CUSAT"},
    {"id": 22, "lat": 10.0508, "lng": 76.3179, "name": "HMT Colony"}
]

def find_cameras_in_radius(lat, lng, radius_km):
    """
    Find cameras within a given radius (in km) from the input latitude and longitude.

    :param lat: Latitude of the input location
    :param lng: Longitude of the input location
    :param radius_km: Search radius in kilometers
    :return: List of cameras within the given radius
    """
    input_location = (lat, lng)
    nearby_cameras = []

    for camera in cameras:
        camera_location = (camera["lat"], camera["lng"])
        distance = geodesic(input_location, camera_location).km  # Compute distance

        if distance <= radius_km:
            nearby_cameras.append({**camera, "distance_km": round(distance, 2)})

    return sorted(nearby_cameras, key=lambda x: x["distance_km"])  # Sort by distance

# Example Usage
lat, lng = 10.0400, 76.3200  # Example location near CUSAT
radius_km = 1  # Search radius in km
nearby_cameras = find_cameras_in_radius(lat, lng, radius_km)
print(nearby_cameras)  