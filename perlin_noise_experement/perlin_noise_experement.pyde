

def setup():
    global angles, particules
    global scl, rscl , stkw , F
    size(1280,720)
    noisescl = 0.04
    scl = 10
    rscl = 70
    init = 10000
    stkw = 0.4
    F = 5
    colorlower = 0
    colorupper = 190
    angles = []
    xoff = 0
    for x in range(width/scl) :
        angles.append([])
        yoff = 0
        for y in range(height/scl) :
            angles[x].append(map(noise(xoff,yoff),0,1,0,TWO_PI))
            yoff = yoff + noisescl
        xoff = xoff + noisescl
    particules = []
    for i in range(init) :
        particules.append([random(1,width-1),random(1,height-1),random(colorlower,colorupper)])
    
    background(255)
'''    
    stroke(180)
    for x in range(width/scl) :
        for y in range(height/scl) :
            hscl = + scl/2
            i = x*scl + hscl
            j = y*scl + hscl
            line(i,j,i+hscl*cos(angles[x][y]),j+hscl*sin(angles[x][y]))
            circle(i+hscl*cos(angles[x][y]),j+hscl*sin(angles[x][y]),1)
    '''    
def draw():
       
    for particule in particules :
        x = particule[0]
        y = particule[1]
        if (x > width - 1 ) or (x < 0 ) or (y > height -1 ) or (y < 0 ) :
            '''if len(particules) <= 1000 :
                particules.remove(particule)
                rx = floor(random(0,width)/(width/rscl))*(width/rscl)
                ry = floor(random(0,height)/(height/rscl))*(height/rscl)
                particules.append([rx,1,random(colorlower,colorupper)])
                particules.append([rx,height-1,random(colorlower,colorupper)])
                particules.append([1,ry,random(colorlower,colorupper)])
                particules.append([height-1,ry,random(colorlower,colorupper)])
            else : 
                particules.remove(particule)'''
            particules.remove(particule)
        else :
            x = x + F*cos(angles[floor(x/scl)][floor(y/scl)])
            if (x > width - 1 ) or (x < 0 ) : 
                particules.remove(particule)
            else :
                y = y + F*sin(angles[int(x/scl)][int(y/scl)])
                stroke(particule[2])
                strokeWeight(stkw)
                #strokeCap(SQUARE)
                #strokeJoin(ROUND)
                line(particule[0],particule[1],x,y)
                #point(x,y)
                particule[0] = x
                particule[1] = y
         
    if len(particules) <= 50 : 
        print('over')     
