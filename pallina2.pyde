xpos=0
ypos=0
xVers=+1
yVers=+1
rag=50
xrac=0
xrac2=0
yrac2=0
punt1=0
punt2=0
a=b=c=255
def setup ():
    global xpos, ypos
    xpos=10
    ypos=100
    size(900,600)
    background(255)
    
def draw():
    global xpos,ypos,xVers,yVers,rag, xrac, xrac2, yrac2, punt1, punt2,a,b,c
    background(255)
    
    if xpos >width or xpos<0:
        xVers=xVers*(-1)
        a=random(0,255)
        b=random(0,255)
        c=random(0,255)
    fill(a,b,c)
    


    if ypos >height-25 or ypos<+25:
        yVers=yVers*(-1)
        a=random(0,255)
        b=random(0,255)
        c=random(0,255)
    fill(a,b,c)
    
    ellipse(xpos,ypos,rag,rag)
    xpos=xpos+xVers*4
    ypos=ypos+yVers*4
        
    rect(xrac,575,100,25)
    if ypos > height-(rag/2):
        print("GIOCATORE 1 hai perso")
        punt2=punt2+1
        
    if ypos > height-(25+rag/2) and xrac < xpos < xrac+100:
        yVers=yVers*(-1)

    
    rect(xrac2,yrac2,100,25)
    if ypos < 0+(rag/2):
        print("GIOCATORE 2 hai perso")
        punt1=punt1+1
        
    if ypos < 0+(25+rag/2) and xrac2 < xpos < xrac2+100:
        yVers=yVers*(-1)
        
    fill(0,0,0)
    textSize(20)
    text(punt2,xrac2+40,yrac2+20)
    
    fill(0,0,0)
    textSize(20)
    text(punt1,xrac+40,595)

    
    
    
def keyPressed():
    global xpos,ypos,xVers,yVers,rag, xrac, xrac2, yrac2;
    print("premuto")
    if keyCode==LEFT:
        xrac=xrac-20
    if keyCode==RIGHT:
        xrac=xrac+20
    if key=="z":
        xrac2=xrac2-20
    if key=="x":
        xrac2=xrac2+20
