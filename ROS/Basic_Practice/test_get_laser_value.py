from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(60)

print ("The distance measured is: ", a, " m.")

laser1 = rc.get_laser(0)
print ("The laser1 value received is: ", laser1)

laser2 = rc.get_laser(49)
print ("The laser2 value received is: ", laser2)

laser2 = rc.get_laser(99)
print ("The laser3 value received is: ", laser2)

l = rc.get_laser_full()

print ("Position 0: ", l[0])
print ("Position 49: ", l[49])
print ("Position 99: ", l[99])

# Make the laser values in dictionary format
dict = {"P0": l[0], "P10": l[10], "P20": l[20], "P30": l[30], "P40": l[40], "P50": l[50], "P60": l[60],"P70": l[70], "P80": l[80],"P90": l[90], "P99": l[99]}

print (dict)
