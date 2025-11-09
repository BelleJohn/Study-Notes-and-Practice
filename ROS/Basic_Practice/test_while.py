from robot_control_class import RobotControl

rc = RobotControl()

laser = rc.get_laser(49)

while laser > 3: #wall_is_close
    rc.move_straight()
    laser = rc.get_laser(49)
    print ("The laser value received was: ", laser)

rc.stop_robot() 

print ("Outside the loop!")