
## 实现H-树分形
import turtle


def drawH(x,y,length):
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(x,y)
        turtle.speed(10)
        turtle.backward(length/2)
        turtle.pendown()
        turtle.forward(length)
        turtle.penup()
        turtle.goto(x-length/2,y+length/2)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(length)
        turtle.penup()
        turtle.goto(x+length/2,y+length/2)
        turtle.pendown()
        turtle.forward(length)
        


def displayHShape(order,x,y,length):
        if order>=0:
                drawH(x,y,length)

                xleft=x-length/2
                xright=x+length/2
                yup=y+length/2
                ydown=y-length/2

                displayHShape(order - 1,xleft,yup,length/2)
                displayHShape(order - 1,xleft,ydown,length/2)
                displayHShape(order - 1,xright,yup,length/2)
                displayHShape(order - 1,xright,ydown,length/2)
                
        
def main():
        order=eval(input("请输入阶数："))
        displayHShape(order,0,0,200)
        
main()
    
    
