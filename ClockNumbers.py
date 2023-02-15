import pygame
from Globals import PI,CENTER
import math
import pygame


class ClockBase:
	def __init__(self, surf, color, size):
		self.color = color
		self.size = size
		self.surf = surf
		
	def cordX(self,i):
			return math.cos(PI/6*i)* self.size 
	def cordY(self,i):	
  		return math.sin(PI/6*i)* self.size
							

class ClockNumbers(ClockBase):
	def draw(self):
		pygame.font.init()
		font = pygame.font.SysFont(None,35)

		for i in range(12):
			x = super().cordX(i-3)
			y = super().cordY(i-3)
			
			if i ==0:
				strNumber = "12"
			else:
				strNumber = str(i)
			text = font.render(strNumber,True,self.color)
			obj = text.get_rect()
			obj.center = (CENTER[0]+x, CENTER[1]+y)
			self.surf.blit(text, obj)
			

	
class ClockTicks(ClockBase):
	def draw(self):
		for i in range(12):
			x = super().cordX(i)
			y = super().cordY(i)
			pygame.draw.circle(self.surf,self.color,(CENTER[0]+x,CENTER[1]+y),4)
      
    