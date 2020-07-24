import pygame
import math

displayWidth = 800
displayHeight = 800

pygame.init()
win = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("a* pathfinding visualisation")

clock = pygame.time.Clock()

class Grid:
    def __init__(self, gridSizeX, gridSizeY, cellSize, barrierCells, startCell, endCell, drawMode):
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY
        self.cellSize = cellSize
        self.barrierCells = []
        self.startCell = []
        self.endCell = []
        self.drawMode = drawMode
    
    def drawGrid(self):
        for x in range(20, self.gridSizeX, 20):
            pygame.draw.line(win, (255,255,255), (x, 0), (x, 800))
        for y in range(20, self.gridSizeY, 20):
            pygame.draw.line(win, (255,255,255), (0, y), (800, y))
    
    def drawCells(self):
        for cell in self.barrierCells:
            pygame.draw.rect(win, (255,0,0), (cell[0], cell[1], 20,20))
       
    def getSurroundingNodes(self, cellX, cellY):
        return [(cellX-20, cellY-20), (cellX-20, cellY), (cellX-20, cellY + 20), (cellX, cellY+20), (cellX+20, cellY+20), (cellX+20, cellY), (cellX+20, cellY-20), (cellX, cellY-20)]
    
    def getDistanceFromNode(self, node1, node2):
        xDiff = node1[0] - node2[0]
        yDiff = node1[1] - node2[1]
        rawDist = math.sqrt(xDiff**2) + math.sqrt(yDiff**2)
        return [rawDist / 20]

def update():
    win.fill((0,0,0))
    grid.drawGrid()
    pygame.display.update()

def stepRound(x, base=20):
    return base * round(x/base)

grid = Grid(displayWidth, displayHeight, 20, [],[0,0], [0,0], "barrier")
grid.barrierCells.append((-20,-20))
while True:
    clock.tick(60)
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    currentMouseGrid = (stepRound(mouseX), stepRound(mouseY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                grid.barrierCells.pop()
            
            if event.key == pygame.K_r and grid.startCell and grid.endCell:
                print("startPos: ", int(grid.startCell[0] / 20), "|", int(grid.startCell[1] / 20))
                print("endPos: ", int(grid.endCell[0] / 20), "|", int(grid.endCell[1] / 20))
            
            if event.key == pygame.K_g:
                x = grid.getDistanceFromNode(grid.startCell, grid.endCell)
                print(x)

        if pygame.mouse.get_pressed()[0] and currentMouseGrid != grid.barrierCells[-1]:
            grid.barrierCells.append((stepRound(mouseX), stepRound(mouseY)))
        
        if pygame.mouse.get_pressed()[2]:
            grid.startCell.clear()
            grid.startCell.append(stepRound(mouseX))
            grid.startCell.append(stepRound(mouseY))
        
        if pygame.mouse.get_pressed()[1]:
            grid.endCell.clear()
            grid.endCell.append(stepRound(mouseX))
            grid.endCell.append(stepRound(mouseY))

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (stepRound(mouseX), stepRound(mouseY), 20 ,20))
    if grid.startCell:
        pygame.draw.rect(win, (0,255,0), (grid.startCell[0], grid.startCell[1], 20,20))
        #  for node in grid.getSurroundingNodes(grid.startCell[0], grid.startCell[1]):
        #     pygame.draw.rect(win, (100, 0,255), (node[0], node[1], 20, 20))
    if grid.endCell:
        pygame.draw.rect(win, (0,0,255), (grid.endCell[0], grid.endCell[1], 20,20))
    
    grid.drawGrid()
    grid.drawCells()
    pygame.display.update()
