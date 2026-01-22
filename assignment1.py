import math

def haversine_distance(coord1, coord2):
    # Earth radius
    R = 6371.0

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # decimal to radians 
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def find_closest_matches(array1, array2):
    if not array1 or not array2:
        return []

    results = []
    for p1 in array1:
        closest_point = None
        min_dist = float('inf')

        for p2 in array2:
            dist = haversine_distance(p1, p2)
            if dist < min_dist:
                min_dist = dist
                closest_point = p2
        
        results.append((p1, closest_point, min_dist))
    
    return results