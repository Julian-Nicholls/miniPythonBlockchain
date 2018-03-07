
import ripcoinGenesis as gen


#create chain & genesis block
blockchain = [gen.createGenesisBlock()]
previousBlock = blockchain[0] 

numOfBlocksToAdd = 25

#add blocks to chain
for i in range(0, numOfBlocksToAdd):

	blockToAdd = nextBlock(previousBlock)
	blockchain.append(blockToAdd)
	previousBlock = blockToAdd
	
	#print results
	print ('Block #{} added to chain'.format(blockToAdd.index))
	print ("Hash: {}\n".format(blockToAdd.hash))