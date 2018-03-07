
import hashlib as hasher

class Block:

	def __init__(self, index, timestamp, data, previousHash):
	
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previousHash = previousHash
		self.hash = self.hashBlock()
		
	def hashBlock(self):
	
		sha = hasher.sha256()
		sha.update(str(self.index) +
				   str(self.timestamp) +
				   str(self.data) + 
				   str(self.previousHash)).encode()
		return sha.hexdigest()