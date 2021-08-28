

def setup() :
    global img
    size(400,260)
    img = loadImage("kiss.PNG")
    
    
    
def draw() :
    image(img,0,0)
    loadPixels()
    
      
