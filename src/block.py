from core.transaction import Transaction
from Crypto.Hash import SHA256

class Block:

	def __init__(self,index:int,timestamp:float,noonce: int,transcations: List[Transcation],previousHash: str):

		self.index = index
		self.timestamp = timestamp
		self.noonce = noonce
		self.transcations = transcations
		self.previousHash = previousHash
		self.hash = hashBlock(
            index=index,
            timestamp=timestamp,
            transactions=transactions,
            noonce=noonce,
            previousHash=previousHash)


