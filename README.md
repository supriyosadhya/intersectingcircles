# intersecting circles
for runing the code download the .py file and run it using the command
python intersecting_cirlces.py
it will ask the user to input the radian measures separated by spaces and the identifiers separated by spaces. The program assumes the user inputs the data correctly.
The program uses the method count_intersections to count the number of intersections. At first the starting and end points of the chords is stored in two lists s_x and e_x in order. Then we compute the number of intersections based on the principle : two chords will intersect if either the start angle or end angle (but not both) of one of the chords is in between the start and end angles of the other. We write a nested loop for that purpose so that for each chord we compare it with other chords which were not compared before( to avoid repititions).
The big-O runtime of the code should be n^2.
