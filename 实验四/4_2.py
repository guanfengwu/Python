
import turtle, time
 
 
def drawline(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
 
def drawGap():
    turtle.penup()
    turtle.fd(5) 
 
def drawDigit(digit):
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
 
 
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年', font=('Arial', 20, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=('Arial', 20, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=('Arial', 20, 'normal'))
        else:
            drawDigit(eval(i))
 
 
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.pensize(5)
    turtle.speed(10)
    turtle.fd(-300)
    turtle.pendown()
    drawDate(time.strftime('%Y-%m=%d+', time.localtime()))
    turtle.hideturtle()
    turtle.done()
main()
