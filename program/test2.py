# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random

###################Node Class###################################
################################################################
class Nodeclass :
	def __init__(self):
		self.x = 0
		self.y = 0
		self.dest = []	#接続先ノード
	
	def setX(self,x):
		self.x = x
	def setY(self,y):
		self.y = y
	def setDest(self,dest):
		self.dest.append(dest)

	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getN(self):
		return len(self.dest)
	def getDest(self,portnum):
		return self.dest[portnum]

###############################################################



SCR_WIDTH,SCR_HEIGHT = 1280,960
pygame.init()
node_size = 20
screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pygame.display.set_caption(u"test")
vx = vy = 120  # 1秒間の移動ピクセル
clock = pygame.time.Clock()

#背景色
screen.fill((255,255,255))
node = []

for var in range(0,10):
	x = random.randint(node_size,SCR_WIDTH - node_size)
	y = random.randint(node_size,SCR_HEIGHT - node_size)

	node.append(Nodeclass())
	node[var].setX(x)
	node[var].setY(y)
	pygame.draw.circle(screen,(0,0,0),(x,y),node_size)	#塗りつぶしなし
#	pygame.draw.circle(screen,(0,0,0),(x,y),node_size,1)	#塗りつぶし



#辺を作成していく
flg = 1
flg2 = 0
###########################木の作成##################################
while flg != 0:
	flg = 0
	nodeA = 1
	nodeB = 1
	while nodeA == nodeB :
		nodeA = random.randint(0,var)
		nodeB = random.randint(0,var)

	print (str(nodeA) + " : " +str(node[nodeA].getN()))
	if node[nodeA].getN() != 0:
		for port in range(0,node[nodeA].getN()):
			if node[nodeA].getDest(port) == nodeB :
				flg2 = 1
				break
		
		
		if flg2 == 0:
			node[nodeA].setDest(nodeB)
			node[nodeB].setDest(nodeA)
 			pygame.draw.line(screen, (0,0,0), (node[nodeA].getX(),node[nodeA].getY()), (node[nodeB].getX(),node[nodeB].getY()))

		flg2 = 0

	else:	
		node[nodeA].setDest(nodeB)
		node[nodeB].setDest(nodeA)
		pygame.draw.line(screen, (0,0,0), (node[nodeA].getX(),node[nodeA].getY()), (node[nodeB].getX(),node[nodeB].getY()))

	for i in range(0,var):
		if node[i].getN() == 0:
			flg += 1

#表示
pygame.display.update()



#終了条件
while True :
	for event in pygame.event.get():
		if event.type == QUIT: sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()



##########################################################################################
##########################################################################################
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
	
