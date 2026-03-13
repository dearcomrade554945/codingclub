import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        text = str(self.timestamp) + self.data + self.previous_hash
        return hashlib.sha256(text.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)


bc = Blockchain()
bc.add_block("Alice pays Bob 5 BTC")
bc.add_block("Bob pays Charlie 2 BTC")

for block in bc.chain:
    print(block.data, block.hash)