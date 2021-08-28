add_library('peasycam')


class Cubie() :
    
    def __init__(self, x,y,z,scl):
        self.x = x*scl
        self.y = y*scl
        self.z = z*scl 
        self.scl = scl
        self.blanc =  [[-1,1,1,-1],
                       [-1,-1,1,1],
                       [-1,-1,-1,-1]]
        self.orange = [[-1,1,1,-1],
                       [-1,-1,1,1],
                       [1,1,1,1]]
        self.bleu =   [[1,1,1,1],
                       [-1,-1,1,1],
                       [-1,1,1,-1]]
        self.vert =   [[-1,-1,-1,-1],
                       [-1,-1,1,1],
                       [-1,1,1,-1]]
        self.rouge =  [[-1,1,1,-1],
                       [1,1,1,1],
                       [-1,-1,1,1]]
        self.jaune =  [[-1,1,1,-1],
                       [-1,-1,-1,-1],
                       [-1,-1,1,1]]
        
    def cube(self):
        r = self.scl/2
        stroke(0)
        strokeWeight(2)
        beginShape(QUADS)
        fill(255,255,255)
        for i in range(4):
            vertex(r*self.blanc[0][i] + self.x, r*self.blanc[1][i] + self.y, r*self.blanc[2][i] + self.z)
            
        fill(0,0,255)
        for i in range(4):
            vertex(r*self.bleu[0][i] + self.x, r*self.bleu[1][i] + self.y, r*self.bleu[2][i] + self.z)
            
        fill(255,0,0)
        for i in range(4):
            vertex(r*self.rouge[0][i] + self.x, r*self.rouge[1][i] + self.y, r*self.rouge[2][i] + self.z)
            
        fill(0,255,0)
        for i in range(4):
            vertex(r*self.vert[0][i] + self.x, r*self.vert[1][i] + self.y, r*self.vert[2][i] + self.z)
            
        fill(255,255,0)
        for i in range(4):
            vertex(r*self.jaune[0][i] + self.x, r*self.jaune[1][i] + self.y, r*self.jaune[2][i] + self.z)
            
        fill(243,114,32)
        for i in range(4):
            vertex(r*self.orange[0][i] + self.x, r*self.orange[1][i] + self.y, r*self.orange[2][i] + self.z)
        endShape()
        
        
    def turnX(self,a):
        rotX = [[1,0,0],
                [0,cos(a),-sin(a)],
                [0,sin(a),cos(a)]]
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.blanc[k][j]
        self.blanc = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.orange[k][j]
        self.orange = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.bleu[k][j]
        self.bleu = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.rouge[k][j]
        self.rouge = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.vert[k][j]
        self.vert = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.jaune[k][j]
        self.jaune = result
        
        
    def turnY(self,a):
        rotX = [[cos(a),0,sin(a)],
                [0,1,0],
                [-sin(a),0,cos(a)]]
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.blanc[k][j]
        self.blanc = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.orange[k][j]
        self.orange = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.bleu[k][j]
        self.bleu = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.rouge[k][j]
        self.rouge = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.vert[k][j]
        self.vert = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.jaune[k][j]
        self.jaune = result
        
    def turnZ(self,a):
        rotX = [[cos(a),-sin(a),0],
                [sin(a),cos(a),0],
                [0,0,1]]
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.blanc[k][j]
        self.blanc = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.orange[k][j]
        self.orange = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.bleu[k][j]
        self.bleu = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.rouge[k][j]
        self.rouge = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.vert[k][j]
        self.vert = result
        
        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    result[i][j] = result[i][j] + rotX[i][k] * self.jaune[k][j]
        self.jaune = result
        
        
        
def setup():
    global cam
    global cubies
    global scl
    size(480,480,P3D)
    cam = PeasyCam(this,500)
    cubies = []
    dim = 3
    scl = 60
    for i in range(-(dim // 2),(dim // 2) + 1):
        for j in range(-(dim // 2),(dim // 2) + 1):
            for k in range(-(dim // 2),(dim // 2) + 1):
                cubie = Cubie(i,j,k,scl)
                cubies.append(cubie)

def keyTyped():
    if key == 'q' or key == 'Q' :
        for cubie in cubies :
            if cubie.x == -1*scl :
                cubie.turnX(PI/2)
    if key == 'w' or key == 'W' :
        for cubie in cubies :
            if cubie.x == -1*scl :
                cubie.turnX(-PI/2)
    if key == 'a' or key == 'A' :
        for cubie in cubies :
            if cubie.x == 0 :
                cubie.turnX(PI/2)
    if key == 's' or key == 'S' :
        for cubie in cubies :
            if cubie.x == 0 :
                cubie.turnX(-PI/2)
    if key == 'z' or key == 'Z' :
        for cubie in cubies :
            if cubie.x == scl :
                cubie.turnX(PI/2)
    if key == 'x' or key == 'X' :
        for cubie in cubies :
            if cubie.x == scl :
                cubie.turnX(-PI/2)
                
    if key == 'e' or key == 'E' :
        for cubie in cubies :
            if cubie.y == -1*scl :
                cubie.turnY(PI/2)
    if key == 'r' or key == 'R' :
        for cubie in cubies :
            if cubie.y == -1*scl :
                cubie.turnY(-PI/2)
    if key == 'd' or key == 'D' :
        for cubie in cubies :
            if cubie.y == 0 :
                cubie.turnY(PI/2)
    if key == 'f' or key == 'F' :
        for cubie in cubies :
            if cubie.y == 0 :
                cubie.turnY(-PI/2)
    if key == 'c' or key == 'C' :
        for cubie in cubies :
            if cubie.y == scl :
                cubie.turnY(PI/2)
    if key == 'v' or key == 'V' :
        for cubie in cubies :
            if cubie.y == scl :
                cubie.turnY(-PI/2)
                
    if key == 't' or key == 'T' :
        for cubie in cubies :
            if cubie.z == -1*scl :
                cubie.turnZ(PI/2)
    if key == 'y' or key == 'Y' :
        for cubie in cubies :
            if cubie.z == -1*scl :
                cubie.turnZ(-PI/2)
    if key == 'g' or key == 'G' :
        for cubie in cubies :
            if cubie.z == 0 :
                cubie.turnZ(PI/2)
    if key == 'h' or key == 'H' :
        for cubie in cubies :
            if cubie.z == 0 :
                cubie.turnZ(-PI/2)
    if key == 'b' or key == 'B' :
        for cubie in cubies :
            if cubie.z == scl :
                cubie.turnZ(PI/2)
    if key == 'n' or key == 'N' :
        for cubie in cubies :
            if cubie.z == scl :
                cubie.turnZ(-PI/2)
    
        
    
def draw():
    global cubies
    global scl
    background(51)
    for cubie in cubies :
        cubie.cube()
        
    
        
    
    
    
    
    
        
