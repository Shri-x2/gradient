import pgzrun, random
WIDTH, HEIGHT, TITLE = 400, 400, "Gradient" 

def draw():
    w = 350
    h = 100
    r=random.randint(0, 255)
    g=0
    b=255
    for i in range(15):
        rec=Rect(0, 0, w,h)
        rec.center= (WIDTH / 2, HEIGHT / 2)
        screen.draw.rect(rec, (r, g, b))
        w= w-10
        h=h+10
        g=g+10
        b=b-10
pgzrun.go()