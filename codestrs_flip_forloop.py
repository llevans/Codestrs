#####################################################################################
#  Name : codestrs_flip_forloop.py                                                  # 
#  Date : Dec 4, 2016                                                               # 
#  Description : Render a bike sprite using the Codestrs online Python interpreter  # 
#                Move the bike forward at the Righ Arrow click event                # 
#                Solution to convert logic that flips the bike backwards            #
#                360 degrees at the Left Arrow click event to a Python for loop     # 
#####################################################################################
import time

stage.set_background("grid")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

sprite.set_gravity_off()

click_counter = 0

def handle_pedal():
    global click_counter
    click_counter = click_counter + 1
    if click_counter % 2 != 0:
        sprite.set_x_speed(5)
    else:
        x = sprite.get_x()
        y = sprite.get_y()
        sprite.go_to(x, y)
    # add other actions...

stage.event_right_key(handle_pedal)

# Solution :
# Assigne the initial rotation angle to 45 degrees
# In a for loop for 10 iterations, increase the rotation by 45 degress
# Call time.sleep(.1)
def handle_flip():
    rotate_angle = 0
    for x in range(1, 9):
        rotate_angle = rotate_angle + 45
        sprite.set_rotation(rotate_angle)
        time.sleep(.1)
    
stage.event_key("left", handle_flip)






