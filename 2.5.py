import turtle as t

ls=[69,292,33,131,61,254]
X_len=400
Y_len=300
x0=-200
y0=-100

t.penup()
t.goto(x0,y0)
t.pendown()

t.fd(X_len)
t.fd(-X_len)
t.seth(90)
t.fd(Y_len)


for i in range(len(ls)):
    t.color("red")
    t.penup()
    t.goto(x0+(i+1)*50,y0 )
    t.seth(90)
    t.pendown()
    t.begin_fill()
    t.pensize(1)
    t.pencolor('red')
    t.fd(ls[i])
    t.seth(0)
    t.fd(20)
    t.seth(-90)
    t.fd(ls[i])
    t.end_fill()
t.done()