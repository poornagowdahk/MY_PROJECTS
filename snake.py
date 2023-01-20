PLAYGROUND_WIDTH=300
PLAYGROUND_HEIGHT=200
PLAYGROUND_COLOR='powder blue'
SNAKE_HEAD_COLOR='green'
SNAKE_BODY_COLOR='green'
SNAKE_MOVING_SPEED=10

# importiere module
try:
    import Tkinter
except:
    import tkinter as Tkinter

import time, random

# Unsere Hauptklasse
class main(Tkinter.Tk):
    # Unsere Initialisierungsfunktion, ruft alle anderen Initialisierungsfunktionen auf
    def __init__(self, *args, **kwargs):
           Tkinter.Tk.__init__(self, *args, **kwargs)
           self.creating_playground()
           self.creating_snake_head()
           self.creating_snake_moving_settings()
           self.creating_score_board()
           self.bind('<Any-KeyPress>',self.connecting_head_with_keys)

    # Initialisierung Score Board
    def creating_score_board(self):
           self.scoreboard=Tkinter.Label(self, text="Score : {}".format(self.score))
           self.scoreboard.pack(anchor='n')
           return

    # So wird unser Score Board aktualisiert wenn die Schlange Futter frisst
    def update_score_board(self):
           self.score=self.score+1
           self.scoreboard['text']="Score : {}".format(self.score)
           return

    # Einstellungen für die Schlangenbewegung
    def creating_snake_moving_settings(self):
           # die Schlange bewegt sich auf der x-Axe am Anfang
           self.x=SNAKE_MOVING_SPEED
           self.y=0
           self.roadmap=[(0,0)]
           self.bodylength=3
           self.snake_food=None
           self.gamevalid=1
           self.score=0
           return
    
    # Bewegung des Schlangenkopfs. Es wird definiert
    # welche Funktion bei welcher Taste aufgerufen wird
    def connecting_head_with_keys(self, event=None):
           key=event.keysym
           if key=='Left':
                  self.turn_left()
           elif key=='Right':
                  self.turn_right()
           elif key=='Up':
                  self.turn_up()
           elif key=='Down':
                  self.turn_down()
           else:
                  pass
           return
    
    def turn_left(self):
           self.x=-SNAKE_MOVING_SPEED
           self.y=0
           return

    def turn_right(self):
           self.x=SNAKE_MOVING_SPEED
           self.y=0
           return

    def turn_up(self):
           self.x=0
           self.y=-SNAKE_MOVING_SPEED
           return

    def turn_down(self):
           self.x=0
           self.y=SNAKE_MOVING_SPEED
           return
       
    # Schlangenkopf erstellen
    def creating_snake_head(self):
           self.snake=self.board.create_rectangle(1,1,11,11,fill=SNAKE_HEAD_COLOR)
           return

    # Creating Ground
    def creating_playground(self):
           self.board=Tkinter.Canvas(self, width=PLAYGROUND_WIDTH, height=PLAYGROUND_HEIGHT, background=PLAYGROUND_COLOR)
           self.board.pack(padx=10, pady=10)
           return

    # Der Kopf bewegt sich
    def moving_snake_head(self):
	   # Mit dieser Zeile bewegt sich der Kopf der Schlange	
           self.board.move(self.snake,self.x,self.y)
           # Mit diesen Zeilen überprüft man nach jedem Schritt ob der Kopf an den Rand des Spiels angekommen ist
           x1,y1,x2,y2=self.board.coords(self.snake)
           if x1<=0 or y1<=0:
                  self.x=0
                  self.y=0
                  self.game_loss()
           elif PLAYGROUND_HEIGHT<=y2 or PLAYGROUND_WIDTH<=x2:
                  self.x=0
                  self.y=0
                  self.game_loss()
           else:
                  pass
           return		

    # Spielende... verloren!
    def game_loss(self):
        self.board.create_text(PLAYGROUND_WIDTH/2,PLAYGROUND_HEIGHT/2,text="Game Over"\
		    ,font=('arial 30 bold'),fill='red')
        self.gamevalid=0
        return

    # Diese Funktion aktualisiert das Spiel
    # nach jedem Tastendruck
    def re_update(self):
        self.moving_snake_head()
        self.update_snake_body_structure()
        self.food_of_snake()
        return

    # Schlangenfutter
    def food_of_snake(self):
        if self.snake_food==None: #wenn es kein Futter gibt weil schon gefressen, mal ein Neues
            x1=random.randint(15,PLAYGROUND_WIDTH-15)
            y1=random.randint(15,PLAYGROUND_HEIGHT-15)
            self.snake_food=self.board.create_oval(x1,y1,x1+10,y1+10,fill='yellow', tag="food")
        if self.snake_food:
            x1,y1,x2,y2=self.board.coords(self.snake_food) #wo befindet sich gerade das Futter?
            if len(self.board.find_overlapping(x1,y1,x2,y2))==2: #hat der Schlangenkopf das Futter erreicht?
                self.board.delete("food")
                self.snake_food=None
                self.update_score_board()
        return


    # Wie bewegt sich der Schlangenkörper?
    def update_snake_body_structure(self):
        x1,y1,x2,y2=self.board.coords(self.snake)
        x2=(x2-((x2-x1)/2))
        y2=(y2-((y2-y1)/2))
        # In roadmap befinden sich alle “Vierecke” des Schlangenkörpers. Mit append addiere ich das letzte “Viereck”
        self.roadmap.append((x2,y2))
        # Mit jedem Schritt lösche ich den Körper und male ihn erneut an der nächsten Position
        self.board.delete('body')
        if len(self.roadmap)>=self.bodylength:
            self.roadmap=self.roadmap[-self.bodylength:]
            self.board.create_line(tuple(self.roadmap), tag="body",width=10,fill=SNAKE_BODY_COLOR)
        return
    
# So geht das Spiel los
if __name__ == '__main__':
    root=main(className=" Schlangenspiel ")
    # Es wird so lange gespielt wie “gamevalid” 1 ist
    while root.gamevalid:
        root.update()
        root.update_idletasks()
        # Diese Funktion aktualisiert das Spiel nach jedem Tastendruck
        root.re_update()
	# wir machen eine mini Pause zwischendurch
        # sonst ist das Spiel zu schnell für uns Menschen.. :)
        time.sleep(0.2)