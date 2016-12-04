stage.set_background("grid")
sprite = codesters.Sprite("bike")
sprite.set_size(0.4)
sprite.go_to(-200, 0)

stage.set_gravity(10)
stage.disable_all_walls()

def space():
    sprite.jump(5)
    # add other actions...
stage.event_space_key(space)

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




