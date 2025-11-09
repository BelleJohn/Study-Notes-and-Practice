from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")
rc.get_laser_summit
def get_laser_values(a, b, c):
    la = rc.get_laser_summit(a)
    lb = rc.get_laser_summit(b)
    lc = rc.get_laser_summit(c)
    return[la, lb, lc]

ls = get_laser_values(0, 100, 199)

print("Reading 1",  ls[0])
print("Reading 2",  ls[1])
print("Reading 3",  ls[2])