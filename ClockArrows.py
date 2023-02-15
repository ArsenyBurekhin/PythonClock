import pygame
from  Globals import PI,CENTER
import math
import datetime
import pytz

class Arrow:
	def __init__(self,surf,color, size):
		self.color = color
		self.size = size
		self.surf = surf

	@staticmethod
	def current_time():
		return datetime.datetime.now().astimezone(pytz.timezone("Europe/Kyiv"))
		
	def draw(self,ticks,time,width,offset):
		
		X = math.cos(PI/ticks*time-PI/2)* (self.size -offset)
		Y = math.sin(PI/ticks*time-PI/2)* (self.size -offset)
		pygame.draw.line(self.surf, self.color,CENTER,(CENTER[0]+X  ,CENTER[1]+Y),width)


class HourlyArrow(Arrow):
	
	def draw(self):
		super().draw(6,Arrow.current_time().hour,5,35)
		
class MinuteArrow(Arrow):
	def draw(self):	
		super().draw(30,Arrow.current_time().minute,3,10)
		
class SecoundArrow(Arrow):
	def draw(self):	
		super().draw(30,Arrow.current_time().second,1,5)
