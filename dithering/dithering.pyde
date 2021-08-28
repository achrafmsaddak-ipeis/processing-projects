

def setup():
    global img
    size(600,448)
    img = loadImage('kitten.JPEG')
    #w = width // 2
    #image(img,0,0)
    #image(img,0,0)
    
    '''
    loadPixels()
    for y in range(height - 1) :
        for x in range(w,width - 1) :
            
            oldR, oldG , oldB =  pixels[x + width*y]
            
            newR = floor(oldR / 2 ) * 255
            newG = floor(oldB / 2 ) * 255
            newB = floor(oldG / 2 ) * 255
            pixels[x + width*y] = newR , newG , newB
            
            errorR = oldR - newR
            errorG = oldG - newG
            errorB = oldB - newB
            
            pixels[x + 1 + width*y][0] = pixels[x + 1 + width*y][0] + (7/16)*errorR
            pixels[x + 1 + width*y][1] = pixels[x + 1 + width*y][1] + (7/16)*errorG
            pixels[x + 1 + width*y][2] = pixels[x + 1 + width*y][2] + (7/16)*errorB
            
            pixels[x - 1 + width*(y+1)][0] = pixels[x - 1 + width*(y+1)][0] + (3/16)*errorR
            pixels[x - 1 + width*(y+1)][1] = pixels[x - 1 + width*(y+1)][1] + (3/16)*errorG
            pixels[x - 1 + width*(y+1)][2] = pixels[x - 1 + width*(y+1)][2] + (3/16)*errorB
            
            pixels[x  + width*(y+1)][0] = pixels[x  + width*(y+1)][0] + (5/16)*errorR
            pixels[x  + width*(y+1)][1] = pixels[x  + width*(y+1)][1] + (5/16)*errorG
            pixels[x  + width*(y+1)][2] = pixels[x  + width*(y+1)][2] + (5/16)*errorB
            
            pixels[x + 1 + width*(y+1)][0] = pixels[x + 1 + width*(y+1)][0] + (1/16)*errorR
            pixels[x + 1 + width*(y+1)][1] = pixels[x + 1 + width*(y+1)][1] + (1/16)*errorG
            pixels[x + 1 + width*(y+1)][2] = pixels[x + 1 + width*(y+1)][2] + (1/16)*errorB
            
    updatePixels()
            '''
            
    

def draw():
    global img
    w = width // 2
    image(img,0,0)
    #image(img,0,0)
    '''
    loadPixels()
    for y in range(height - 1) :
        for x in range(w,width - 1) :
            
            oldR, oldG , oldB =  pixels[x + width*y]
            
            newR = floor(oldR / 2 ) * 255
            newG = floor(oldB / 2 ) * 255
            newB = floor(oldG / 2 ) * 255
            pixels[x + width*y] = newR , newG , newB
            
            errorR = oldR - newR
            errorG = oldG - newG
            errorB = oldB - newB
            
            pixels[x + 1 + width*y][0] = pixels[x + 1 + width*y][0] + (7/16)*errorR
            pixels[x + 1 + width*y][1] = pixels[x + 1 + width*y][1] + (7/16)*errorG
            pixels[x + 1 + width*y][2] = pixels[x + 1 + width*y][2] + (7/16)*errorB
            
            pixels[x - 1 + width*(y+1)][0] = pixels[x - 1 + width*(y+1)][0] + (3/16)*errorR
            pixels[x - 1 + width*(y+1)][1] = pixels[x - 1 + width*(y+1)][1] + (3/16)*errorG
            pixels[x - 1 + width*(y+1)][2] = pixels[x - 1 + width*(y+1)][2] + (3/16)*errorB
            
            pixels[x  + width*(y+1)][0] = pixels[x  + width*(y+1)][0] + (5/16)*errorR
            pixels[x  + width*(y+1)][1] = pixels[x  + width*(y+1)][1] + (5/16)*errorG
            pixels[x  + width*(y+1)][2] = pixels[x  + width*(y+1)][2] + (5/16)*errorB
            
            pixels[x + 1 + width*(y+1)][0] = pixels[x + 1 + width*(y+1)][0] + (1/16)*errorR
            pixels[x + 1 + width*(y+1)][1] = pixels[x + 1 + width*(y+1)][1] + (1/16)*errorG
            pixels[x + 1 + width*(y+1)][2] = pixels[x + 1 + width*(y+1)][2] + (1/16)*errorB
            
    updatePixels()
            '''
            
            
