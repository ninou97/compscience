import math

def treasure():
    number_of_treasures = int(input("Number of treasures: "))
    alex_coords = input("Alex's coordinates: ").split()
    alex_coords = [int(x) for x in alex_coords]

    if len(alex_coords) != 2:
        print("wrong input")
        return


    treasure_map = [0] * number_of_treasures

    # fill treasure map
    for i in range(number_of_treasures):
        inputs = input(f"Treasure {i+1} - type x and y separated by space: ").split()
        inputs = [int(x) for x in inputs]

        if len(inputs) != 2:
            print("wrong input")
            return
        
        for j in range(2):
            inputs[j] = inputs[j] - alex_coords[j]

        treasure_map[i] = inputs

    # print(treasure_map)

    distances = [0] * number_of_treasures
    
    # find distance 
    for i in range(number_of_treasures):
        distances[i] = [math.sqrt((treasure_map[i][0])**2 + (treasure_map[i][1])**2), treasure_map[i]]

    # min distance
    min = [4200]
    for d in distances:
        if d[0] < min[0]:
            min = d

    print(min[1][0]+alex_coords[0], min[1][1]+alex_coords[1])
        


        



treasure()