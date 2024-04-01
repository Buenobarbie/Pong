import pygame
import random
pygame.init()

win_width = 1280
win_height = 700

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Pong")
run = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30,True)		

def show_score():
	text1 = font.render(f'Score : {p1.score}', 1 ,(255,255,255))
	text2 = font.render(f'Score : {p2.score}', 1 ,(255,255,255))

	win.blit(text1 , (60,20))
	win.blit(text2 , (680,20))

class Player():

	def __init__(self,x,y,color):
		self.x  = self.initialx = x 
		self.y = self.initialy = y 
		self.width = 10
		self.height = 70
		self.color = color 
		self.vel = 10
		
		self.score = 0

	def rec(self):
		return  pygame.Rect(self.x,self.y,self.width,self.height)

	def draw(self):
		pygame.draw.rect(win,self.color,(int(self.x), int(self.y),self.width,self.height))

class Ball():
	def __init__(self,size,x,y, color):
		self.x = self.initial_x = x
		self.y = self.initial_y = y 
		self.color = color 
		self.size = size
		self.vel_x = self.vel_y = 7
		


	def rec(self):
		return  pygame.Rect(self.x,self.y,self.size,self.size)
	

	def draw(self):	
		pygame.draw.ellipse(win ,self.color,self.rec())

	def restart(self):
		self.x = self.initial_x
		self.y = self.initial_y
		self.vel_x *= random.choice((1,-1))


def draw_win():
	win.fill((0,0,0))
	p1.draw()
	p2.draw()
	ball.draw()

	pygame.draw.aaline(win,(200,200,200),(win_width/2,0),(win_width/2,win_height))


	show_score()

	pygame.display.update()

def ball_move():
	ball.x += ball.vel_x
	ball.y += ball.vel_y

	ball.top = ball.y - ball.size/2
	ball.bottom = ball.y + ball.size/2
	ball.left = ball.x - ball.size/2
	ball.right = ball.x + ball.size/2


	if ball.top <= 0 or ball.bottom >= win_height:
		ball.vel_y*= -1

	if ball.left <= 0  :
		p2.score +=1
		ball.restart()
	
	if ball.right >= win_width:
		p1.score +=1
		ball.restart()

	if ball.rec().colliderect(p1.rec()) or ball.rec().colliderect(p2.rec()):
		ball.vel_x*= -1		

p1 = Player(40, win_height/2,(200,200,200))
p2 = Player(win_width-p1.x -p1.width , win_height/2, (200,200,200))
size = 20
ball = Ball(size,win_width/2 - size/2, win_height/2 - size/2 , (200,200,200))

count = 0
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	ball_move()
	keys = pygame.key.get_pressed()

	#PLAYER 1
	if keys[pygame.K_w] and p1.y >=p1.vel:
		p1.y -= p1.vel
	if keys[pygame.K_s] and win_height - p1.y - p1.height >= p1.vel:
		p1.y += p1.vel



	#PLAYER 2
	if p2.y - p2.height/2 > ball.y  and p2.y >=p2.vel:
		p2.y -= p2.vel
	if p2.y - p2.height/2 < ball.y and win_height - p2.y - p2.height >= p2.vel:
		p2.y += p2.vel

	if count >0:
		count -= 1

	if keys[pygame.K_SPACE] and count == 0 :
		count = 10
		
		if ball.vel_x != 0:
			a = ball.vel_x
			b = ball.vel_y
			ball.vel_x = 0
			ball.vel_y = 0
		else:
			ball.vel_x = a
			ball.vel_y = b


	clock.tick(60)
	draw_win()

pygame.quit()