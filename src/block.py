from core.transaction import Transaction
from typing import List, cast
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

	def toJson(self) -> str:
		d = {
			"hash" : self.hash
			"index" : self.index
			"timestamp" : self.timestamp
			"noonce": self.noonce,
            "previousHash": self.previousHash,
            "transactions": [],
		}
		for transaction in self.transactions:
            dTransactions = cast(List[Transaction], d["transactions"])
            dTransactions.append(transaction.asDict())

        return json.dumps(d, indent=4)

    def generateBlock(self):
    	

	
