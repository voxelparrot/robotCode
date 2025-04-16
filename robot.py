#bot1
def pickUpPoms():
  times = 5
  while times > 0:
    set_servo_position(,) # Move claw down
    set_servo_position(,) # Close claw
    set_servo_position(,) # Move claw up
    set_servo_position(,) # Open claw
    times--
  
def goToPoms(): # Position the bot to grab the poms
  forward()
  left()
  forward()
  right()
  forward()
  left()

def putPomsInTray(): # Deposit the poms into the tray
  
  
enable_servos()
goToPoms()













