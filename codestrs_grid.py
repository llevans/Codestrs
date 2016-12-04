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

stage.event_space_key(handle_pedal)







