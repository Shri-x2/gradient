import pgzrun, random
RADIUS = 200
WIDTH, HEIGHT = 400, 400
Title = "Gradient Circle"
def draw():
    rad = RADIUS
    r = random.randint(0,255)
    g = 0
    b = 255
    for i in range(10):
        # circle =Circle(0,0,rad,rad)
        rad=rad-20
        screen.draw.filled_circle((200,200),rad, (r,g,b))
        g=g+25
        b=b-25
pgzrun.go()