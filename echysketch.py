from turtle import Turtle, Screen


james = Turtle()
screen = Screen()


def m_forward():
    james.fd(10)


def m_backward():
    james.bk(10)


def m_c_clock():
    james.left(10)
    # or james.seth(james.heading() + 10)


def m_clock():
    james.right(10)
    # or james.seth(james.heading() - 10)


def clear_s():
    james.clear()
    james.pu()
    james.home()
    james.pd()


screen.listen()
screen.onkey(fun=m_forward, key="w")
screen.onkey(fun=m_backward, key="s")
screen.onkey(fun=m_c_clock, key="a")
screen.onkey(fun=m_clock, key="d")
screen.onkey(fun=clear_s, key="c")
screen.exitonclick()
