from robot_control_class import RobotControl

rc = RobotControl()

laser = rc.get_laser(49)
if laser < 3: #wall_is_close
    rc.stop_robot() 
    
else:
    rc.move_straight()
    
print ("The laser value received was: ", laser)