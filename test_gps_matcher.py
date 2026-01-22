import pytest
from gps_matcher import haversine_distance, find_closest_matches

def test_distance_calculation():
    # Distance between Boston (42.3601, -71.0589) and NYC (40.7128, -74.0060)
    # is roughly 306 km
    boston = (42.3601, -71.0589)
    nyc = (40.7128, -74.0060)
    dist = haversine_distance(boston, nyc)
    assert 300 < dist < 310

def test_closest_matching():
    list_a = [(42.3601, -71.0589)] # Boston
    list_b = [(40.7128, -74.0060), (34.0522, -118.2437)] # NYC and LA
    
    matches = find_closest_matches(list_a, list_b)
    
    # checking to see if it shows NYC as the closest point to Boston
    assert matches[0][1] == (40.7128, -74.0060)