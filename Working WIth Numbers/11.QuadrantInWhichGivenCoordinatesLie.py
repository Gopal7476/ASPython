# find out the quadrant in which the given co-ordinate lie.

x_axis, y_axis = map(int,input().split())
if(x_axis > 0 and y_axis > 0):
    print("First Quadrant")
elif(x_axis < 0 and y_axis > 0):
    print("Second Quadrant")
elif(x_axis < 0 and y_axis < 0):
    print("Third Quadrant")
elif(x_axis > 0 and y_axis < 0):
    print("Fourth Quadrant")
elif(x_axis == 0 and y_axis == 0):
    print("Origin")
elif(x_axis != 0 and y_axis == 0):
    print("Lies in X-axis")
else:
    print("Lies in Y-axis")