#bot1

# Move forward 
# Turn left 45º
# Move forward
# Turn right 90º
# Move forward to center
# Turn left 90º
def goToPoms(): # Position the bot to grab the poms
  forward()
  left()
  forward()
  right()
  forward()
  left()
def pickUpPoms(): # Pick up top 3 poms
  times = 3
  while times > 0:
    set_servo_position(,) # Move claw down
    set_servo_position(,) # Close claw
    set_servo_position(,) # Move claw up
    set_servo_position(,) # Open claw
    times--
# Move forward
# Turn left 90º
# Move forward
# Turn and pick up bottles with bottle claw
# Turn left 90º
# Move forward
def putPomsInTray(): # Deposit the poms into the tray
# Pick up and deposit the rest of the poms (optional)
# Turn left 90º
# Move forward
# Grab pickle
# Turn left 90º
# Move forward
# Turn right 90º
# Pick up tomato
# Turn around 180º
# Move forward
# Turn left 90º
# Move forward
# Turn right 90º
# Move forward

enable_servos()
goToPoms()
