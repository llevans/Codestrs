import time

stage.set_background("grid")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

sprite.set_gravity_off()

click_counter = 0

def handle_space_key():
    global click_counter
    click_counter = click_counter + 1
    if click_counter % 2 != 0:
        sprite.set_x_speed(5)
    else:
        x = sprite.get_x()
        y = sprite.get_y()
        sprite.go_to(x, y)
    # add other actions...

stage.event_space_key(handle_space_key)

def handle_flip():
    rotate_angle = 0
    for x in range(1, 9):
        rotate_angle = rotate_angle + 45
        sprite.set_rotation(rotate_angle)
        time.sleep(.1)
    
stage.event_key("up", handle_flip)


#Problem :
# Make the bike jump vertically when the Enter key is clicked
def handle_jump():
    # Deterime the bicycle's x and y position (like lines 18,19)

    # Call the jump method from the Sprite API

    # Delay the program for 1/2 second

    # Move the bike back to it's original position (line 20)

stage.event_enter_key(handle_jump)





