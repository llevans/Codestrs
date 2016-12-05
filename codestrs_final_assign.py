#####################################################################################
#  Name : codestrs_final_assign.py                                                  # 
#  Date : Dec 4, 2016                                                               # 
#  Description : Update the Flappy Bike game user interface to be more robust.      #
#                Write functions to move the bike when the user clicks the          #
#                up, down, left and right arrow keys.                               #
#                                                                                   #
#####################################################################################


stage.set_background("city")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

stage.set_gravity(10)
stage.disable_all_walls()

# Problem :
#  Update the Flappy Bike game more robust.
#  Implement Python functions for to manuever the sprite up, down, left and right 
#  Bind the functions to the 4 arrow key click events
# 
def handle_up_arrow():
    palceholder_code = 1

stage.event_key("up", handle_up_arrow)

def handle_down_arrow():
    palceholder_code = 1

stage.event_key("down", handle_down_arrow)

def handle_right_arrow():
    palceholder_code = 1

stage.event_key("right", handle_right_arrow)

def handle_left_arrow():
    palceholder_code = 1

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




