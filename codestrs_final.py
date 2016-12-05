#####################################################################################
#  Name : codestrs_final.py                                                         # 
#  Date : Dec 4, 2016                                                               # 
#  Description : Solution to updating the Flappy Bike game user interface.          #
#                The hanlde_**_arrow functions allow the player to move the bike    #
#                when he/she clicks the up, down, left and right arrow keys.        #
#                                                                                   #
#####################################################################################
stage.set_background("city")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

stage.set_gravity(10)
stage.disable_all_walls()

def handle_up_arrow():
    sprite.set_y_speed(4)

stage.event_key("up", handle_up_arrow)

def handle_down_arrow():
    sprite.set_y_speed(-4)

stage.event_key("down", handle_down_arrow)

def handle_right_arrow():
    sprite.set_x_speed(4)

stage.event_key("right", handle_right_arrow)

def handle_left_arrow():
    sprite.set_x_speed(-4)

stage.event_key("left", handle_left_arrow)

def interval():
    # sprite = codesters.Rectangle(x, y, width, height, "color")
    top_height = random.randint(50, 300)
    top_block = codesters.Rectangle(300, 0, 100, top_height, "blue")
    top_block.set_gravity_off()
    top_block.set_top(250)
    
    bot_height = 350 - top_height
    bot_block = codesters.Rectangle(300, 0, 100, bot_height, "blue")
    bot_block.set_gravity_off()
    bot_block.set_bottom(-250)
    
    top_block.set_x_speed(-2)
    bot_block.set_x_speed(-2)
    # add any other actions...
stage.event_interval(interval, 5)

def collision(sprite, hit_sprite):
    sprite.go_to(0,0)
    text = codesters.Text("Game Over!", 0, 100, "yellow")
sprite.event_collision(collision)




