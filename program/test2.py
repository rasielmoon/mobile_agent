# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
from multiprocessing import Pool
from multiprocessing import Process


###################agent Class###################################
class agentclass :
	def __init__(self):
		self.img = pygame.image.load("fig/agent1.png").convert_alpha()
		self.node = 0
		self.nextnode = 0
		self.stop = 0

	def setNode(self,node):
		self.node = node
	def setNextNode(self,node):
		self.nextnode = node
	def setStop(self):
		self.stop =1

	def getNode(self):
		return self.node
	def getNextNode(self):
		return self.nextnode
	def getStop(self):
		return self.stop
	
	
	def getIMG(self):
		return self.img

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
	node_num =0

	for vary in range(0,nodey):
		for varx in range(0,nodex):
			x =10  + node_size * 2 + varx * node_size * dist
			y =10  + node_size * 2 + vary * node_size * dist
			pygame.draw.circle(screen,(255,255,255),(x,y),node_size)	#塗りつぶし
			pygame.draw.circle(screen,(0,0,0),(x,y),node_size,2)	#枠
		 	
			num_N = font.render(str(node_num),True,(0,0,0))
			screen.blit(num_N,(x-5,y-5))
			node_num = node_num +1


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

#############################################################################################################################
def agent_move(all_agent,screen,step,clk,agent_num):
	if agent[agent_num].getStop() != 1 :
		if clk == 0:
#			print agent[agent_num].getNode()
			for x in range(0,all_agent):
				if x != agent_num :
					if agent[x].getNode() == agent[agent_num].getNode() :
						if  agent_num > x :
							agent[agent_num].setStop()
							agent[agent_num].setNode(-1)
			if agent[agent_num].getStop() == 0 :
				portN = node[agent[agent_num].getNode()].getN()-1
				portN = random.randint(0,portN)####################################################################
				agent[agent_num].setNextNode(node[agent[agent_num].getNode()].getDest(portN))
				x = node[agent[agent_num].getNode()].getX()
				y = node[agent[agent_num].getNode()].getY()
				screen.blit(agent[agent_num].getIMG(),(x-20,y-20))
		
		elif clk == 100 :
			agent[agent_num].setNode(agent[agent_num].getNextNode())
		
		else :
			target_x = node[agent[agent_num].getNextNode()].getX()
			target_y = node[agent[agent_num].getNextNode()].getY()
		
			x = node[agent[agent_num].getNode()].getX()
			y = node[agent[agent_num].getNode()].getY()
			vx = (target_x - x)/step
			vy = (target_y - y)/step
			
			x = x + vx * clk
			y = y + vy * clk
			screen.blit(agent[agent_num].getIMG(),(x-20,y-20))


#############################################################################################################################

pygame.init()
SCR_WIDTH,SCR_HEIGHT = 1000,1000
screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pygame.display.set_caption(u"Demo")
clock = pygame.time.Clock()
step = 100
agent_num =1
agent =[]
font = pygame.font.Font(None, 15)
flg = 0

#背景色
screen.fill((255,255,255))
while(flg == 0):
	flg = 1
	node = []
	nodex = 5
	nodey = 5
	node_num = nodex * nodey
	make_node(SCR_WIDTH,SCR_HEIGHT,node,nodex,nodey)
	for i in range(0,node_num) :
		if node[i].getN() == 0:
			flg = 0

print ("wire comp")
draw_node(SCR_WIDTH,SCR_HEIGHT,node,nodex,nodey)

for i in range(0,agent_num):
	agent.append(agentclass())
	agent[i].setNode(random.randint(0,node_num-1))



#表示
pygame.display.update()
pygame.image.save(screen,"background.bmp")
back = pygame.image.load("background.bmp").convert()
clk = 0
while True :
	count = 0
	for x in range(0,agent_num):
		if agent[x].getStop() == 0:
			count = count + 1

	if count == 1:
		font = pygame.font.Font(None, 200)
		text = font.render("Complete!!!!!",True,(0,0,0))
		screen.blit(text,(100,400))
		pygame.display.update()
	if count > 1 :
		screen.blit(back,(0,0))
		for x in range(0,agent_num):
			agent_move(agent_num,screen,step,clk,x)
	
		pygame.display.update()

		if clk == 100 :
			clk = 0	
	
		else :
			clk = clk + 1

	for event in pygame.event.get():
		if event.type == QUIT: sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			agent.append(agentclass())
			i = i + 1
			hoge = random.randint(0,node_num-1)
			agent[i].setNode(hoge)
			agent[i].setNextNode(hoge)
			agent_num = agent_num + 1



#move(clock,back,agentIMG)

#screen.blit(back,(0,0))
#pygame.display.update()


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
	
