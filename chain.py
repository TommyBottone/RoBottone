from hashlib import sha256
import time

class Transaction:
  def __init__(self, from_address, to_address, amount = 0):
    self.from_address = from_address
    self.to_address = to_address
    self.amount = amount  


class Block:
  def __init__(self, index, transactions, timestamp, previous_hash):
    self.index = index
    self.transactions = transactions
    self.timestamp = timestamp
    self.previous_hash = previous_hash
    self.nonce = 0

  def compute_hash(self):
    block_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.nonce)
    return sha256(block_string.encode()).hexdigest()


class Blockchain:
  # difficulty of our PoW algorithm
  difficulty = 2

  def __init__(self):
    self.unconfirmed_transactions = []
    self.chain = []
    self.create_genesis_block()

  def create_genesis_block(self):
    genesis_block = Block(0, [], time.time(), "0")
    genesis_block.hash = genesis_block.compute_hash()
    self.chain.append(genesis_block)

  @property
  def last_block(self):
    return self.chain[-1]

  def add_block(self, block, proof):
    previous_hash = self.last_block.hash

    if previous_hash != block.previous_hash:
        return False

    if not self.is_valid_proof(block, proof):
        return False

    block.hash = proof
    self.chain.append(block)
    return True

  def is_valid_proof(self, block, block_hash):
    return (block_hash.startswith('0' * Blockchain.difficulty) and
            block_hash == block.compute_hash())

  def proof_of_work(self, block):
    block.nonce = 0

    computed_hash = block.compute_hash()
    while not computed_hash.startswith('0' * Blockchain.difficulty):
        block.nonce += 1
        computed_hash = block.compute_hash()

    return computed_hash

  def add_new_transaction(self, transaction):
    self.unconfirmed_transactions.append(transaction)

  def mine(self):
    if not self.unconfirmed_transactions:
        return False

    last_block = self.last_block

    new_block = Block(index=last_block.index + 1,
                      transactions=self.unconfirmed_transactions,
                      timestamp=time.time(),
                      previous_hash=last_block.hash)

    proof = self.proof_of_work(new_block)
    self.add_block(new_block, proof)

    self.unconfirmed_transactions = []
    return new_block.index

blockchain = Blockchain()

def get_chain():
  chain_data = []
  for block in blockchain.chain:
    chain_data.append(block.__dict__)

  the_chain = ""
  i = 0
  for c in chain_data:
    i += 1
    the_chain += str(c) + "\n"
  if the_chain == "":
    the_chain = "empty"
  return the_chain

def mine_chain(owner):
  transactions = Transaction(from_address="OG", to_address=owner, amount=1)
  blockchain.add_new_transaction(transactions)
  blockchain.mine()
  return get_chain()