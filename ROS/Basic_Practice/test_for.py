from robot_control_class import RobotControl

rc = RobotControl

laser = rc.get_laser_full()

maxim = 0

for value in laser:
    if value > maxim:
        maxim = value
print("The higher value in the list is:", maxim)