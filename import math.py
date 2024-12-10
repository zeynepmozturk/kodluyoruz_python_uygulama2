import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# 2. Öklid Mesafesi İçin Fonksiyon
def euclideanDistance(point1, point2):
    # Öklid mesafesi: √((x2 - x1)^2 + (y2 - y1)^2)
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)
print(f"Minimum Mesafe: {min_distance}")
