import pgzrun, random
RADIUS = 300
Title = "Gradient Circle"
def draw():
    rad = RADIUS
    r = random.randint(0,255)
    g = 0
    b = 255
    for i in range(10):
        circle =Circle(0,0,rad,rad)
        rad=rad-20
        screen.draw.circle(circle, (r,g,b))
pgzrun.go()