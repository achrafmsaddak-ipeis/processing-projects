mat1 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
mat2 = [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
mat3 = [[31, 32, 33], [34, 35, 36], [37, 38, 39]]
mat4 = [[41, 42, 43], [44, 45, 46], [47, 48, 49]]
mat5 = [[51, 52, 53], [54, 55, 56], [57, 58, 59]]
mat6 = [[61, 62, 63], [64, 65, 66], [67, 68, 69]]

horizantal = [mat1,mat2,mat3,mat4]
vertical = [mat5,mat2,mat6,mat4]
directions = [horizantal,vertical]

def transpose(mat):
    test = [[row[i] for row in mat] for i in range(len(mat[0]))] 
    return test



def rotate_clockwise(mat):
    corners = (mat[0][2],mat[2][0])
    mat[0][1:3] = mat[0][0:2]
    mat[2][0:2] = mat[2][1:3]
    mat[0][0] = mat[1][0]
    mat[2][2] = mat[1][2]
    mat[1][0] = corners[1]
    mat[1][2] = corners[0]
    return mat

def rotate_anticlockwise(mat):
    corners = (mat[0][0],mat[2][2])
    mat[2][1:3] = mat[2][0:2]
    mat[0][0:2] = mat[0][1:3]
    mat[0][2] = mat[1][2]
    mat[2][0] = mat[1][0]
    mat[1][0] = corners[0]
    mat[1][2] = corners[1]
    return mat

def move_horizantal(level,orientation,drc=0):
    if orientation :
        mat = directions[drc]
        aux = mat[0][level][:]
        mat[0][level] = mat[3][level] 
        mat[3][level] = mat[2][level] 
        mat[2][level] = mat[1][level]
        mat[1][level] = aux
        if level == 0 :
            rotate_anticlockwise(directions[drc-1][0])
        elif level == 2 :
            rotate_clockwise(directions[drc-1][2])
    else :
        mat = directions[drc]
        aux = mat[0][level][:] 
        mat[0][level] = mat[1][level] 
        mat[1][level] = mat[2][level] 
        mat[2][level] = mat[3][level]
        mat[3][level] = aux
        if level == 0 :
            rotate_clockwise(directions[drc-1][0])
        elif level == 2 :
            rotate_anticlockwise(directions[drc-1][2])


def move_vertical(level,orientation,drc=1):
    global mat1,mat2,mat3,mat4,mat5,mat6
    if orientation :
        mat = directions[drc]
        for i in range(4) :
            mat[i] = transpose(mat[i])
        aux = mat[0][level][:]
        mat[0][level] = mat[3][level] 
        mat[3][level] = mat[2][level] 
        mat[2][level] = mat[1][level]
        mat[1][level] = aux
        print(mat[1])
        for i in range(4) :
            mat[i] = transpose(mat[i])
        mat5 = mat[0]
        mat2 = mat[1]
        mat6 = mat[2]
        mat4 = mat[3]
        if level == 0 :
            rotate_clockwise(directions[drc-1][0])
        elif level == 2 :
            rotate_anticlockwise(directions[drc-1][2])
    else :
        mat = directions[drc]
        for i in range(4) :
            mat[i] = transpose(mat[i])
        aux = mat[0][level][:]
        mat[0][level] = mat[1][level] 
        mat[1][level] = mat[2][level] 
        mat[2][level] = mat[3][level]
        mat[3][level] = aux
        for i in range(4) :
            mat[i] = transpose(mat[i])
        mat5 = mat[0]
        mat2 = mat[1]
        mat6 = mat[2]
        mat4 = mat[3]
        if level == 0 :
            rotate_anticlockwise(directions[drc-1][0])
        elif level == 2 :
            rotate_clockwise(directions[drc-1][2])
            
            
def draw_mat(mat,x,y,scl):
    global colors
    for i in range(3) :
        for j in range(3) :
            stroke(0)
            strokeWeight(2)
            fill(colors[mat])
            rect(x + i*scl,y + j*scl,scl,scl)
    
    
def setup():
    global mat1,mat2,mat3,mat4,mat5,mat6
    global colors, positions
    global mats
    size(600,480)
    mats = [mat1,mat2,mat3,mat4,mat5,mat6]
    colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
    positions = [(60,180),(180,180),(300,180),(420,180),(180,60),(180,300)]
    

def keyPressed():
    global mat1,mat2,mat3,mat4,mat5,mat6
    global colors, positions
    global mats
    level = mouseY // 160
    if key == CODED :
        if keyCode == UP:
            move_vertical(level,False)
        elif keyCode == DOWN:
            move_vertical(level,True)
        elif keyCode == RIGHT:
            move_horizantal(level,True)
        elif keyCode == LEFT:
            move_horizantal(level,False)
    mats = [mat1,mat2,mat3,mat4,mat5,mat6]

    
    
        
    
def draw():
    global mats
    global mat1,mat2,mat3,mat4,mat5,mat6
    global colors, positions
    background(255)
    for k in range(6) :
        (x,y) = positions[k]
        for i in range(3) :
            for j in range(3) :
                stroke(0)
                strokeWeight(2)
                index = (mats[k][j][i])//10
                fill(colors[index-1][0],colors[index-1][1],colors[index-1][2])
                rect(x + i*40,y + j*40,40,40)
        
         
    

    
    
    
    
    
    
    
    
    
