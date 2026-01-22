This module provides solution for matching sets of GPS coordinates. 
Given two arrays of geographic locations (latitude and longitude), using the module we can identify the closest point in the second array for every point in the first array.
This implementation uses the Haversine Formula to account for the Earth's curvature, ensuring accurate distance calculations between coordinates.

This module requires python 3.9+
You can import the find_closest_matches function into your own project:from gps_matcher import find_closest_matches
