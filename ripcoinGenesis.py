
import ripcoinBlock
import datetime as date

def createGenesisBlock():

	#manually build a block
	return Block(0, date.datetime.now(), {"Block": "Genesis", "Joke":"Phil Collins Drumming"}, "0")