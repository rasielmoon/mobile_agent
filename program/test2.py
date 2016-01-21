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

#############################################################################################################################
def draw_Line(nodeA,nodeB):
 	pygame.draw.line(screen, (0,0,0), (node[nodeA].getX(),node[nodeA].getY()), (node[nodeB].getX(),node[nodeB].getY()))

def set_destNode(nodeA,nodeB):
	node[nodeA].setDest(nodeB)
	node[nodeB].setDest(nodeA)

def draw_node(SCR_WIDTH,SCR_HEIGHT,node,nodex,nodey):
	node_size = 20
	dist = 10

	for vary in range(0,nodey):
		for varx in range(0,nodex):
			x =10  + node_size * 2 + varx * node_size * dist
			y =10  + node_size * 2 + vary * node_size * dist
			pygame.draw.circle(screen,(255,255,255),(x,y),node_size)	#塗りつぶし
			pygame.draw.circle(screen,(0,0,0),(x,y),node_size,2)	#枠
		 


def make_node(SCR_WIDTH,SCR_HEIGHT,node,nodex,nodey):
	node_size = 20
	node_num = 0
	dist = 10
	for vary in range(0,nodey):
		for varx in range (0,nodex):
			node.append(Nodeclass())
			x =10  + node_size * 2 + varx * node_size * dist
			y =10  + node_size * 2 + vary * node_size * dist

			node[node_num].setX(x)
			node[node_num].setY(y)
			node_num += 1

###########################木の作成##################################
	node_num = 0
	for vary in range (0,nodey):
		for varx in range(0,nodex):
			if vary == nodey-1 and varx == nodex-1:
				hoge = 0
			else:
				if vary == nodey-1:
					con = random.randint(0,1)
					if con == 1:
						set_destNode(node_num,node_num + 1)
						draw_Line(node_num,node_num + 1)

				else :
					if varx == 0:
						for hoge in range(0,3):
							con = random.randint(0,1)
							if con == 1:
								if hoge == 0:
									set_destNode(node_num,node_num + 1)
									draw_Line(node_num,node_num + 1)
								else:
									set_destNode(node_num,node_num + nodex + hoge - 1)
									draw_Line(node_num,node_num + nodex + hoge - 1)

							
					elif varx == nodex-1:
						for hoge in range(0,1):
							con = random.randint(0,1)
							if con == 1:
								set_destNode(node_num,node_num + nodex + hoge  - 1)
								draw_Line(node_num,node_num + nodex + hoge - 1)


					else:
						for hoge in range(0,4):
							con = random.randint(0,1)
							if con == 1:
								if hoge == 0:
									set_destNode(node_num,node_num + 1)
									draw_Line(node_num,node_num + 1)
								else:
									set_destNode(node_num,node_num + nodex + hoge - 2)
									draw_Line(node_num,node_num + nodex + hoge - 2)


						
			node_num += 1





#############################################################################################################################

pygame.init()
SCR_WIDTH,SCR_HEIGHT = 1280,960
screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pygame.display.set_caption(u"test")
vx = vy = 120  # 1秒間の移動ピクセル
clock = pygame.time.Clock()

#背景色
screen.fill((255,255,255))
node = []
nodex = 5
nodey = 5
node_num = nodex * nodey

make_node(SCR_WIDTH,SCR_HEIGHT,node,nodex,nodey)
print ("wire comp")
draw_node(SCR_WIDTH,SCR_HEIGHT,node,nodex,nodey)
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
	
