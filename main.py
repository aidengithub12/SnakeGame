import pygame
import random
running = True
GREEN = (0,  255,  0)
BLACK = (0,  0,  0)
FPS = 30
WIDTH = 500 #YOUR WIDTH
HEIGHT = 500 #YOUR HEIGHT
velocityX = 0 #pixels per frame : not needed but fun to have
velocityY = 0
score = 0
tab = pygame.display.set_mode((WIDTH, HEIGHT)) #window width and height
pygame.init()
all_sprites = pygame.sprite.Group() #groupes all sprites
collidable = pygame.sprite.Group()
food = pygame.sprite.Group()
all_sprites.update()
tab.fill(BLACK) #any color
all_sprites.draw(tab)
clock = pygame.time.Clock()

'''
        if pygame.sprite.spritecollide(level.right_paddle, balls, False):
            ball.bounce_edge()
        if pygame.sprite.spritecollide(level.left_paddle, balls, False):
            ball.bounce_edge()

'''
class app(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("apple.png")
        self.rect = self.image.get_rect()
        self.rect.center = (((WIDTH/2) - random.randint(-100,100), (HEIGHT/2) - random.randint(-100,100)))
    def update(self):
        pass
class snake(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load("snake_part.png")
      self.rect = self.image.get_rect()
      self.rect.center = (WIDTH/2, HEIGHT/2)
      self.position = list(self.rect.center)
      self.lastpos = self.position
      self.velocityX = 0
      self.velocityY = 0
   def update(self):
        
        
        
        key = pygame.key.get_pressed()
        if(self.rect.x >= (WIDTH)):
            print("HIT EDGE")
            
            #remove sprite
            pass
        elif(self.rect.x <= 0):
            #remove sprite
            print("HIT EDGE")
            pass
        elif(self.rect.y <= 0):
            #remove sprite
            print("HIT EDGE")
            pass
        elif(self.rect.y >= (HEIGHT)):
            #remove sprite
            print("HIT EDGE")
            pass
        else:
            if key[pygame.K_RIGHT]:self.rect.x += 10
            if key[pygame.K_LEFT]:self.rect.x -= 10
            if key[pygame.K_UP]:self.rect.y -= 10
            if key[pygame.K_DOWN]:self.rect.y += 10
            if key[pygame.K_RIGHT]:self.position[0] += 10
            if key[pygame.K_LEFT]:self.position[0] -= 10
            if key[pygame.K_UP]:self.position[1] -= 10
            if key[pygame.K_DOWN]:self.position[1] += 10
        print("Current position: " + str(self.position))
        print("Last Position: " + str(self.lastpos))
        self.velocityX = (self.lastpos[0] - self.position[0]) / FPS
        self.velocityY = (self.lastpos[1] - self.position[1]) / FPS
def Logic(player: snake):
    
    pass
  
# class Player(pygame.sprite.Sprite):
#  #your Character
#  def __init__(self):
#     pygame.sprite.Sprite.__init__(self)
#     self.image = pygame.image.load("Ship.png") #your image or shape/sprites look
#     self.rect = self.image.get_rect()
#     self.rect.center = (WIDTH / 2, (HEIGHT / 2)) #sprites Position
#  def update(self):
#    key = pygame.key.get_pressed()
#    #stop at edge commands (might need to ajust)
#    if(self.rect.x >= (WIDTH-200)):
#       self.rect.x -= 10
#    elif(self.rect.x <= 0):
#       self.rect.x += 10
#    elif(self.rect.y <= 0):
#       self.rect.y += 10
#    elif(self.rect.y >= (HEIGHT-200)):
#     self.rect.y -= 10
#    else:
#     #sprites move commands
#     if key[pygame.K_RIGHT]:self.rect.x += 10
#     if key[pygame.K_LEFT]:self.rect.x -= 10
#     if key[pygame.K_UP]:self.rect.y -= 10
#     if key[pygame.K_DOWN]:self.rect.y += 10



snakePlayer = snake()
apple = app()
all_sprites.add(snakePlayer)
all_sprites.add(apple)

food.add(apple)
while (running):
 clock.tick(FPS)
 if pygame.sprite.spritecollide(snakePlayer, collidable, False):
    print("GAME OVER")
    snakePlayer.kill()
 if pygame.sprite.spritecollide(snakePlayer,food,False):
    # print("YUMMY")
    apple.kill()
    c = app()
    apple = c
    all_sprites.add(apple)
    food.add(apple)
    score += 1
 
 snakePlayer.lastpos = snakePlayer.position
 for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
 all_sprites.update() #updates screen
 print("vX: " + str(velocityX) + "\nvY: " + str(velocityY))
 
 tab.fill('white')
 all_sprites.draw(tab) #adds all sprites to the screen
 pygame.display.flip()