import turtle
def runner_detour():
    t = turtle.Pen(shape = "turtle")
    t.color("blue")
    t.speed('slow')
    t.delay(10)
    t.forward(500)
    t.onclick(t.circle(5))
    t.goto(0,0)
    
