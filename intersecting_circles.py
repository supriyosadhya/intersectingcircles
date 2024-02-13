def count_intersections(radian_measures, identifiers):
    count = 0
    s_x = [0]*(int(len(identifiers)/2))
    e_x = [0]*(int(len(identifiers)/2))
    for i in range(len(radian_measures)):
        if identifiers[i].split('_')[0] == 's':
            s_x[int(identifiers[i].split('_')[1]) - 1] = radian_measures[i]
        else:
            e_x[int(identifiers[i].split('_')[1]) - 1] = radian_measures[i]
    
    for i in range(len(s_x)):
        for j in range(i+1,len(s_x)):
            one = (s_x[i] < s_x[j] < e_x[i])
            two = (s_x[i] < e_x[j] < e_x[i])
            result = False
            if one or two:
                result = True
            if one and two:
                result = False
            if result:
                count = count + 1
    return count

# # Example Input
# radian_measures_1 = [0.78, 1.47, 1.77, 3.92]
# identifiers_1 = ["s_1", "s_2", "e_1", "e_2"]

# radian_measures_2 = [0.9, 1.3, 1.7, 2.92]
# identifiers_2 = ["s_1", "e_1", "s_2", "e_2"]

radian_string = input("Enter radian measures(in floats) separated by spaces: ")
elements = radian_string.split()
radian_list = [(item) for item in elements]

identifier_string = input("Enter the chord itentifiers separated by spaces: ")
identifier_list = identifier_string.split()
intersections = count_intersections(radian_list, identifier_list)

print("Number of intersections in Example 2:", intersections)