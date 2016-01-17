# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


class Nodeclass :
	def __init__(self):
		self.x = 0
		self.y = 0
	
	def setX(self,x):
		self.x = x
	def setY(self,y):
		self.y = y

	def getX(self):
		return self.x
	def getY(self):
		return self.y


SCR_WIDTH,SCR_HEIGHT = 1280,960
pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pygame.display.set_caption(u"test")
vx = vy = 120  # 1秒間の移動ピクセル
clock = pygame.time.Clock()

#背景色
screen.fill((255,255,255))
node = []

for var in range(0,10):
	x = random.randint(10,1270)
	y = random.randint(10,950)

	node.append(Nodeclass())
	node[var].setX(x)
	node[var].setY(y)
	pygame.draw.circle(screen,(0,0,0),(x,y),10)	#塗りつぶしなし
#	pygame.draw.circle(screen,(0,0,0),(x,y),10,1)	#塗りつぶし


#辺を作成していく
flg = 0
while flg < 10:
	nodeA = random.randint(0,var)
	nodeB = random.randint(0,var)
	pygame.draw.line(screen, (0,0,0), (node[nodeA].getX(),node[nodeA].getY()), (node[nodeB].getX(),node[nodeB].getY()))
	flg += 1	



#表示
pygame.display.update()



#終了条件
while True :
	for event in pygame.event.get():
		if event.type == QUIT: sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()

#画像を表示する
#img_rect=[]
#img = pygame.image.load("node.jpg").convert_alpha()
#img_rect.append( img.get_rect())
#img_rect[var].x = var * 100
#img_rect[var].y = 0

#screen.blit(img, img_rect[var])

#時間指定用　これを移動量に掛けて
#while True:
#	time_passed = clock.tick(60)  # 60fpsで前回からの経過時間を返す（ミリ秒）
#	time_passed_seconds = time_passed / 1000.0  # ミリ秒を秒に変換
	
