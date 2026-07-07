# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return '<{}, {}>'.format(self.x, self.y)
    
#     def distance(self, other):
#         return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
    
#     def distance_from_origin(self):
#         distance = (self.x**2 + self.y**2)**0.5
#         return distance
    
#     def distance_from_line(self, a, b, c):
#         return (abs(a*self.x + b*self.y + c)) / (a**2 + b**2)**0.5
    
#     def lies_on_line(self, a, b, c):
#         is_lies = a * self.x + b * self.y + c
#         if is_lies == 0:
#             return "Lies on the Line"
#         else:
#             return "Does not lie on the Line"

# p1 = Point(0, 0)
# p2 = Point(1, 1)
# print(p1, p2)

# print(p1.distance(p2)) 

# print(p2.distance_from_origin())

# print(p2.distance_from_line(1, 1, -2))

# print(p2.lies_on_line(1, 1, -2))

# print(p2.distance_from_line(1,1,-2))


# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

# class Line:
#     def __init__ (self, A, B, C):
#         self.A = A
#         self.B = B
#         self.C = C
    
#     def intersect (self, other):
#         determinant = self.A * other.B - other.A * self.B
#         if determinant == 0:
#             if (self.A * other.B - self.B * other.A) / self.B * other.B == self.C / other.C:
#                 return "Lines are coincident"
#             else:
#                 return "Lines are Parallel"
#         else:
#             return "Intersects!!!"

# line1 = Line(2, 0, 6)
# line2 = Line(4, 0, 12)

# print(line1.intersect(line2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Location:
    def __init__(self, location, destination):
        self.location = location
        self.destination = destination

    def reflect_destination_on_x_axis(self):
        reflected_x = self.destination.x
        reflected_y = -self.destination.y
        print(f"Reflected point on x-axis: ({reflected_x}, {reflected_y})")

# Example usage
location_point = Point(1, 2)
destination_point = Point(3, 4)
location = Location(location_point, destination_point)

location.reflect_destination_on_x_axis()



