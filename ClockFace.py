
import pygame
from Globals import CENTER
class ClockFace():
	def __init__(self, surf, color, size):
		self.color = color
		self.size = size
		self.surf = surf
		
	
class ClockCycleFace(ClockFace):
	def draw(self):  
  		pygame.draw.circle(self.surf, self.color,(CENTER),self.size,1)
	
class ClockSquareFace(ClockFace):	
	def draw(self):  
  		pygame.draw.rect(self.surf, self.color,pygame.Rect(CENTER[0]- self.size -5,CENTER[1]-self.size -5,self.size*2+5,self.size*2+5),1)
	 		
	