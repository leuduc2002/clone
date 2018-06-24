weight = 500
height = 600

class Ship:
    def __init__(self,w,h,x,y):
            self.w = w
            self.h = h
            self.x = x
            self.y = y

    def Move(self, pos):
        self.x = self.y
        self.y = pos[1] - self.h / 2
        if self.y < 0:
            self.y = 0
        if self.y > height - self.h:
            self.y = height - self.h

    def Draw(self):
        pygame.draw.rect(display_surf,WHITE,(self.x,self.y,self.w,self.h))

class ScoreBoard:
    def __init__(self,x,y,score,size):
        self.x = x
        self.y = y
        self.score = score
        self.font = pygame.font.Font(None,size)
    def display(self):
        display_score = self.font.render("Score: " + str(self.score),True , WHITE)
        display_surf.blit(display_score,(self.x,self.y))