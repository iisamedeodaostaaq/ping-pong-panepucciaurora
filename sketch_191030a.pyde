xpos=0               #coordinata x della pallina
ypos=0               #coordinata y della pallina
xVers=+1             #direzione x della pallina
yVers=+1             #direzione y della pallina
rag=50               #raggio della pallina
xrac=0               #coordinata x racchetta 1
xrac2=0              #coordinata x racchetta 2
yrac2=0              #coordinata y racchetta 2
punt1=0              #contatore punteggio racchetta 1
punt2=0              #contatore punteggio racchetta 2
a=b=c=255            #rgb


#INIZIALIZZA IL FOGLIO
def setup ():
    global xpos, ypos
    xpos=10
    ypos=100
    size(900,600)
    background(255)

    
def draw():
    global xpos,ypos,xVers,yVers,rag, xrac, xrac2, yrac2, punt1, punt2,a,b,c
    background(255)
    
    #MOVIMENTO PALLINA
        if xpos >width or xpos<0:             #se tocca i margini laterali  
        xVers=xVers*(-1)                  #cambia verso della x, la y resta invariata
        a=random(0,255)           
        b=random(0,255)
        c=random(0,255)
    fill(a,b,c)                           #genera tre numeri casuali per creare un nuovo rgb
    


    if ypos >height-25 or ypos<+25:      #se tocca il margine superiore o inferiore
        yVers=yVers*(-1)                 #cambia verso la y, la x resta invariata
        a=random(0,255)
        b=random(0,255)
        c=random(0,255)
    fill(a,b,c)                          #genera tre numeri casuali per creare un nuovo rgb
    
    
    #SPOSTAMENTO PALLINA
    ellipse(xpos,ypos,rag,rag)           #genera la pallina
    xpos=xpos+xVers*4                    #incremento x e y creando lo spostamento 
    ypos=ypos+yVers*4
    
        
    #FUNZIONI RACCHETTA GIOCATORE 1 (MARGINE INFERIORE)
    rect(xrac,575,100,25)                #inizializza la racchetta
    if ypos > height-(rag/2):            #se la pallina tocca il margine inferiore
        print("GIOCATORE 1 hai perso")   #stampa
        punt2=punt2+1                    #incrementa il punteggio del giocatore 2
        
    if ypos > height-(25+rag/2) and xrac < xpos < xrac+100:      #se tocca la racchetta 1
        yVers=yVers*(-1)                                         #cambia il verso della pallina
    
    if xrac > (width - 100):             #se la racchetta raggiunge il margine destro
        xrac=xrac-20                     #torna indietro in modo da non uscire dal foglio
        
    if xrac < 0:                         #se la racchetta raggiunge il margine sinistro
        xrac=xrac+20                     #torna avanti in modo da non uscire dal foglio
    
    
    #FUNZIONI RACCHETTA GIOCATORE 2 (MARGINE SUPERIORE)
    rect(xrac2,yrac2,100,25)            #inizializza la racchetta
    if ypos < 0+(rag/2):                #se la pallina tocca il margine superiore
        print("GIOCATORE 2 hai perso")  #stampa
        punt1=punt1+1                   #incrementa il punteggio del giocatore 1
        
    if ypos < 0+(25+rag/2) and xrac2 < xpos < xrac2+100:        #se tocca la racchetta 2
        yVers=yVers*(-1)                                        #cambia il verso della pallina
    
    if xrac2 > (width - 100):            #se la racchetta raggiunge il margine destro
        xrac2=xrac2-20                     #torna indietro in modo da non uscire dal foglio
        
    if xrac2 < 0:                         #se la racchetta raggiunge il margine sinistro
        xrac2=xrac2+20                     #torna avanti in modo da non uscire dal foglio
        
    
    #PUNTEGGIO GIOCATORI
    
    #giocatore 1
        
    fill(0,0,0)                         #colore font
    textSize(20)                        #dimensione font
    text(punt2,xrac2+40,yrac2+20)       #inizializza il testo e lo posiziona in corrispondenza 
                                        #della racchetta 1
    
    if punt1 == 10:                      #se il punteggio giocatore 1 arriva a 10
        fill (0,0,0)                     
        textSize(60)
        background(255)
        text("GIOCATORE 1 HAI VINTO", 100,300)   #stampa
        xpos=0                                   #inizializza la posizione della pallina
        ypos=0
        textSize(20)
        text("premere x con il cursore per uscire", 50, 500)        


    #giocatore 2
    
    fill(0,0,0)                         #colore font
    textSize(20)                        #dimensione font
    text(punt1,xrac+40,595)             #inizializza il testo e lo posiziona in corrispondenza
                                        #della racchetta 2

    if punt2 == 10:                             #se il punteggio giocatore 2 arriva a 10
        fill (0,0,0)                            #stampa
        textSize(60)
        background(255)
        text("GIOCATORE 1 HAI VINTO", 100,300)
        xpos=0
        ypos=0
        textSize(20)
        text("premere x con il cursore per uscire", 50, 500)

   


    
#COMANDI PRESSIONE-AZIONE DA TASTIERA    
def keyPressed():
    global xpos,ypos,xVers,yVers,rag, xrac, xrac2, yrac2;
    print("premuto")
    
    #PULSANTI COMANDI RACCHETTA GIOCATORE 1
    
    if keyCode==LEFT:                   #premendo la freccia sinistra da tastiera
        xrac=xrac-20                    #decrementa la x della racchetta 1
    
    if keyCode==RIGHT:                  #premendo la freccia destra da tastiera
        xrac=xrac+20                    #incrementa la x della racchetta 1
        
    #PULSANTI COMANDI RACCHETTA GIOCATORE 2
    
    if key=="z":                        #premendo il tasto z da tastiera
        xrac2=xrac2-20                  #decrementa la x della racchetta 2
        
    if key=="x":                        #premendo il tasto x da tastiera
        xrac2=xrac2+20                  #incrementa la x della racchetta 2
        
