//====================================================================================================
//The Free Edition of C++ to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-cplus-to-python.html
//====================================================================================================

import math

def main():
    gmode = DETECT
    gdriver = None
    area = None
    initgraph(gmode, gdriver, "c:\tc\bgi\ ")
    setbkcolor(1)
    Globals.start()
    maxx = getmaxx()
    maxy = getmaxy()
    p = 400
    q = 300
    m = 100
    n = 100
    x = m
    y = n
    key = None
    score = 0
    finish = 0
    level = 1
    l_flag = 1
    score1 = str(['\0' for _ in range(5)])
    ch = None
    cnt_ball = str(['\0' for _ in range(5)])
    char_level = str(['\0' for _ in range(2)])

    rectangle(0, 0, maxx, maxy - 10)

    Globals.draw_burst(200, 300)
    area = imagesize(0,0,32,24)
#C++ TO PYTHON CONVERTER TODO TASK: The memory management function 'malloc' has no equivalent in Python:
    Globals.burst = malloc(area)
    getimage(200-16,300-12,200+16,300+12,Globals.burst)
    putimage(200-16,300-12,Globals.burst,XOR_PUT)

    Globals.draw_balloon(p, q)

    area = imagesize(p-4 *DefineConstants.BALLOON_SIZE,q-5 *DefineConstants.BALLOON_SIZE,p+4 *DefineConstants.BALLOON_SIZE,q+7 *DefineConstants.BALLOON_SIZE)
#C++ TO PYTHON CONVERTER TODO TASK: The memory management function 'malloc' has no equivalent in Python:
    Globals.balloon = malloc(area)

    getimage(p-4 *DefineConstants.BALLOON_SIZE,q-5 *DefineConstants.BALLOON_SIZE,p+4 *DefineConstants.BALLOON_SIZE,q+7 *DefineConstants.BALLOON_SIZE,Globals.balloon)
    putimage(p-4 *DefineConstants.BALLOON_SIZE, q-5 *DefineConstants.BALLOON_SIZE, Globals.balloon, COPY_PUT)

    Globals.draw_arrow(x, y)
    area = imagesize(x, y-DefineConstants.ARROW_SIZE, x+(6 *DefineConstants.ARROW_SIZE), y+DefineConstants.ARROW_SIZE)
#C++ TO PYTHON CONVERTER TODO TASK: The memory management function 'malloc' has no equivalent in Python:
    Globals.arrow = malloc(area)
    getimage(x, y-DefineConstants.ARROW_SIZE, x+(6 *DefineConstants.ARROW_SIZE), y+DefineConstants.ARROW_SIZE,Globals.arrow)
    putimage(x, y-DefineConstants.ARROW_SIZE,Globals.arrow,XOR_PUT)

    Globals.draw_bow(x, y)
    area = imagesize(x+25,y-65,x+66,y+65)
#C++ TO PYTHON CONVERTER TODO TASK: The memory management function 'malloc' has no equivalent in Python:
    Globals.bow = malloc(area)
    getimage(x+25,y-65,x+66,y+65,Globals.bow)

    if Globals.balloon == None or Globals.burst == None or Globals.bow == None:
        printf("Insufficient memory... Press any key ")
        getch()
        closegraph()
        restorecrtmode()
        exit(0)
    # Downloaded from www.indiaexam.in
    while finish == 0:
        settextstyle(8,0,1)
        setusercharsize(4,4,3,3)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        outtextxy(getmaxx()/2-100,5,"LEVEL : ")
        itoa(level,char_level,10)
        setfillstyle(0,0)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        bar(getmaxx()/2+40,15,getmaxx()/2+70,45)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        outtextxy(getmaxx()/2+50,5,char_level)

        rectangle(5,360,250,460)

        if Globals.flag_balloon != 0 and Globals.count_balloon>0:
            temp_ref_p = RefObject(p);
            Globals.fly(temp_ref_p, q)
            p = temp_ref_p.arg_value
        else:
            q = 400
            Globals.flag_balloon = 1

        if kbhit():
            key = Globals.testkeys()
            if key == 77:
                Globals.flag_arrow = 1

        if key == 27:
            break
        if key == 80 and Globals.flag_arrow == 0:
            x = 125
            putimage(x,y-65,Globals.bow,XOR_PUT)
            if y<300:
                y+=25
            putimage(x,y-65,Globals.bow,XOR_PUT)
            Globals.draw_bow(x-25, y)
            key = 0
        if key == 72 and Globals.flag_arrow == 0:
            x = 125
            putimage(x,y-65,Globals.bow,XOR_PUT)
            if y>70:
                y-=25
            putimage(x,y-65,Globals.bow,XOR_PUT)
            Globals.draw_bow(x-25, y)
            key = 0
        if Globals.count_arrow > 0 and Globals.count_balloon > 0:
            if score == 100 and l_flag == 1:
                level = 2
                Globals.count_balloon = 8
                Globals.count_arrow = 6
                l_flag = 2
            if score == 180 and l_flag == 2:
                level = 3
                Globals.count_balloon = 6
                Globals.count_arrow = 6
                l_flag = 0

//====================================================================================================
//End of the allowed output for the Free Edition of C++ to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-cplus-to-python.html
//====================================================================================================
