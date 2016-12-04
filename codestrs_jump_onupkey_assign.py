#######################################################################################
#  Name : codestrs_jump_onupkey_assign.py                                             # 
#  Date : Dec 4, 2016                                                                 # 
#  Description : Render a bike sprite using the Codestrs online Python interpreter    # 
#                Move the bike forward at the Righ Arrow click event                  # 
#                Assignment to have the bike jump upwards at the Up Arrow click event #
*                                                                                     #   
#######################################################################################
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

def handle_flip():
    rotate_angle = 0
    for x in range(1, 9):
        rotate_angle = rotate_angle + 45
        sprite.set_rotation(rotate_angle)
        time.sleep(.1)
    
stage.event_key("left", handle_flip)


#Problem :
# Make the bike jump vertically when the Enter key is clicked
def handle_jump():
    # Deterime the bicycle's x and y position (like lines 18,19)

    # Call the jump method from the Sprite API

    # Delay the program for 1/2 second

    # Move the bike back to it's original position (line 20)

stage.event_key("up", handle_jump)





