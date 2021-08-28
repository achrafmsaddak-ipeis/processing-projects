

class Field() :
    
    def __init__(self,noisescl,scl,force) :
         self.noisescl = noisescl
         self.scl = scl
         self.force = force
         self.angles = []
         
    def generate(self,w,h):
        xoff = 0
        for x in range(w/self.scl) :
            self.angles.append([])
            yoff = 0
            for y in range(h/self.scl) :
                self.angles[x].append(map(noise(xoff,yoff),0,1,0,TWO_PI))
                yoff = yoff + self.noisescl
            xoff = xoff + self.noisescl
            
    def apply(self,x,y):
        
        i = int(x / self.scl)
        j = int(y / self.scl)
        
        try :
            return (self.force*cos(self.angles[i][j]),self.force*sin(self.angles[i][j]))
        except :
            return (0,0)
        
            
            
class Particule() :
    
    def __init__(self,x,y,stkw,colors):
        self.x = x
        self.y = y
        self.vx = 0 
        self.vy = 0
        self.stkw = stkw
        self.colors = colors
        
    def update(self,force) :
        prx = self.x
        pry = self.y
        self.ax = force[0]
        self.vx = self.vx + self.ax
        self.x = self.x + self.ax
        self.ay = force[1]
        self.vy = self.vy + self.ay
        self.y = self.y + self.ay
        
        stroke(self.colors[0],self.colors[1],self.colors[2])
        strokeWeight(self.stkw)
        line(prx,pry,self.x,self.y)
    
            



def setup():
    global particules1 , particules2 , particules3
    global field1 , field2 , field3
    size(480,480)
    init = 5000
    field1 = Field(0.05,15,1)
    field1.generate(width,height)
    
    field2 = Field(0.1,10,1)
    field2.generate(width,height)
    
    field3 = Field(0.5,4,1)
    field3.generate(width,height)
    
    particules1 = []
    for i in range(init) :
        particules1.append(Particule(random(1,width-1),random(1,height-1),0.4,(50,0,50)))
        
    particules2 = []
    for i in range(init) :
        particules1.append(Particule(random(1,width-1),random(1,height-1),0.4,(100,0,100)))
        
    particules3 = []
    for i in range(init) :
        particules3.append(Particule(random(1,width-1),random(1,height-1),0.4,(180,0,1850)))
        
    background(0)

frameindex = 0

def draw():
    global frameindex
    frameindex = frameindex + 1
    print(frameindex)
    
    if frameindex <= 50 :   
        for particule in particules1 :
    
            if (particule.x > width - 1 ) or (particule.x < 0 ) or (particule.y > height -1 ) or (particule.y < 0 ) :
                particules1.remove(particule)
            else :
                particule.update(field1.apply(particule.x,particule.y))
         
    if frameindex >= 50 : 
        for particule in particules2 :
    
            if (particule.x > width - 1 ) or (particule.x < 0 ) or (particule.y > height -1 ) or (particule.y < 0 ) :
                particules2.remove(particule)
            else :
                particule.update(field2.apply(particule.x,particule.y))
                
    if frameindex >= 100 : 
        for particule in particules3 :
    
            if (particule.x > width - 1 ) or (particule.x < 0 ) or (particule.y > height -1 ) or (particule.y < 0 ) :
                particules3.remove(particule)
            else :
                particule.update(field3.apply(particule.x,particule.y))
            
