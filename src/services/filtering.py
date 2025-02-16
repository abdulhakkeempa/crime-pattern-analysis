from geopy.distance import geodesic

def filter_by_location(results, user_lat, user_lon, radius_km):
    if not user_lat or not user_lon or not radius_km:
        return results
    
    filtered_results = []
    for match in results:
        complaint_location = match.get("location")
        if complaint_location:
            complaint_lat = complaint_location["lat"]
            complaint_lon = complaint_location["lon"]
            distance = geodesic((user_lat, user_lon), (complaint_lat, complaint_lon)).km
            if distance <= radius_km:
                filtered_results.append(match)
    return filtered_results