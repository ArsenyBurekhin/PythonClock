import ClockFace
import ClockNumbers
import ClockArrows
import Globals
import Clock
class clock_builder():
	@staticmethod
	def buildBlueSquereFaceWithNumbersAndRedArrows(size,surf):
		clockface = ClockFace.ClockSquareFace(surf,Globals.CALM_SEA,size)
		clockNumbers = ClockNumbers.ClockNumbers(surf,Globals.CALM_SEA,size)
		return Clock.Clock(surf,clockface,clockNumbers,Globals.STONE_RED,size)
		
	@staticmethod
	def buildYellowRoundFaceWithTicksAndBlueArrows(size,surf):
		clockface = ClockFace.ClockCycleFace(surf,Globals.HAPPY_LEMON,size)
		clockNumbers = ClockNumbers.ClockTicks(surf,Globals.HAPPY_LEMON,size)
		return Clock.Clock(surf,clockface,clockNumbers,Globals.CALM_SEA,size)
