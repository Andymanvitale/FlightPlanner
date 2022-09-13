import math

from geopy import distance

p1 = (43.668613, 40.258916, 0.976)

p2 = (43.658852, 40.250839, 1.475)

flat_distance = distance.distance(p1[:2], p2[:2]).km

print(flat_distance)