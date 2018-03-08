
from ripcoinBlock import Block
import datetime as date

def nextBlock(lastBlock):

	thisIndex = lastBlock.index + 1
	thisTimestamp = date.datetime.now()
	thisData = {"TutMessage":"Hey! I'm block #" + str(thisIndex)}
	thisHash = lastBlock.hash
	
	return Block(thisIndex, thisTimestamp, thisData, thisHash)