class HashTableEntry:
	"""
	Linked List hash table key/value pair
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

	# Hash table can't have fewer than this many slots
	MIN_CAPACITY = 9

class HashTable:
	"""
	A hash table with 'capacity' buckets
	that accepts string keys
	"""

	def __init__(self, capacity):
		self.capacity = capacity # Number of buckets in the hash table
		self.storage = [None] * capacity
		self.item_count = 0

	def get_num_slot(self):
		"""
		Return the length of the list you're using to hold the hash
		table data.  (Not the number of items stored in the hash table,
		but the number of slots in the main list.)
		One of the tests relies on this.
		"""


	def get_load_factor(self):
		"""
		Return the load factor for this hash table.
		"""
		return self.item_count / self.capacity

	def resize(self, new_capacity):
		"""
		Changes the capacity of the hash table
		and rehashes all key/value pairs.
		"""
		old_storage = self.storage
		self.capacity = new_capacity
		self.storage = [None] * self.capacity

		current_entry = None

		# Save this because put adds to it, and we don't want that.
		# It might be less hackish to pass a flag to put indicating that
		# We're in a resize and don't want to modify item count
		old_item_count = self.item_count

		for bucket_item in old_storage:
			current_entry = bucket_item
			while current_entry is not None:
				self.put(current_entry.key, current_entry.value)
				current_entry = current_entry.next

		# Restore this to the correct number
		self.item_count = old_item_count

	def djb2(self, key):
		"""
		DJB2 hash, 32-bit
		Implement this, and/or FNV-1
		"""
		str_key = str(key).encode()

		hash_value = 5381

		#hash = FNV_offset_basis_64

		for b in str_key:
			hash_value = ((hash_value << 5) + hash_value) + b
			# hash ^= b
			hash_value &= 0xffffffff # 64 bit hash

		return hash_value

	def hash_index(self, key):
		"""
		Take an arbitrary key and return a valid integer index
		within the hash table's storage capacity.
		"""
		return self.djb2(key) % self.capacity

	def put(self, key, value):
		"""
		Store the value with the given key.
		Hash collisions should be handled with Linked List Chaining.
		"""
		index = self.hash_index(key)

		current_entry = self.storage[index]

		while current_entry is not None and current_entry.key != key:
			current_entry = current_entry.next

		if current_entry is not None:
			current_entry.value = value
		else:
			new_entry = HashTableEntry(key, value)
			new_entry.next = self.storage[index]
			self.storage[index] = new_entry

			self.item_count += 1

			if self.get_load_factor() > 0.7:
				self.resize(self.capacity * 2)

	def delete(self, key):
		"""
		Remove the value stored with the given key.
		Print a warning if the key is not found
		"""
		try:
			index = self.hash_index(key)
		except KeyError:
			print('Key Not Found')

		self.storage[index] = None

	def get(self, key):
		"""
		Retrieve the value stored with the given key.
		Returns None if the key is not found.
		"""
		index = self.hash_index(key)
		return self.storage[index]
