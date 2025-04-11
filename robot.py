#bot1
def pickUpPoms():
  times = 5
  while times > 0:
    set_servo_position(,) #claw down
    set_servo_position(,) #claw close
    set_servo_position(,) #claw up
    set_servo_position(,) #claw open
    times--
  
def goToPoms1():
  forward()
  left()
  forward()
  right()
  forward()
  left()

def putPomsInTray():
  
  
enable_servos()
goToPoms1()


