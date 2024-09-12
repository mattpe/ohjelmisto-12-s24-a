import math, locale
from geopy import distance

# select latitude_deg, longitude_deg from airport where ident='EFVU';

efhk_coords = (60.3172, 24.963301)
efvu_coords = (68.087196, 27.123899)
result_distance = distance.distance(efhk_coords, efvu_coords).km
print(result_distance)

# EXTRAA - tulostuksen muotoiluesimerkkejä:
#   korvataan desimaalipiste pilkulla eri keinoin
# 1. kokonaiset kilsat ja jämämetrit erikseen:
print(f"{math.floor(result_distance)},{result_distance%1*100:.0f} km")
# 2. korvataan merkkijonon pisteet pilkulla:
print(f"{result_distance:.2f} km".replace('.', ','))
# 3. asetetaan locale, ja muotoilla floatista stringi sen perusteella
locale.setlocale(locale.LC_ALL, 'fi_FI')
print(f"{locale.format_string('%.2f', result_distance)} km")
