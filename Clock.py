import ClockFace
import ClockNumbers
import ClockArrows
import Globals



class Clock:
	def __init__(self,surf,clockFace,clockBase,color,size):
		self.clockFace = clockFace
		self.clockBase = clockBase 
		self.hourlyArrow = ClockArrows.HourlyArrow(surf,color,size)
		self.minuteArrow = ClockArrows.MinuteArrow(surf,color,size)
		self.secoundArrow = ClockArrows.SecoundArrow(surf,color,size)
	
	def draw(self):
		self.clockFace.draw()
		self.clockBase.draw() 
		self.hourlyArrow.draw()
		self.minuteArrow.draw()
		self.secoundArrow.draw()
		
    