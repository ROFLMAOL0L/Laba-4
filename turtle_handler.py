#x = [-7,-5,-3,-1,1,3,5,7,9,11]
#y = [2,1,4,2,-4,4,6,8,4,2]
#n = 'какая-то формула'
#file_name = 'название файла'
def deit(x, y, n, file_name): #data entry in turtle
    if (not isinstance(x, list)) and (not isinstance(y, list)):
        return('Error: y and x are not lists')
    elif not isinstance(x, list):
        return('Error: x is not a list')
    elif not isinstance(y, list):
        return('Error: y is not a list')
    elif (len(x) <= 1) and (len(y) <= 1):
        return('Error: the lengths of x and y lists are 0 or 1')
    elif len(x) <= 1:
        return('Error: list length x is 0 or 1')
    elif len(y) <= 1:
        return('Error: list length y is 0 or 1')
    elif len(x) != len(y):
        return('Error: lists x and y are not the same length')
    elif not isinstance(n, str):
        return('Error: n is not a string')
    elif (n == '') or (n == ' '):
        return('Error: n is an empty string')
    elif not isinstance(file_name, str):
        return('Error: file_name is not a string')
    elif (file_name == '') or (file_name == ' '):
        return('Error: file_name is an empty string')
    else:
        #print(x)
        #print(y)
        #print(n)
        x_amp = max(x)-min(x)
        y_amp = max(y)-min(y)
        dx = 1600/x_amp
        dy = 900/y_amp
        min_x = min(x)
        min_y = min(y)
            
        import turtle
        turtle.title('y = ' + n)
        bg = turtle.Turtle()
        bg.hideturtle()
        bg.speed(0)
        bg.up()
        bg.goto(-830,-480)
        bg.down()
        bg.goto(-830,480)
        bg.goto(830,480)
        bg.goto(830,-480)
        bg.goto(-830,-480)

        if min(x) <= 0 and max(x) >= 0:
            yl = turtle.Turtle()
            yl.hideturtle()
            yl.speed(0)
            yl.pencolor('green')
            yl.up()
            yl.goto(((0-min_x)*dx)-800,-480)
            yl.down()
            yl.goto(((0-min_x)*dx)-800,480)

        if min(y) <= 0 and max(y) >= 0:
            xl = turtle.Turtle()
            xl.hideturtle()
            xl.speed(0)
            xl.pencolor('red')
            xl.up()
            xl.goto(-830,((0-min_y)*dy)-450)
            xl.down()
            xl.goto(830,((0-min_y)*dy)-450)
                
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.up()
        t.goto(((x[0]-min_x)*dx)-800,((y[0]-min_y)*dy)-450)
        t.down()
        t.dot()
        for i in range(1,len(x)):
            t.goto(((x[i]-min_x)*dx)-800,((y[i]-min_y)*dy)-450)
            t.dot()
        turtle.mainloop()
#deit(x, y, n, file_name)
