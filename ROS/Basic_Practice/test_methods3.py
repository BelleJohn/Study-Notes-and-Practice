from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")

msg1 = rc.move_straight_time("forward", 0.3, 5)
print(msg1)
msg2 = rc.turn("clockwise", 0.3, 7)
print(msg2)
