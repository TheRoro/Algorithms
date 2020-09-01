class Coordinate(object):
    def __init__(self, point, is_start, height):
        self.point = point
        self.is_start = is_start
        self.height = height
    
    def __lt__(self, other):
            if self.point != other.point:
                return self.point < other.point
            else:
                if self.is_start:
                    h1 = -self.height
                else:
                    h1 = self.height

                if other.is_start:
                    h2 = -other.height
                else:
                    h2 = other.height

                return h1 < h2

def generateSkyline(buildings):
    coordinates = []
    for building in buildings:
        coordinates.append(Coordinate(building[0], True, building[1])) #Starting point
        coordinates.append(Coordinate(building[2], False, building[1])) #Ending point

    coordinates = sorted(coordinates)

    

    return coordinates

if __name__ == '__main__':
    buildings = [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22]]
    ans = generateSkyline(buildings)
    for building in ans:
        print("(", building.point, ",", building.height, ")", building.is_start)


