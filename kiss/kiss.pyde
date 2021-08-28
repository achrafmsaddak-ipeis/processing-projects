

def setup() :
    global particules
    global img
    global E
    size(500,650)
    img = loadImage('kiss.PNG')
    particules = []
    E = 160
    color
    img.loadPixels()
    for i in range(200) :
        for j in range(260) : 
            if (red(img.pixels[i + j*200]) + green(img.pixels[i + j*200]) + blue(img.pixels[i + j*200]))/3 <= E :
                particules.append([i,j])             
    img.updatePixels()
    len(particules)
    
    
    
    
def draw() :
    background(255)
    cx = 500
    cy = 325
    scl = 2.5
    stroke(160)
    for j in range(0,height,5) :
        line(0,j,width,j)
    #image(img,0,0)
    for particule in particules :
        stroke(0)
        strokeWeight(2.4)
        x = particule[0]*scl
        y = particule[1]*scl 
        line(x , y,x+3,y)

    
    
    
