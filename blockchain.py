blockchain = [12,20,30]

def get_last_blockchain_value():
    return blockchain[-1]

def add_blockchain(transaction_amount):

    blockchain.append(transaction_amount)
    
print ("Last value: {}".format( get_last_blockchain_value() ))

tx_amnt = input('Please enter an amount : ')
add_blockchain(tx_amnt)

print("My current blockchain: {}".format( blockchain ))

