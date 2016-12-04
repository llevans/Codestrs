#####################################################################################
#  Name : codestrs_grid.py                                                          # 
#  Date : Dec 4, 2016                                                               # 
#  Description : Render a bike sprite using the Codestrs online Python interpreter  # 
#                Move the bike forward at the Righ Arrow click event                # 
#####################################################################################

stage.set_background("grid")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

sprite.set_gravity_off()

click_counter = 0

def handle_pedal():
    global click_counter
    click_counter = click_counter + 1
    
    # If click on space bar is odd - start pedalling 
    if click_counter % 2 != 0:
        sprite.set_x_speed(5)

    # If click on space bar is even - stop pedalling 
    else:
        x = sprite.get_x()
        y = sprite.get_y()
        sprite.go_to(x, y)
    # add other actions...

stage.event_right_key(handle_pedal)







